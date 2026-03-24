import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AclConfigIdpConfig",
    "AclConfigIdpConfigExternalIdpConfig",
    "AssistantCustomerPolicy",
    "AssistantCustomerPolicyBannedPhrase",
    "AssistantCustomerPolicyModelArmorConfig",
    "AssistantGenerationConfig",
    "AssistantGenerationConfigSystemInstruction",
    "ChatEngineChatEngineConfig",
    "ChatEngineChatEngineConfigAgentCreationConfig",
    "ChatEngineChatEngineMetadata",
    "ChatEngineCommonConfig",
    "CmekConfigSingleRegionKey",
    "ControlBoostAction",
    "ControlBoostActionInterpolationBoostSpec",
    ...,
    "ControlCondition",
    "ControlConditionActiveTimeRange",
    "ControlConditionQueryTerm",
    "ControlFilterAction",
    "ControlPromoteAction",
    "ControlPromoteActionSearchLinkPromotion",
    "ControlRedirectAction",
    "ControlSynonymsAction",
    "DataConnectorActionConfig",
    "DataConnectorBapConfig",
    "DataConnectorDestinationConfig",
    "DataConnectorDestinationConfigDestination",
    "DataConnectorEntity",
    "DataConnectorError",
    "DataStoreAdvancedSiteSearchConfig",
    "DataStoreDocumentProcessingConfig",
    "DataStoreDocumentProcessingConfigChunkingConfig",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "LicenseConfigEndDate",
    "LicenseConfigStartDate",
    "RecommendationEngineCommonConfig",
    ...,
    ...,
    ...,
    ...,
    ...,
    "SearchEngineCommonConfig",
    "SearchEngineKnowledgeGraphConfig",
    "SearchEngineKnowledgeGraphConfigFeatureConfig",
    "SearchEngineSearchEngineConfig",
    "TargetSiteFailureReason",
    "TargetSiteFailureReasonQuotaFailure",
    "TargetSiteSiteVerificationInfo",
    "WidgetConfigAccessSettings",
    "WidgetConfigHomepageSetting",
    "WidgetConfigHomepageSettingShortcut",
    "WidgetConfigHomepageSettingShortcutIcon",
    "WidgetConfigUiBranding",
    "WidgetConfigUiBrandingLogo",
    "WidgetConfigUiSettings",
    "WidgetConfigUiSettingsDataStoreUiConfig",
    "WidgetConfigUiSettingsDataStoreUiConfigFacetField",
    ...,
    "WidgetConfigUiSettingsGenerativeAnswerConfig",
]

@pulumi.output_type
class AclConfigIdpConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        external_idp_config: Optional[
            outputs.AclConfigIdpConfigExternalIdpConfig
        ] = ...,
        idp_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalIdpConfig")
    def external_idp_config(
        self,
    ) -> Optional[outputs.AclConfigIdpConfigExternalIdpConfig]: ...
    @_builtins.property
    @pulumi.getter(name="idpType")
    def idp_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AclConfigIdpConfigExternalIdpConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, workforce_pool_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workforcePoolName")
    def workforce_pool_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssistantCustomerPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        banned_phrases: Optional[
            Sequence[outputs.AssistantCustomerPolicyBannedPhrase]
        ] = ...,
        model_armor_config: Optional[
            outputs.AssistantCustomerPolicyModelArmorConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bannedPhrases")
    def banned_phrases(
        self,
    ) -> Optional[Sequence[outputs.AssistantCustomerPolicyBannedPhrase]]: ...
    @_builtins.property
    @pulumi.getter(name="modelArmorConfig")
    def model_armor_config(
        self,
    ) -> Optional[outputs.AssistantCustomerPolicyModelArmorConfig]: ...

@pulumi.output_type
class AssistantCustomerPolicyBannedPhrase(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        phrase: _builtins.str,
        ignore_diacritics: Optional[_builtins.bool] = ...,
        match_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def phrase(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ignoreDiacritics")
    def ignore_diacritics(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="matchType")
    def match_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssistantCustomerPolicyModelArmorConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        response_template: _builtins.str,
        user_prompt_template: _builtins.str,
        failure_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="responseTemplate")
    def response_template(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="userPromptTemplate")
    def user_prompt_template(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="failureMode")
    def failure_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class AssistantGenerationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_language: Optional[_builtins.str] = ...,
        system_instruction: Optional[
            outputs.AssistantGenerationConfigSystemInstruction
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultLanguage")
    def default_language(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="systemInstruction")
    def system_instruction(
        self,
    ) -> Optional[outputs.AssistantGenerationConfigSystemInstruction]: ...

@pulumi.output_type
class AssistantGenerationConfigSystemInstruction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, additional_system_instruction: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalSystemInstruction")
    def additional_system_instruction(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChatEngineChatEngineConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        agent_creation_config: Optional[
            outputs.ChatEngineChatEngineConfigAgentCreationConfig
        ] = ...,
        allow_cross_region: Optional[_builtins.bool] = ...,
        dialogflow_agent_to_link: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentCreationConfig")
    def agent_creation_config(
        self,
    ) -> Optional[outputs.ChatEngineChatEngineConfigAgentCreationConfig]: ...
    @_builtins.property
    @pulumi.getter(name="allowCrossRegion")
    def allow_cross_region(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dialogflowAgentToLink")
    def dialogflow_agent_to_link(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChatEngineChatEngineConfigAgentCreationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        default_language_code: _builtins.str,
        time_zone: _builtins.str,
        business: Optional[_builtins.str] = ...,
        location: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultLanguageCode")
    def default_language_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def business(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChatEngineChatEngineMetadata(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, dialogflow_agent: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dialogflowAgent")
    def dialogflow_agent(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ChatEngineCommonConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, company_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CmekConfigSingleRegionKey(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str: ...

@pulumi.output_type
class ControlBoostAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_store: _builtins.str,
        filter: _builtins.str,
        fixed_boost: Optional[_builtins.float] = ...,
        interpolation_boost_spec: Optional[
            outputs.ControlBoostActionInterpolationBoostSpec
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fixedBoost")
    def fixed_boost(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="interpolationBoostSpec")
    def interpolation_boost_spec(
        self,
    ) -> Optional[outputs.ControlBoostActionInterpolationBoostSpec]: ...

@pulumi.output_type
class ControlBoostActionInterpolationBoostSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        attribute_type: Optional[_builtins.str] = ...,
        control_point: Optional[
            outputs.ControlBoostActionInterpolationBoostSpecControlPoint
        ] = ...,
        field_name: Optional[_builtins.str] = ...,
        interpolation_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeType")
    def attribute_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="controlPoint")
    def control_point(
        self,
    ) -> Optional[outputs.ControlBoostActionInterpolationBoostSpecControlPoint]: ...
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="interpolationType")
    def interpolation_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ControlBoostActionInterpolationBoostSpecControlPoint(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        attribute_value: Optional[_builtins.str] = ...,
        boost_amount: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="boostAmount")
    def boost_amount(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class ControlCondition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        active_time_ranges: Optional[
            Sequence[outputs.ControlConditionActiveTimeRange]
        ] = ...,
        query_regex: Optional[_builtins.str] = ...,
        query_terms: Optional[Sequence[outputs.ControlConditionQueryTerm]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeTimeRanges")
    def active_time_ranges(
        self,
    ) -> Optional[Sequence[outputs.ControlConditionActiveTimeRange]]: ...
    @_builtins.property
    @pulumi.getter(name="queryRegex")
    def query_regex(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="queryTerms")
    def query_terms(self) -> Optional[Sequence[outputs.ControlConditionQueryTerm]]: ...

@pulumi.output_type
class ControlConditionActiveTimeRange(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_time: Optional[_builtins.str] = ...,
        start_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ControlConditionQueryTerm(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        full_match: Optional[_builtins.bool] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fullMatch")
    def full_match(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ControlFilterAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, data_store: _builtins.str, filter: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> _builtins.str: ...

@pulumi.output_type
class ControlPromoteAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_store: _builtins.str,
        search_link_promotion: outputs.ControlPromoteActionSearchLinkPromotion,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="searchLinkPromotion")
    def search_link_promotion(
        self,
    ) -> outputs.ControlPromoteActionSearchLinkPromotion: ...

@pulumi.output_type
class ControlPromoteActionSearchLinkPromotion(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        title: _builtins.str,
        description: Optional[_builtins.str] = ...,
        document: Optional[_builtins.str] = ...,
        enabled: Optional[_builtins.bool] = ...,
        image_uri: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def document(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ControlRedirectAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, redirect_uri: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> _builtins.str: ...

@pulumi.output_type
class ControlSynonymsAction(dict):
    def __init__(
        __self__, *, synonyms: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def synonyms(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DataConnectorActionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        action_params: Optional[Mapping[str, _builtins.str]] = ...,
        create_bap_connection: Optional[_builtins.bool] = ...,
        is_action_configured: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionParams")
    def action_params(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="createBapConnection")
    def create_bap_connection(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="isActionConfigured")
    def is_action_configured(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DataConnectorBapConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled_actions: Optional[Sequence[_builtins.str]] = ...,
        supported_connector_modes: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledActions")
    def enabled_actions(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="supportedConnectorModes")
    def supported_connector_modes(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DataConnectorDestinationConfig(dict):
    def __init__(
        __self__,
        *,
        destinations: Optional[
            Sequence[outputs.DataConnectorDestinationConfigDestination]
        ] = ...,
        key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def destinations(
        self,
    ) -> Optional[Sequence[outputs.DataConnectorDestinationConfigDestination]]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataConnectorDestinationConfigDestination(dict):
    def __init__(__self__, *, host: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataConnectorEntity(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_store: Optional[_builtins.str] = ...,
        entity_name: Optional[_builtins.str] = ...,
        key_property_mappings: Optional[Mapping[str, _builtins.str]] = ...,
        params: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="keyPropertyMappings")
    def key_property_mappings(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataConnectorError(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.int] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class DataStoreAdvancedSiteSearchConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_automatic_refresh: Optional[_builtins.bool] = ...,
        disable_initial_index: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableAutomaticRefresh")
    def disable_automatic_refresh(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disableInitialIndex")
    def disable_initial_index(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DataStoreDocumentProcessingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        chunking_config: Optional[
            outputs.DataStoreDocumentProcessingConfigChunkingConfig
        ] = ...,
        default_parsing_config: Optional[
            outputs.DataStoreDocumentProcessingConfigDefaultParsingConfig
        ] = ...,
        name: Optional[_builtins.str] = ...,
        parsing_config_overrides: Optional[
            Sequence[outputs.DataStoreDocumentProcessingConfigParsingConfigOverride]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="chunkingConfig")
    def chunking_config(
        self,
    ) -> Optional[outputs.DataStoreDocumentProcessingConfigChunkingConfig]: ...
    @_builtins.property
    @pulumi.getter(name="defaultParsingConfig")
    def default_parsing_config(
        self,
    ) -> Optional[outputs.DataStoreDocumentProcessingConfigDefaultParsingConfig]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parsingConfigOverrides")
    def parsing_config_overrides(
        self,
    ) -> Optional[
        Sequence[outputs.DataStoreDocumentProcessingConfigParsingConfigOverride]
    ]: ...

@pulumi.output_type
class DataStoreDocumentProcessingConfigChunkingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        layout_based_chunking_config: Optional[
            outputs.DataStoreDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="layoutBasedChunkingConfig")
    def layout_based_chunking_config(
        self,
    ) -> Optional[
        outputs.DataStoreDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig
    ]: ...

@pulumi.output_type
class DataStoreDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        chunk_size: Optional[_builtins.int] = ...,
        include_ancestor_headings: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="chunkSize")
    def chunk_size(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="includeAncestorHeadings")
    def include_ancestor_headings(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DataStoreDocumentProcessingConfigDefaultParsingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        digital_parsing_config: Optional[
            outputs.DataStoreDocumentProcessingConfigDefaultParsingConfigDigitalParsingConfig
        ] = ...,
        layout_parsing_config: Optional[
            outputs.DataStoreDocumentProcessingConfigDefaultParsingConfigLayoutParsingConfig
        ] = ...,
        ocr_parsing_config: Optional[
            outputs.DataStoreDocumentProcessingConfigDefaultParsingConfigOcrParsingConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="digitalParsingConfig")
    def digital_parsing_config(
        self,
    ) -> Optional[
        outputs.DataStoreDocumentProcessingConfigDefaultParsingConfigDigitalParsingConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="layoutParsingConfig")
    def layout_parsing_config(
        self,
    ) -> Optional[
        outputs.DataStoreDocumentProcessingConfigDefaultParsingConfigLayoutParsingConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ocrParsingConfig")
    def ocr_parsing_config(
        self,
    ) -> Optional[
        outputs.DataStoreDocumentProcessingConfigDefaultParsingConfigOcrParsingConfig
    ]: ...

@pulumi.output_type
class DataStoreDocumentProcessingConfigDefaultParsingConfigDigitalParsingConfig(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DataStoreDocumentProcessingConfigDefaultParsingConfigLayoutParsingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_image_annotation: Optional[_builtins.bool] = ...,
        enable_table_annotation: Optional[_builtins.bool] = ...,
        exclude_html_classes: Optional[Sequence[_builtins.str]] = ...,
        exclude_html_elements: Optional[Sequence[_builtins.str]] = ...,
        exclude_html_ids: Optional[Sequence[_builtins.str]] = ...,
        structured_content_types: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableImageAnnotation")
    def enable_image_annotation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableTableAnnotation")
    def enable_table_annotation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="excludeHtmlClasses")
    def exclude_html_classes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludeHtmlElements")
    def exclude_html_elements(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludeHtmlIds")
    def exclude_html_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="structuredContentTypes")
    def structured_content_types(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DataStoreDocumentProcessingConfigDefaultParsingConfigOcrParsingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, use_native_text: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="useNativeText")
    def use_native_text(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class DataStoreDocumentProcessingConfigParsingConfigOverride(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        file_type: _builtins.str,
        digital_parsing_config: Optional[
            outputs.DataStoreDocumentProcessingConfigParsingConfigOverrideDigitalParsingConfig
        ] = ...,
        layout_parsing_config: Optional[
            outputs.DataStoreDocumentProcessingConfigParsingConfigOverrideLayoutParsingConfig
        ] = ...,
        ocr_parsing_config: Optional[
            outputs.DataStoreDocumentProcessingConfigParsingConfigOverrideOcrParsingConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileType")
    def file_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="digitalParsingConfig")
    def digital_parsing_config(
        self,
    ) -> Optional[
        outputs.DataStoreDocumentProcessingConfigParsingConfigOverrideDigitalParsingConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="layoutParsingConfig")
    def layout_parsing_config(
        self,
    ) -> Optional[
        outputs.DataStoreDocumentProcessingConfigParsingConfigOverrideLayoutParsingConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="ocrParsingConfig")
    def ocr_parsing_config(
        self,
    ) -> Optional[
        outputs.DataStoreDocumentProcessingConfigParsingConfigOverrideOcrParsingConfig
    ]: ...

@pulumi.output_type
class DataStoreDocumentProcessingConfigParsingConfigOverrideDigitalParsingConfig(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class DataStoreDocumentProcessingConfigParsingConfigOverrideLayoutParsingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_image_annotation: Optional[_builtins.bool] = ...,
        enable_table_annotation: Optional[_builtins.bool] = ...,
        exclude_html_classes: Optional[Sequence[_builtins.str]] = ...,
        exclude_html_elements: Optional[Sequence[_builtins.str]] = ...,
        exclude_html_ids: Optional[Sequence[_builtins.str]] = ...,
        structured_content_types: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableImageAnnotation")
    def enable_image_annotation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableTableAnnotation")
    def enable_table_annotation(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="excludeHtmlClasses")
    def exclude_html_classes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludeHtmlElements")
    def exclude_html_elements(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="excludeHtmlIds")
    def exclude_html_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="structuredContentTypes")
    def structured_content_types(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class DataStoreDocumentProcessingConfigParsingConfigOverrideOcrParsingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, use_native_text: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="useNativeText")
    def use_native_text(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class LicenseConfigEndDate(dict):
    def __init__(
        __self__,
        *,
        day: Optional[_builtins.int] = ...,
        month: Optional[_builtins.int] = ...,
        year: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class LicenseConfigStartDate(dict):
    def __init__(
        __self__,
        *,
        day: Optional[_builtins.int] = ...,
        month: Optional[_builtins.int] = ...,
        year: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class RecommendationEngineCommonConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, company_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RecommendationEngineMediaRecommendationEngineConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        engine_features_config: Optional[
            outputs.RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfig
        ] = ...,
        optimization_objective: Optional[_builtins.str] = ...,
        optimization_objective_config: Optional[
            outputs.RecommendationEngineMediaRecommendationEngineConfigOptimizationObjectiveConfig
        ] = ...,
        training_state: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="engineFeaturesConfig")
    def engine_features_config(
        self,
    ) -> Optional[
        outputs.RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="optimizationObjective")
    def optimization_objective(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="optimizationObjectiveConfig")
    def optimization_objective_config(
        self,
    ) -> Optional[
        outputs.RecommendationEngineMediaRecommendationEngineConfigOptimizationObjectiveConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="trainingState")
    def training_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        most_popular_config: Optional[
            outputs.RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigMostPopularConfig
        ] = ...,
        recommended_for_you_config: Optional[
            outputs.RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigRecommendedForYouConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mostPopularConfig")
    def most_popular_config(
        self,
    ) -> Optional[
        outputs.RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigMostPopularConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="recommendedForYouConfig")
    def recommended_for_you_config(
        self,
    ) -> Optional[
        outputs.RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigRecommendedForYouConfig
    ]: ...

@pulumi.output_type
class RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigMostPopularConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, time_window_days: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="timeWindowDays")
    def time_window_days(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigRecommendedForYouConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, context_event_type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contextEventType")
    def context_event_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class RecommendationEngineMediaRecommendationEngineConfigOptimizationObjectiveConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_field: Optional[_builtins.str] = ...,
        target_field_value_float: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetField")
    def target_field(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetFieldValueFloat")
    def target_field_value_float(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class SearchEngineCommonConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, company_name: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class SearchEngineKnowledgeGraphConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        cloud_knowledge_graph_types: Optional[Sequence[_builtins.str]] = ...,
        enable_cloud_knowledge_graph: Optional[_builtins.bool] = ...,
        enable_private_knowledge_graph: Optional[_builtins.bool] = ...,
        feature_config: Optional[
            outputs.SearchEngineKnowledgeGraphConfigFeatureConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudKnowledgeGraphTypes")
    def cloud_knowledge_graph_types(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableCloudKnowledgeGraph")
    def enable_cloud_knowledge_graph(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateKnowledgeGraph")
    def enable_private_knowledge_graph(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="featureConfig")
    def feature_config(
        self,
    ) -> Optional[outputs.SearchEngineKnowledgeGraphConfigFeatureConfig]: ...

@pulumi.output_type
class SearchEngineKnowledgeGraphConfigFeatureConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_private_kg_auto_complete: Optional[_builtins.bool] = ...,
        disable_private_kg_enrichment: Optional[_builtins.bool] = ...,
        disable_private_kg_query_ui_chips: Optional[_builtins.bool] = ...,
        disable_private_kg_query_understanding: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disablePrivateKgAutoComplete")
    def disable_private_kg_auto_complete(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disablePrivateKgEnrichment")
    def disable_private_kg_enrichment(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disablePrivateKgQueryUiChips")
    def disable_private_kg_query_ui_chips(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="disablePrivateKgQueryUnderstanding")
    def disable_private_kg_query_understanding(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class SearchEngineSearchEngineConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        required_subscription_tier: Optional[_builtins.str] = ...,
        search_add_ons: Optional[Sequence[_builtins.str]] = ...,
        search_tier: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requiredSubscriptionTier")
    def required_subscription_tier(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="searchAddOns")
    def search_add_ons(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="searchTier")
    def search_tier(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class TargetSiteFailureReason(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        quota_failure: Optional[outputs.TargetSiteFailureReasonQuotaFailure] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="quotaFailure")
    def quota_failure(
        self,
    ) -> Optional[outputs.TargetSiteFailureReasonQuotaFailure]: ...

@pulumi.output_type
class TargetSiteFailureReasonQuotaFailure(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, total_required_quota: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="totalRequiredQuota")
    def total_required_quota(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class TargetSiteSiteVerificationInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        site_verification_state: Optional[_builtins.str] = ...,
        verify_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="siteVerificationState")
    def site_verification_state(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="verifyTime")
    def verify_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WidgetConfigAccessSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_public_access: Optional[_builtins.bool] = ...,
        allowlisted_domains: Optional[Sequence[_builtins.str]] = ...,
        enable_web_app: Optional[_builtins.bool] = ...,
        language_code: Optional[_builtins.str] = ...,
        workforce_identity_pool_provider: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPublicAccess")
    def allow_public_access(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="allowlistedDomains")
    def allowlisted_domains(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableWebApp")
    def enable_web_app(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="workforceIdentityPoolProvider")
    def workforce_identity_pool_provider(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WidgetConfigHomepageSetting(dict):
    def __init__(
        __self__,
        *,
        shortcuts: Optional[
            Sequence[outputs.WidgetConfigHomepageSettingShortcut]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def shortcuts(
        self,
    ) -> Optional[Sequence[outputs.WidgetConfigHomepageSettingShortcut]]: ...

@pulumi.output_type
class WidgetConfigHomepageSettingShortcut(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        destination_uri: Optional[_builtins.str] = ...,
        icon: Optional[outputs.WidgetConfigHomepageSettingShortcutIcon] = ...,
        title: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationUri")
    def destination_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def icon(self) -> Optional[outputs.WidgetConfigHomepageSettingShortcutIcon]: ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WidgetConfigHomepageSettingShortcutIcon(dict):
    def __init__(__self__, *, url: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WidgetConfigUiBranding(dict):
    def __init__(
        __self__, *, logo: Optional[outputs.WidgetConfigUiBrandingLogo] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def logo(self) -> Optional[outputs.WidgetConfigUiBrandingLogo]: ...

@pulumi.output_type
class WidgetConfigUiBrandingLogo(dict):
    def __init__(__self__, *, url: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WidgetConfigUiSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_store_ui_configs: Optional[
            Sequence[outputs.WidgetConfigUiSettingsDataStoreUiConfig]
        ] = ...,
        default_search_request_order_by: Optional[_builtins.str] = ...,
        disable_user_events_collection: Optional[_builtins.bool] = ...,
        enable_autocomplete: Optional[_builtins.bool] = ...,
        enable_create_agent_button: Optional[_builtins.bool] = ...,
        enable_people_search: Optional[_builtins.bool] = ...,
        enable_quality_feedback: Optional[_builtins.bool] = ...,
        enable_safe_search: Optional[_builtins.bool] = ...,
        enable_search_as_you_type: Optional[_builtins.bool] = ...,
        enable_visual_content_summary: Optional[_builtins.bool] = ...,
        generative_answer_config: Optional[
            outputs.WidgetConfigUiSettingsGenerativeAnswerConfig
        ] = ...,
        interaction_type: Optional[_builtins.str] = ...,
        result_description_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreUiConfigs")
    def data_store_ui_configs(
        self,
    ) -> Optional[Sequence[outputs.WidgetConfigUiSettingsDataStoreUiConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultSearchRequestOrderBy")
    def default_search_request_order_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableUserEventsCollection")
    def disable_user_events_collection(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableAutocomplete")
    def enable_autocomplete(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableCreateAgentButton")
    def enable_create_agent_button(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enablePeopleSearch")
    def enable_people_search(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableQualityFeedback")
    def enable_quality_feedback(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableSafeSearch")
    def enable_safe_search(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableSearchAsYouType")
    def enable_search_as_you_type(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableVisualContentSummary")
    def enable_visual_content_summary(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="generativeAnswerConfig")
    def generative_answer_config(
        self,
    ) -> Optional[outputs.WidgetConfigUiSettingsGenerativeAnswerConfig]: ...
    @_builtins.property
    @pulumi.getter(name="interactionType")
    def interaction_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resultDescriptionType")
    def result_description_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WidgetConfigUiSettingsDataStoreUiConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        facet_fields: Optional[
            Sequence[outputs.WidgetConfigUiSettingsDataStoreUiConfigFacetField]
        ] = ...,
        fields_ui_components_maps: Optional[
            Sequence[
                outputs.WidgetConfigUiSettingsDataStoreUiConfigFieldsUiComponentsMap
            ]
        ] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="facetFields")
    def facet_fields(
        self,
    ) -> Optional[
        Sequence[outputs.WidgetConfigUiSettingsDataStoreUiConfigFacetField]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="fieldsUiComponentsMaps")
    def fields_ui_components_maps(
        self,
    ) -> Optional[
        Sequence[outputs.WidgetConfigUiSettingsDataStoreUiConfigFieldsUiComponentsMap]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WidgetConfigUiSettingsDataStoreUiConfigFacetField(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, field: _builtins.str, display_name: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WidgetConfigUiSettingsDataStoreUiConfigFieldsUiComponentsMap(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        field: _builtins.str,
        ui_component: _builtins.str,
        device_visibilities: Optional[Sequence[_builtins.str]] = ...,
        display_template: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="uiComponent")
    def ui_component(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="deviceVisibilities")
    def device_visibilities(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayTemplate")
    def display_template(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class WidgetConfigUiSettingsGenerativeAnswerConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_related_questions: Optional[_builtins.bool] = ...,
        ignore_adversarial_query: Optional[_builtins.bool] = ...,
        ignore_low_relevant_content: Optional[_builtins.bool] = ...,
        ignore_non_answer_seeking_query: Optional[_builtins.bool] = ...,
        image_source: Optional[_builtins.str] = ...,
        language_code: Optional[_builtins.str] = ...,
        max_rephrase_steps: Optional[_builtins.int] = ...,
        model_prompt_preamble: Optional[_builtins.str] = ...,
        model_version: Optional[_builtins.str] = ...,
        result_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableRelatedQuestions")
    def disable_related_questions(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreAdversarialQuery")
    def ignore_adversarial_query(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreLowRelevantContent")
    def ignore_low_relevant_content(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ignoreNonAnswerSeekingQuery")
    def ignore_non_answer_seeking_query(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="imageSource")
    def image_source(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxRephraseSteps")
    def max_rephrase_steps(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="modelPromptPreamble")
    def model_prompt_preamble(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelVersion")
    def model_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="resultCount")
    def result_count(self) -> Optional[_builtins.int]: ...
