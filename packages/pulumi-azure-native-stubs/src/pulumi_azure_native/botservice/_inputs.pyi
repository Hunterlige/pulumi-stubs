import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict, Union
from ._enums import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AcsChatChannelArgs",
    "AcsChatChannelArgsDict",
    "AlexaChannelPropertiesArgs",
    "AlexaChannelPropertiesArgsDict",
    "AlexaChannelArgs",
    "AlexaChannelArgsDict",
    "BotPropertiesArgs",
    "BotPropertiesArgsDict",
    "ConnectionSettingParameterArgs",
    "ConnectionSettingParameterArgsDict",
    "ConnectionSettingPropertiesArgs",
    "ConnectionSettingPropertiesArgsDict",
    "DirectLineChannelPropertiesArgs",
    "DirectLineChannelPropertiesArgsDict",
    "DirectLineChannelArgs",
    "DirectLineChannelArgsDict",
    "DirectLineSiteArgs",
    "DirectLineSiteArgsDict",
    "DirectLineSpeechChannelPropertiesArgs",
    "DirectLineSpeechChannelPropertiesArgsDict",
    "DirectLineSpeechChannelArgs",
    "DirectLineSpeechChannelArgsDict",
    "EmailChannelPropertiesArgs",
    "EmailChannelPropertiesArgsDict",
    "EmailChannelArgs",
    "EmailChannelArgsDict",
    "FacebookChannelPropertiesArgs",
    "FacebookChannelPropertiesArgsDict",
    "FacebookChannelArgs",
    "FacebookChannelArgsDict",
    "FacebookPageArgs",
    "FacebookPageArgsDict",
    "KikChannelPropertiesArgs",
    "KikChannelPropertiesArgsDict",
    "KikChannelArgs",
    "KikChannelArgsDict",
    "LineChannelPropertiesArgs",
    "LineChannelPropertiesArgsDict",
    "LineChannelArgs",
    "LineChannelArgsDict",
    "LineRegistrationArgs",
    "LineRegistrationArgsDict",
    "M365ExtensionsArgs",
    "M365ExtensionsArgsDict",
    "MsTeamsChannelPropertiesArgs",
    "MsTeamsChannelPropertiesArgsDict",
    "MsTeamsChannelArgs",
    "MsTeamsChannelArgsDict",
    "OmnichannelArgs",
    "OmnichannelArgsDict",
    "OutlookChannelArgs",
    "OutlookChannelArgsDict",
    "PrivateLinkServiceConnectionStateArgs",
    "PrivateLinkServiceConnectionStateArgsDict",
    "SearchAssistantArgs",
    "SearchAssistantArgsDict",
    "SkuArgs",
    "SkuArgsDict",
    "SkypeChannelPropertiesArgs",
    "SkypeChannelPropertiesArgsDict",
    "SkypeChannelArgs",
    "SkypeChannelArgsDict",
    "SlackChannelPropertiesArgs",
    "SlackChannelPropertiesArgsDict",
    "SlackChannelArgs",
    "SlackChannelArgsDict",
    "SmsChannelPropertiesArgs",
    "SmsChannelPropertiesArgsDict",
    "SmsChannelArgs",
    "SmsChannelArgsDict",
    "TelegramChannelPropertiesArgs",
    "TelegramChannelPropertiesArgsDict",
    "TelegramChannelArgs",
    "TelegramChannelArgsDict",
    "TelephonyChannelPropertiesArgs",
    "TelephonyChannelPropertiesArgsDict",
    "TelephonyChannelResourceApiConfigurationArgs",
    "TelephonyChannelResourceApiConfigurationArgsDict",
    "TelephonyChannelArgs",
    "TelephonyChannelArgsDict",
    "TelephonyPhoneNumbersArgs",
    "TelephonyPhoneNumbersArgsDict",
    "WebChatChannelPropertiesArgs",
    "WebChatChannelPropertiesArgsDict",
    "WebChatChannelArgs",
    "WebChatChannelArgsDict",
    "WebChatSiteArgs",
    "WebChatSiteArgsDict",
]

class AcsChatChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AcsChatChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AlexaChannelPropertiesArgsDict(TypedDict):
    alexa_skill_id: pulumi.Input[_builtins.str]
    is_enabled: pulumi.Input[_builtins.bool]

@pulumi.input_type
class AlexaChannelPropertiesArgs:
    def __init__(
        __self__,
        *,
        alexa_skill_id: pulumi.Input[_builtins.str],
        is_enabled: pulumi.Input[_builtins.bool],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="alexaSkillId")
    def alexa_skill_id(self) -> pulumi.Input[_builtins.str]: ...
    @alexa_skill_id.setter
    def alexa_skill_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[_builtins.bool]): ...

class AlexaChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[AlexaChannelPropertiesArgsDict]]

@pulumi.input_type
class AlexaChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[AlexaChannelPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[AlexaChannelPropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[AlexaChannelPropertiesArgs]]): ...

class BotPropertiesArgsDict(TypedDict):
    display_name: pulumi.Input[_builtins.str]
    endpoint: pulumi.Input[_builtins.str]
    msa_app_id: pulumi.Input[_builtins.str]
    all_settings: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    app_password_hint: NotRequired[pulumi.Input[_builtins.str]]
    cmek_key_vault_url: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    developer_app_insight_key: NotRequired[pulumi.Input[_builtins.str]]
    developer_app_insights_api_key: NotRequired[pulumi.Input[_builtins.str]]
    developer_app_insights_application_id: NotRequired[pulumi.Input[_builtins.str]]
    disable_local_auth: NotRequired[pulumi.Input[_builtins.bool]]
    icon_url: NotRequired[pulumi.Input[_builtins.str]]
    is_cmek_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_streaming_supported: NotRequired[pulumi.Input[_builtins.bool]]
    luis_app_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    luis_key: NotRequired[pulumi.Input[_builtins.str]]
    manifest_url: NotRequired[pulumi.Input[_builtins.str]]
    msa_app_msi_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    msa_app_tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    msa_app_type: NotRequired[pulumi.Input[Union[_builtins.str, MsaAppType]]]
    open_with_hint: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    public_network_access: NotRequired[
        pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
    ]
    publishing_credentials: NotRequired[pulumi.Input[_builtins.str]]
    schema_transformation_version: NotRequired[pulumi.Input[_builtins.str]]
    storage_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BotPropertiesArgs:
    def __init__(
        __self__,
        *,
        display_name: pulumi.Input[_builtins.str],
        endpoint: pulumi.Input[_builtins.str],
        msa_app_id: pulumi.Input[_builtins.str],
        all_settings: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        app_password_hint: Optional[pulumi.Input[_builtins.str]] = ...,
        cmek_key_vault_url: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        developer_app_insight_key: Optional[pulumi.Input[_builtins.str]] = ...,
        developer_app_insights_api_key: Optional[pulumi.Input[_builtins.str]] = ...,
        developer_app_insights_application_id: Optional[
            pulumi.Input[_builtins.str]
        ] = ...,
        disable_local_auth: Optional[pulumi.Input[_builtins.bool]] = ...,
        icon_url: Optional[pulumi.Input[_builtins.str]] = ...,
        is_cmek_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_streaming_supported: Optional[pulumi.Input[_builtins.bool]] = ...,
        luis_app_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        luis_key: Optional[pulumi.Input[_builtins.str]] = ...,
        manifest_url: Optional[pulumi.Input[_builtins.str]] = ...,
        msa_app_msi_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        msa_app_tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        msa_app_type: Optional[pulumi.Input[Union[_builtins.str, MsaAppType]]] = ...,
        open_with_hint: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        public_network_access: Optional[
            pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]
        ] = ...,
        publishing_credentials: Optional[pulumi.Input[_builtins.str]] = ...,
        schema_transformation_version: Optional[pulumi.Input[_builtins.str]] = ...,
        storage_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @endpoint.setter
    def endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="msaAppId")
    def msa_app_id(self) -> pulumi.Input[_builtins.str]: ...
    @msa_app_id.setter
    def msa_app_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allSettings")
    def all_settings(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @all_settings.setter
    def all_settings(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="appPasswordHint")
    def app_password_hint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_password_hint.setter
    def app_password_hint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cmekKeyVaultUrl")
    def cmek_key_vault_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cmek_key_vault_url.setter
    def cmek_key_vault_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="developerAppInsightKey")
    def developer_app_insight_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @developer_app_insight_key.setter
    def developer_app_insight_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="developerAppInsightsApiKey")
    def developer_app_insights_api_key(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @developer_app_insights_api_key.setter
    def developer_app_insights_api_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="developerAppInsightsApplicationId")
    def developer_app_insights_application_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @developer_app_insights_application_id.setter
    def developer_app_insights_application_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableLocalAuth")
    def disable_local_auth(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_local_auth.setter
    def disable_local_auth(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="iconUrl")
    def icon_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @icon_url.setter
    def icon_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isCmekEnabled")
    def is_cmek_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_cmek_enabled.setter
    def is_cmek_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isStreamingSupported")
    def is_streaming_supported(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_streaming_supported.setter
    def is_streaming_supported(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="luisAppIds")
    def luis_app_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @luis_app_ids.setter
    def luis_app_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="luisKey")
    def luis_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @luis_key.setter
    def luis_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="manifestUrl")
    def manifest_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @manifest_url.setter
    def manifest_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="msaAppMSIResourceId")
    def msa_app_msi_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @msa_app_msi_resource_id.setter
    def msa_app_msi_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="msaAppTenantId")
    def msa_app_tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @msa_app_tenant_id.setter
    def msa_app_tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="msaAppType")
    def msa_app_type(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, MsaAppType]]]: ...
    @msa_app_type.setter
    def msa_app_type(
        self, value: Optional[pulumi.Input[Union[_builtins.str, MsaAppType]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="openWithHint")
    def open_with_hint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @open_with_hint.setter
    def open_with_hint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(
        self,
    ) -> Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]: ...
    @public_network_access.setter
    def public_network_access(
        self, value: Optional[pulumi.Input[Union[_builtins.str, PublicNetworkAccess]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="publishingCredentials")
    def publishing_credentials(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @publishing_credentials.setter
    def publishing_credentials(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="schemaTransformationVersion")
    def schema_transformation_version(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @schema_transformation_version.setter
    def schema_transformation_version(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="storageResourceId")
    def storage_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @storage_resource_id.setter
    def storage_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionSettingParameterArgsDict(TypedDict):
    key: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionSettingParameterArgs:
    def __init__(
        __self__,
        *,
        key: Optional[pulumi.Input[_builtins.str]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ConnectionSettingPropertiesArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ConnectionSettingParameterArgsDict]]]
    ]
    provisioning_state: NotRequired[pulumi.Input[_builtins.str]]
    scopes: NotRequired[pulumi.Input[_builtins.str]]
    service_provider_display_name: NotRequired[pulumi.Input[_builtins.str]]
    service_provider_id: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ConnectionSettingPropertiesArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionSettingParameterArgs]]]
        ] = ...,
        provisioning_state: Optional[pulumi.Input[_builtins.str]] = ...,
        scopes: Optional[pulumi.Input[_builtins.str]] = ...,
        service_provider_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_provider_id: Optional[pulumi.Input[_builtins.str]] = ...,
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
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ConnectionSettingParameterArgs]]]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ConnectionSettingParameterArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceProviderDisplayName")
    def service_provider_display_name(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_provider_display_name.setter
    def service_provider_display_name(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceProviderId")
    def service_provider_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_provider_id.setter
    def service_provider_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DirectLineChannelPropertiesArgsDict(TypedDict):
    direct_line_embed_code: NotRequired[pulumi.Input[_builtins.str]]
    extension_key1: NotRequired[pulumi.Input[_builtins.str]]
    extension_key2: NotRequired[pulumi.Input[_builtins.str]]
    sites: NotRequired[pulumi.Input[Sequence[pulumi.Input[DirectLineSiteArgsDict]]]]

@pulumi.input_type
class DirectLineChannelPropertiesArgs:
    def __init__(
        __self__,
        *,
        direct_line_embed_code: Optional[pulumi.Input[_builtins.str]] = ...,
        extension_key1: Optional[pulumi.Input[_builtins.str]] = ...,
        extension_key2: Optional[pulumi.Input[_builtins.str]] = ...,
        sites: Optional[pulumi.Input[Sequence[pulumi.Input[DirectLineSiteArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="directLineEmbedCode")
    def direct_line_embed_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @direct_line_embed_code.setter
    def direct_line_embed_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="extensionKey1")
    def extension_key1(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @extension_key1.setter
    def extension_key1(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="extensionKey2")
    def extension_key2(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @extension_key2.setter
    def extension_key2(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def sites(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[DirectLineSiteArgs]]]]: ...
    @sites.setter
    def sites(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[DirectLineSiteArgs]]]]
    ): ...

class DirectLineChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[DirectLineChannelPropertiesArgsDict]]

@pulumi.input_type
class DirectLineChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[DirectLineChannelPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[DirectLineChannelPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[DirectLineChannelPropertiesArgs]]
    ): ...

class DirectLineSiteArgsDict(TypedDict):
    is_enabled: pulumi.Input[_builtins.bool]
    site_name: pulumi.Input[_builtins.str]
    app_id: NotRequired[pulumi.Input[_builtins.str]]
    e_tag: NotRequired[pulumi.Input[_builtins.str]]
    is_block_user_upload_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_detailed_logging_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_endpoint_parameters_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_no_storage_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_secure_site_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_v1_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_v3_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_web_chat_speech_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_webchat_preview_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    trusted_origins: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class DirectLineSiteArgs:
    def __init__(
        __self__,
        *,
        is_enabled: pulumi.Input[_builtins.bool],
        site_name: pulumi.Input[_builtins.str],
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        e_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        is_block_user_upload_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_detailed_logging_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_endpoint_parameters_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_no_storage_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_secure_site_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_v1_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_v3_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_web_chat_speech_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_webchat_preview_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        trusted_origins: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="siteName")
    def site_name(self) -> pulumi.Input[_builtins.str]: ...
    @site_name.setter
    def site_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isBlockUserUploadEnabled")
    def is_block_user_upload_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_block_user_upload_enabled.setter
    def is_block_user_upload_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isDetailedLoggingEnabled")
    def is_detailed_logging_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_detailed_logging_enabled.setter
    def is_detailed_logging_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isEndpointParametersEnabled")
    def is_endpoint_parameters_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_endpoint_parameters_enabled.setter
    def is_endpoint_parameters_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isNoStorageEnabled")
    def is_no_storage_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_no_storage_enabled.setter
    def is_no_storage_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isSecureSiteEnabled")
    def is_secure_site_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_secure_site_enabled.setter
    def is_secure_site_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isV1Enabled")
    def is_v1_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_v1_enabled.setter
    def is_v1_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isV3Enabled")
    def is_v3_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_v3_enabled.setter
    def is_v3_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isWebChatSpeechEnabled")
    def is_web_chat_speech_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_web_chat_speech_enabled.setter
    def is_web_chat_speech_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isWebchatPreviewEnabled")
    def is_webchat_preview_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_webchat_preview_enabled.setter
    def is_webchat_preview_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trustedOrigins")
    def trusted_origins(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @trusted_origins.setter
    def trusted_origins(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DirectLineSpeechChannelPropertiesArgsDict(TypedDict):
    cognitive_service_region: NotRequired[pulumi.Input[_builtins.str]]
    cognitive_service_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    cognitive_service_subscription_key: NotRequired[pulumi.Input[_builtins.str]]
    custom_speech_model_id: NotRequired[pulumi.Input[_builtins.str]]
    custom_voice_deployment_id: NotRequired[pulumi.Input[_builtins.str]]
    is_default_bot_for_cog_svc_account: NotRequired[pulumi.Input[_builtins.bool]]
    is_enabled: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DirectLineSpeechChannelPropertiesArgs:
    def __init__(
        __self__,
        *,
        cognitive_service_region: Optional[pulumi.Input[_builtins.str]] = ...,
        cognitive_service_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cognitive_service_subscription_key: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_speech_model_id: Optional[pulumi.Input[_builtins.str]] = ...,
        custom_voice_deployment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        is_default_bot_for_cog_svc_account: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceRegion")
    def cognitive_service_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cognitive_service_region.setter
    def cognitive_service_region(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceResourceId")
    def cognitive_service_resource_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cognitive_service_resource_id.setter
    def cognitive_service_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceSubscriptionKey")
    def cognitive_service_subscription_key(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cognitive_service_subscription_key.setter
    def cognitive_service_subscription_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="customSpeechModelId")
    def custom_speech_model_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_speech_model_id.setter
    def custom_speech_model_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="customVoiceDeploymentId")
    def custom_voice_deployment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @custom_voice_deployment_id.setter
    def custom_voice_deployment_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isDefaultBotForCogSvcAccount")
    def is_default_bot_for_cog_svc_account(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_default_bot_for_cog_svc_account.setter
    def is_default_bot_for_cog_svc_account(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DirectLineSpeechChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[DirectLineSpeechChannelPropertiesArgsDict]]

@pulumi.input_type
class DirectLineSpeechChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[DirectLineSpeechChannelPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(
        self,
    ) -> Optional[pulumi.Input[DirectLineSpeechChannelPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[DirectLineSpeechChannelPropertiesArgs]]
    ): ...

class EmailChannelPropertiesArgsDict(TypedDict):
    email_address: pulumi.Input[_builtins.str]
    is_enabled: pulumi.Input[_builtins.bool]
    auth_method: NotRequired[pulumi.Input[_builtins.float]]
    magic_code: NotRequired[pulumi.Input[_builtins.str]]
    password: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class EmailChannelPropertiesArgs:
    def __init__(
        __self__,
        *,
        email_address: pulumi.Input[_builtins.str],
        is_enabled: pulumi.Input[_builtins.bool],
        auth_method: Optional[pulumi.Input[_builtins.float]] = ...,
        magic_code: Optional[pulumi.Input[_builtins.str]] = ...,
        password: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="emailAddress")
    def email_address(self) -> pulumi.Input[_builtins.str]: ...
    @email_address.setter
    def email_address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="authMethod")
    def auth_method(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @auth_method.setter
    def auth_method(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="magicCode")
    def magic_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @magic_code.setter
    def magic_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class EmailChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[EmailChannelPropertiesArgsDict]]

@pulumi.input_type
class EmailChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[EmailChannelPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[EmailChannelPropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[EmailChannelPropertiesArgs]]): ...

class FacebookChannelPropertiesArgsDict(TypedDict):
    app_id: pulumi.Input[_builtins.str]
    is_enabled: pulumi.Input[_builtins.bool]
    app_secret: NotRequired[pulumi.Input[_builtins.str]]
    pages: NotRequired[pulumi.Input[Sequence[pulumi.Input[FacebookPageArgsDict]]]]

@pulumi.input_type
class FacebookChannelPropertiesArgs:
    def __init__(
        __self__,
        *,
        app_id: pulumi.Input[_builtins.str],
        is_enabled: pulumi.Input[_builtins.bool],
        app_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        pages: Optional[pulumi.Input[Sequence[pulumi.Input[FacebookPageArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[_builtins.str]: ...
    @app_id.setter
    def app_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="appSecret")
    def app_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_secret.setter
    def app_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def pages(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[FacebookPageArgs]]]]: ...
    @pages.setter
    def pages(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[FacebookPageArgs]]]]
    ): ...

class FacebookChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[FacebookChannelPropertiesArgsDict]]

@pulumi.input_type
class FacebookChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[FacebookChannelPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[FacebookChannelPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[FacebookChannelPropertiesArgs]]
    ): ...

class FacebookPageArgsDict(TypedDict):
    id: pulumi.Input[_builtins.str]
    access_token: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FacebookPageArgs:
    def __init__(
        __self__,
        *,
        id: pulumi.Input[_builtins.str],
        access_token: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]: ...
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class KikChannelPropertiesArgsDict(TypedDict):
    is_enabled: pulumi.Input[_builtins.bool]
    user_name: pulumi.Input[_builtins.str]
    api_key: NotRequired[pulumi.Input[_builtins.str]]
    is_validated: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class KikChannelPropertiesArgs:
    def __init__(
        __self__,
        *,
        is_enabled: pulumi.Input[_builtins.bool],
        user_name: pulumi.Input[_builtins.str],
        api_key: Optional[pulumi.Input[_builtins.str]] = ...,
        is_validated: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="userName")
    def user_name(self) -> pulumi.Input[_builtins.str]: ...
    @user_name.setter
    def user_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isValidated")
    def is_validated(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_validated.setter
    def is_validated(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class KikChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[KikChannelPropertiesArgsDict]]

@pulumi.input_type
class KikChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[KikChannelPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[KikChannelPropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[KikChannelPropertiesArgs]]): ...

class LineChannelPropertiesArgsDict(TypedDict):
    line_registrations: pulumi.Input[Sequence[pulumi.Input[LineRegistrationArgsDict]]]

@pulumi.input_type
class LineChannelPropertiesArgs:
    def __init__(
        __self__,
        *,
        line_registrations: pulumi.Input[Sequence[pulumi.Input[LineRegistrationArgs]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="lineRegistrations")
    def line_registrations(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[LineRegistrationArgs]]]: ...
    @line_registrations.setter
    def line_registrations(
        self, value: pulumi.Input[Sequence[pulumi.Input[LineRegistrationArgs]]]
    ): ...

class LineChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[LineChannelPropertiesArgsDict]]

@pulumi.input_type
class LineChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[LineChannelPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[LineChannelPropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[LineChannelPropertiesArgs]]): ...

class LineRegistrationArgsDict(TypedDict):
    channel_access_token: NotRequired[pulumi.Input[_builtins.str]]
    channel_secret: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class LineRegistrationArgs:
    def __init__(
        __self__,
        *,
        channel_access_token: Optional[pulumi.Input[_builtins.str]] = ...,
        channel_secret: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelAccessToken")
    def channel_access_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @channel_access_token.setter
    def channel_access_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="channelSecret")
    def channel_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @channel_secret.setter
    def channel_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class M365ExtensionsArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class M365ExtensionsArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MsTeamsChannelPropertiesArgsDict(TypedDict):
    is_enabled: pulumi.Input[_builtins.bool]
    accepted_terms: NotRequired[pulumi.Input[_builtins.bool]]
    calling_webhook: NotRequired[pulumi.Input[_builtins.str]]
    deployment_environment: NotRequired[pulumi.Input[_builtins.str]]
    enable_calling: NotRequired[pulumi.Input[_builtins.bool]]
    incoming_call_route: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class MsTeamsChannelPropertiesArgs:
    def __init__(
        __self__,
        *,
        is_enabled: pulumi.Input[_builtins.bool],
        accepted_terms: Optional[pulumi.Input[_builtins.bool]] = ...,
        calling_webhook: Optional[pulumi.Input[_builtins.str]] = ...,
        deployment_environment: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_calling: Optional[pulumi.Input[_builtins.bool]] = ...,
        incoming_call_route: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="acceptedTerms")
    def accepted_terms(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @accepted_terms.setter
    def accepted_terms(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="callingWebhook")
    def calling_webhook(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @calling_webhook.setter
    def calling_webhook(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="deploymentEnvironment")
    def deployment_environment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deployment_environment.setter
    def deployment_environment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableCalling")
    def enable_calling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_calling.setter
    def enable_calling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="incomingCallRoute")
    def incoming_call_route(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @incoming_call_route.setter
    def incoming_call_route(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class MsTeamsChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[MsTeamsChannelPropertiesArgsDict]]

@pulumi.input_type
class MsTeamsChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[MsTeamsChannelPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[MsTeamsChannelPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[MsTeamsChannelPropertiesArgs]]
    ): ...

class OmnichannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OmnichannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class OutlookChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class OutlookChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class PrivateLinkServiceConnectionStateArgsDict(TypedDict):
    actions_required: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]

@pulumi.input_type
class PrivateLinkServiceConnectionStateArgs:
    def __init__(
        __self__,
        *,
        actions_required: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        status: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @actions_required.setter
    def actions_required(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[
        pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
    ]: ...
    @status.setter
    def status(
        self,
        value: Optional[
            pulumi.Input[Union[_builtins.str, PrivateEndpointServiceConnectionStatus]]
        ],
    ): ...

class SearchAssistantArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SearchAssistantArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SkuArgsDict(TypedDict):
    name: pulumi.Input[Union[_builtins.str, SkuName]]

@pulumi.input_type
class SkuArgs:
    def __init__(
        __self__, *, name: pulumi.Input[Union[_builtins.str, SkuName]]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[Union[_builtins.str, SkuName]]: ...
    @name.setter
    def name(self, value: pulumi.Input[Union[_builtins.str, SkuName]]): ...

class SkypeChannelPropertiesArgsDict(TypedDict):
    is_enabled: pulumi.Input[_builtins.bool]
    calling_web_hook: NotRequired[pulumi.Input[_builtins.str]]
    enable_calling: NotRequired[pulumi.Input[_builtins.bool]]
    enable_groups: NotRequired[pulumi.Input[_builtins.bool]]
    enable_media_cards: NotRequired[pulumi.Input[_builtins.bool]]
    enable_messaging: NotRequired[pulumi.Input[_builtins.bool]]
    enable_screen_sharing: NotRequired[pulumi.Input[_builtins.bool]]
    enable_video: NotRequired[pulumi.Input[_builtins.bool]]
    groups_mode: NotRequired[pulumi.Input[_builtins.str]]
    incoming_call_route: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SkypeChannelPropertiesArgs:
    def __init__(
        __self__,
        *,
        is_enabled: pulumi.Input[_builtins.bool],
        calling_web_hook: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_calling: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_groups: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_media_cards: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_messaging: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_screen_sharing: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_video: Optional[pulumi.Input[_builtins.bool]] = ...,
        groups_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        incoming_call_route: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="callingWebHook")
    def calling_web_hook(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @calling_web_hook.setter
    def calling_web_hook(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableCalling")
    def enable_calling(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_calling.setter
    def enable_calling(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableGroups")
    def enable_groups(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_groups.setter
    def enable_groups(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableMediaCards")
    def enable_media_cards(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_media_cards.setter
    def enable_media_cards(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableMessaging")
    def enable_messaging(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_messaging.setter
    def enable_messaging(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableScreenSharing")
    def enable_screen_sharing(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_screen_sharing.setter
    def enable_screen_sharing(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableVideo")
    def enable_video(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_video.setter
    def enable_video(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="groupsMode")
    def groups_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @groups_mode.setter
    def groups_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="incomingCallRoute")
    def incoming_call_route(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @incoming_call_route.setter
    def incoming_call_route(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SkypeChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[SkypeChannelPropertiesArgsDict]]

@pulumi.input_type
class SkypeChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[SkypeChannelPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[SkypeChannelPropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[SkypeChannelPropertiesArgs]]): ...

class SlackChannelPropertiesArgsDict(TypedDict):
    is_enabled: pulumi.Input[_builtins.bool]
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    landing_page_url: NotRequired[pulumi.Input[_builtins.str]]
    register_before_o_auth_flow: NotRequired[pulumi.Input[_builtins.bool]]
    scopes: NotRequired[pulumi.Input[_builtins.str]]
    signing_secret: NotRequired[pulumi.Input[_builtins.str]]
    verification_token: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SlackChannelPropertiesArgs:
    def __init__(
        __self__,
        *,
        is_enabled: pulumi.Input[_builtins.bool],
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        landing_page_url: Optional[pulumi.Input[_builtins.str]] = ...,
        register_before_o_auth_flow: Optional[pulumi.Input[_builtins.bool]] = ...,
        scopes: Optional[pulumi.Input[_builtins.str]] = ...,
        signing_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        verification_token: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[_builtins.bool]): ...
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
    @pulumi.getter(name="landingPageUrl")
    def landing_page_url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @landing_page_url.setter
    def landing_page_url(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="registerBeforeOAuthFlow")
    def register_before_o_auth_flow(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @register_before_o_auth_flow.setter
    def register_before_o_auth_flow(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="signingSecret")
    def signing_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @signing_secret.setter
    def signing_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="verificationToken")
    def verification_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @verification_token.setter
    def verification_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SlackChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[SlackChannelPropertiesArgsDict]]

@pulumi.input_type
class SlackChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[SlackChannelPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[SlackChannelPropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[SlackChannelPropertiesArgs]]): ...

class SmsChannelPropertiesArgsDict(TypedDict):
    account_sid: pulumi.Input[_builtins.str]
    is_enabled: pulumi.Input[_builtins.bool]
    phone: pulumi.Input[_builtins.str]
    auth_token: NotRequired[pulumi.Input[_builtins.str]]
    is_validated: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class SmsChannelPropertiesArgs:
    def __init__(
        __self__,
        *,
        account_sid: pulumi.Input[_builtins.str],
        is_enabled: pulumi.Input[_builtins.bool],
        phone: pulumi.Input[_builtins.str],
        auth_token: Optional[pulumi.Input[_builtins.str]] = ...,
        is_validated: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountSID")
    def account_sid(self) -> pulumi.Input[_builtins.str]: ...
    @account_sid.setter
    def account_sid(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter
    def phone(self) -> pulumi.Input[_builtins.str]: ...
    @phone.setter
    def phone(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="authToken")
    def auth_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @auth_token.setter
    def auth_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isValidated")
    def is_validated(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_validated.setter
    def is_validated(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class SmsChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[SmsChannelPropertiesArgsDict]]

@pulumi.input_type
class SmsChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[SmsChannelPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[SmsChannelPropertiesArgs]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[SmsChannelPropertiesArgs]]): ...

class TelegramChannelPropertiesArgsDict(TypedDict):
    is_enabled: pulumi.Input[_builtins.bool]
    access_token: NotRequired[pulumi.Input[_builtins.str]]
    is_validated: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class TelegramChannelPropertiesArgs:
    def __init__(
        __self__,
        *,
        is_enabled: pulumi.Input[_builtins.bool],
        access_token: Optional[pulumi.Input[_builtins.str]] = ...,
        is_validated: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isValidated")
    def is_validated(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_validated.setter
    def is_validated(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class TelegramChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[TelegramChannelPropertiesArgsDict]]

@pulumi.input_type
class TelegramChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[TelegramChannelPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[TelegramChannelPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[TelegramChannelPropertiesArgs]]
    ): ...

class TelephonyChannelPropertiesArgsDict(TypedDict):
    api_configurations: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[TelephonyChannelResourceApiConfigurationArgsDict]]
        ]
    ]
    cognitive_service_region: NotRequired[pulumi.Input[_builtins.str]]
    cognitive_service_subscription_key: NotRequired[pulumi.Input[_builtins.str]]
    default_locale: NotRequired[pulumi.Input[_builtins.str]]
    is_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    phone_numbers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[TelephonyPhoneNumbersArgsDict]]]
    ]
    premium_sku: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TelephonyChannelPropertiesArgs:
    def __init__(
        __self__,
        *,
        api_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[TelephonyChannelResourceApiConfigurationArgs]]
            ]
        ] = ...,
        cognitive_service_region: Optional[pulumi.Input[_builtins.str]] = ...,
        cognitive_service_subscription_key: Optional[pulumi.Input[_builtins.str]] = ...,
        default_locale: Optional[pulumi.Input[_builtins.str]] = ...,
        is_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        phone_numbers: Optional[
            pulumi.Input[Sequence[pulumi.Input[TelephonyPhoneNumbersArgs]]]
        ] = ...,
        premium_sku: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiConfigurations")
    def api_configurations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[TelephonyChannelResourceApiConfigurationArgs]]
        ]
    ]: ...
    @api_configurations.setter
    def api_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[TelephonyChannelResourceApiConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceRegion")
    def cognitive_service_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cognitive_service_region.setter
    def cognitive_service_region(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceSubscriptionKey")
    def cognitive_service_subscription_key(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cognitive_service_subscription_key.setter
    def cognitive_service_subscription_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultLocale")
    def default_locale(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_locale.setter
    def default_locale(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_enabled.setter
    def is_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="phoneNumbers")
    def phone_numbers(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TelephonyPhoneNumbersArgs]]]]: ...
    @phone_numbers.setter
    def phone_numbers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TelephonyPhoneNumbersArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="premiumSKU")
    def premium_sku(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @premium_sku.setter
    def premium_sku(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TelephonyChannelResourceApiConfigurationArgsDict(TypedDict):
    cognitive_service_region: NotRequired[pulumi.Input[_builtins.str]]
    cognitive_service_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    cognitive_service_subscription_key: NotRequired[pulumi.Input[_builtins.str]]
    default_locale: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    provider_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TelephonyChannelResourceApiConfigurationArgs:
    def __init__(
        __self__,
        *,
        cognitive_service_region: Optional[pulumi.Input[_builtins.str]] = ...,
        cognitive_service_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cognitive_service_subscription_key: Optional[pulumi.Input[_builtins.str]] = ...,
        default_locale: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        provider_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceRegion")
    def cognitive_service_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cognitive_service_region.setter
    def cognitive_service_region(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceResourceId")
    def cognitive_service_resource_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cognitive_service_resource_id.setter
    def cognitive_service_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceSubscriptionKey")
    def cognitive_service_subscription_key(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cognitive_service_subscription_key.setter
    def cognitive_service_subscription_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultLocale")
    def default_locale(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_locale.setter
    def default_locale(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="providerName")
    def provider_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @provider_name.setter
    def provider_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TelephonyChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[TelephonyChannelPropertiesArgsDict]]

@pulumi.input_type
class TelephonyChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[TelephonyChannelPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[TelephonyChannelPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[TelephonyChannelPropertiesArgs]]
    ): ...

class TelephonyPhoneNumbersArgsDict(TypedDict):
    acs_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    acs_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    acs_secret: NotRequired[pulumi.Input[_builtins.str]]
    cognitive_service_region: NotRequired[pulumi.Input[_builtins.str]]
    cognitive_service_resource_id: NotRequired[pulumi.Input[_builtins.str]]
    cognitive_service_subscription_key: NotRequired[pulumi.Input[_builtins.str]]
    default_locale: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    offer_type: NotRequired[pulumi.Input[_builtins.str]]
    phone_number: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TelephonyPhoneNumbersArgs:
    def __init__(
        __self__,
        *,
        acs_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
        acs_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        acs_secret: Optional[pulumi.Input[_builtins.str]] = ...,
        cognitive_service_region: Optional[pulumi.Input[_builtins.str]] = ...,
        cognitive_service_resource_id: Optional[pulumi.Input[_builtins.str]] = ...,
        cognitive_service_subscription_key: Optional[pulumi.Input[_builtins.str]] = ...,
        default_locale: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        offer_type: Optional[pulumi.Input[_builtins.str]] = ...,
        phone_number: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="acsEndpoint")
    def acs_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @acs_endpoint.setter
    def acs_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="acsResourceId")
    def acs_resource_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @acs_resource_id.setter
    def acs_resource_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="acsSecret")
    def acs_secret(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @acs_secret.setter
    def acs_secret(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceRegion")
    def cognitive_service_region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cognitive_service_region.setter
    def cognitive_service_region(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceResourceId")
    def cognitive_service_resource_id(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cognitive_service_resource_id.setter
    def cognitive_service_resource_id(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="cognitiveServiceSubscriptionKey")
    def cognitive_service_subscription_key(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cognitive_service_subscription_key.setter
    def cognitive_service_subscription_key(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultLocale")
    def default_locale(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_locale.setter
    def default_locale(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="offerType")
    def offer_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @offer_type.setter
    def offer_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @phone_number.setter
    def phone_number(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WebChatChannelPropertiesArgsDict(TypedDict):
    sites: NotRequired[pulumi.Input[Sequence[pulumi.Input[WebChatSiteArgsDict]]]]

@pulumi.input_type
class WebChatChannelPropertiesArgs:
    def __init__(
        __self__,
        *,
        sites: Optional[pulumi.Input[Sequence[pulumi.Input[WebChatSiteArgs]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def sites(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[WebChatSiteArgs]]]]: ...
    @sites.setter
    def sites(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[WebChatSiteArgs]]]]
    ): ...

class WebChatChannelArgsDict(TypedDict):
    channel_name: pulumi.Input[_builtins.str]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[WebChatChannelPropertiesArgsDict]]

@pulumi.input_type
class WebChatChannelArgs:
    def __init__(
        __self__,
        *,
        channel_name: pulumi.Input[_builtins.str],
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[WebChatChannelPropertiesArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelName")
    def channel_name(self) -> pulumi.Input[_builtins.str]: ...
    @channel_name.setter
    def channel_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[WebChatChannelPropertiesArgs]]: ...
    @properties.setter
    def properties(
        self, value: Optional[pulumi.Input[WebChatChannelPropertiesArgs]]
    ): ...

class WebChatSiteArgsDict(TypedDict):
    is_enabled: pulumi.Input[_builtins.bool]
    site_name: pulumi.Input[_builtins.str]
    app_id: NotRequired[pulumi.Input[_builtins.str]]
    e_tag: NotRequired[pulumi.Input[_builtins.str]]
    is_block_user_upload_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_detailed_logging_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_endpoint_parameters_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_no_storage_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_secure_site_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_v1_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_v3_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_web_chat_speech_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    is_webchat_preview_enabled: NotRequired[pulumi.Input[_builtins.bool]]
    tenant_id: NotRequired[pulumi.Input[_builtins.str]]
    trusted_origins: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WebChatSiteArgs:
    def __init__(
        __self__,
        *,
        is_enabled: pulumi.Input[_builtins.bool],
        site_name: pulumi.Input[_builtins.str],
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        e_tag: Optional[pulumi.Input[_builtins.str]] = ...,
        is_block_user_upload_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_detailed_logging_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_endpoint_parameters_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_no_storage_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_secure_site_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_v1_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_v3_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_web_chat_speech_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_webchat_preview_enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        tenant_id: Optional[pulumi.Input[_builtins.str]] = ...,
        trusted_origins: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> pulumi.Input[_builtins.bool]: ...
    @is_enabled.setter
    def is_enabled(self, value: pulumi.Input[_builtins.bool]): ...
    @_builtins.property
    @pulumi.getter(name="siteName")
    def site_name(self) -> pulumi.Input[_builtins.str]: ...
    @site_name.setter
    def site_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="isBlockUserUploadEnabled")
    def is_block_user_upload_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_block_user_upload_enabled.setter
    def is_block_user_upload_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isDetailedLoggingEnabled")
    def is_detailed_logging_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_detailed_logging_enabled.setter
    def is_detailed_logging_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isEndpointParametersEnabled")
    def is_endpoint_parameters_enabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_endpoint_parameters_enabled.setter
    def is_endpoint_parameters_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isNoStorageEnabled")
    def is_no_storage_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_no_storage_enabled.setter
    def is_no_storage_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isSecureSiteEnabled")
    def is_secure_site_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_secure_site_enabled.setter
    def is_secure_site_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isV1Enabled")
    def is_v1_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_v1_enabled.setter
    def is_v1_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isV3Enabled")
    def is_v3_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_v3_enabled.setter
    def is_v3_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isWebChatSpeechEnabled")
    def is_web_chat_speech_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_web_chat_speech_enabled.setter
    def is_web_chat_speech_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="isWebchatPreviewEnabled")
    def is_webchat_preview_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_webchat_preview_enabled.setter
    def is_webchat_preview_enabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trustedOrigins")
    def trusted_origins(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @trusted_origins.setter
    def trusted_origins(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
