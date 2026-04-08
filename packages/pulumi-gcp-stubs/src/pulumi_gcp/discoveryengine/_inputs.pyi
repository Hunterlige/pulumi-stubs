import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AclConfigIdpConfigArgs",
    "AclConfigIdpConfigArgsDict",
    "AclConfigIdpConfigExternalIdpConfigArgs",
    "AclConfigIdpConfigExternalIdpConfigArgsDict",
    "AssistantCustomerPolicyArgs",
    "AssistantCustomerPolicyArgsDict",
    "AssistantCustomerPolicyBannedPhraseArgs",
    "AssistantCustomerPolicyBannedPhraseArgsDict",
    "AssistantCustomerPolicyModelArmorConfigArgs",
    "AssistantCustomerPolicyModelArmorConfigArgsDict",
    "AssistantGenerationConfigArgs",
    "AssistantGenerationConfigArgsDict",
    "AssistantGenerationConfigSystemInstructionArgs",
    "AssistantGenerationConfigSystemInstructionArgsDict",
    "ChatEngineChatEngineConfigArgs",
    "ChatEngineChatEngineConfigArgsDict",
    "ChatEngineChatEngineConfigAgentCreationConfigArgs",
    ...,
    "ChatEngineChatEngineMetadataArgs",
    "ChatEngineChatEngineMetadataArgsDict",
    "ChatEngineCommonConfigArgs",
    "ChatEngineCommonConfigArgsDict",
    "CmekConfigSingleRegionKeyArgs",
    "CmekConfigSingleRegionKeyArgsDict",
    "ControlBoostActionArgs",
    "ControlBoostActionArgsDict",
    "ControlBoostActionInterpolationBoostSpecArgs",
    "ControlBoostActionInterpolationBoostSpecArgsDict",
    ...,
    ...,
    "ControlConditionArgs",
    "ControlConditionArgsDict",
    "ControlConditionActiveTimeRangeArgs",
    "ControlConditionActiveTimeRangeArgsDict",
    "ControlConditionQueryTermArgs",
    "ControlConditionQueryTermArgsDict",
    "ControlFilterActionArgs",
    "ControlFilterActionArgsDict",
    "ControlPromoteActionArgs",
    "ControlPromoteActionArgsDict",
    "ControlPromoteActionSearchLinkPromotionArgs",
    "ControlPromoteActionSearchLinkPromotionArgsDict",
    "ControlRedirectActionArgs",
    "ControlRedirectActionArgsDict",
    "ControlSynonymsActionArgs",
    "ControlSynonymsActionArgsDict",
    "DataConnectorActionConfigArgs",
    "DataConnectorActionConfigArgsDict",
    "DataConnectorBapConfigArgs",
    "DataConnectorBapConfigArgsDict",
    "DataConnectorDestinationConfigArgs",
    "DataConnectorDestinationConfigArgsDict",
    "DataConnectorDestinationConfigDestinationArgs",
    "DataConnectorDestinationConfigDestinationArgsDict",
    "DataConnectorEntityArgs",
    "DataConnectorEntityArgsDict",
    "DataConnectorErrorArgs",
    "DataConnectorErrorArgsDict",
    "DataStoreAdvancedSiteSearchConfigArgs",
    "DataStoreAdvancedSiteSearchConfigArgsDict",
    "DataStoreDocumentProcessingConfigArgs",
    "DataStoreDocumentProcessingConfigArgsDict",
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
    "LicenseConfigEndDateArgs",
    "LicenseConfigEndDateArgsDict",
    "LicenseConfigStartDateArgs",
    "LicenseConfigStartDateArgsDict",
    "RecommendationEngineCommonConfigArgs",
    "RecommendationEngineCommonConfigArgsDict",
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
    "SearchEngineCommonConfigArgs",
    "SearchEngineCommonConfigArgsDict",
    "SearchEngineKnowledgeGraphConfigArgs",
    "SearchEngineKnowledgeGraphConfigArgsDict",
    "SearchEngineKnowledgeGraphConfigFeatureConfigArgs",
    ...,
    "SearchEngineSearchEngineConfigArgs",
    "SearchEngineSearchEngineConfigArgsDict",
    "TargetSiteFailureReasonArgs",
    "TargetSiteFailureReasonArgsDict",
    "TargetSiteFailureReasonQuotaFailureArgs",
    "TargetSiteFailureReasonQuotaFailureArgsDict",
    "TargetSiteSiteVerificationInfoArgs",
    "TargetSiteSiteVerificationInfoArgsDict",
    "WidgetConfigAccessSettingsArgs",
    "WidgetConfigAccessSettingsArgsDict",
    "WidgetConfigHomepageSettingArgs",
    "WidgetConfigHomepageSettingArgsDict",
    "WidgetConfigHomepageSettingShortcutArgs",
    "WidgetConfigHomepageSettingShortcutArgsDict",
    "WidgetConfigHomepageSettingShortcutIconArgs",
    "WidgetConfigHomepageSettingShortcutIconArgsDict",
    "WidgetConfigUiBrandingArgs",
    "WidgetConfigUiBrandingArgsDict",
    "WidgetConfigUiBrandingLogoArgs",
    "WidgetConfigUiBrandingLogoArgsDict",
    "WidgetConfigUiSettingsArgs",
    "WidgetConfigUiSettingsArgsDict",
    "WidgetConfigUiSettingsDataStoreUiConfigArgs",
    "WidgetConfigUiSettingsDataStoreUiConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    "WidgetConfigUiSettingsGenerativeAnswerConfigArgs",
    ...,
]

class AclConfigIdpConfigArgsDict(TypedDict):
    external_idp_config: NotRequired[
        pulumi.Input[AclConfigIdpConfigExternalIdpConfigArgsDict]
    ]
    idp_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AclConfigIdpConfigArgs:
    def __init__(
        __self__,
        *,
        external_idp_config: Optional[
            pulumi.Input[AclConfigIdpConfigExternalIdpConfigArgs]
        ] = ...,
        idp_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="externalIdpConfig")
    def external_idp_config(
        self,
    ) -> Optional[pulumi.Input[AclConfigIdpConfigExternalIdpConfigArgs]]: ...
    @external_idp_config.setter
    def external_idp_config(
        self, value: Optional[pulumi.Input[AclConfigIdpConfigExternalIdpConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="idpType")
    def idp_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @idp_type.setter
    def idp_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AclConfigIdpConfigExternalIdpConfigArgsDict(TypedDict):
    workforce_pool_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AclConfigIdpConfigExternalIdpConfigArgs:
    def __init__(
        __self__, *, workforce_pool_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="workforcePoolName")
    def workforce_pool_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workforce_pool_name.setter
    def workforce_pool_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AssistantCustomerPolicyArgsDict(TypedDict):
    banned_phrases: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AssistantCustomerPolicyBannedPhraseArgsDict]]
        ]
    ]
    model_armor_config: NotRequired[
        pulumi.Input[AssistantCustomerPolicyModelArmorConfigArgsDict]
    ]

@pulumi.input_type
class AssistantCustomerPolicyArgs:
    def __init__(
        __self__,
        *,
        banned_phrases: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AssistantCustomerPolicyBannedPhraseArgs]]
            ]
        ] = ...,
        model_armor_config: Optional[
            pulumi.Input[AssistantCustomerPolicyModelArmorConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bannedPhrases")
    def banned_phrases(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AssistantCustomerPolicyBannedPhraseArgs]]]
    ]: ...
    @banned_phrases.setter
    def banned_phrases(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AssistantCustomerPolicyBannedPhraseArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelArmorConfig")
    def model_armor_config(
        self,
    ) -> Optional[pulumi.Input[AssistantCustomerPolicyModelArmorConfigArgs]]: ...
    @model_armor_config.setter
    def model_armor_config(
        self, value: Optional[pulumi.Input[AssistantCustomerPolicyModelArmorConfigArgs]]
    ): ...

class AssistantCustomerPolicyBannedPhraseArgsDict(TypedDict):
    phrase: pulumi.Input[_builtins.str]
    ignore_diacritics: NotRequired[pulumi.Input[_builtins.bool]]
    match_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AssistantCustomerPolicyBannedPhraseArgs:
    def __init__(
        __self__,
        *,
        phrase: pulumi.Input[_builtins.str],
        ignore_diacritics: Optional[pulumi.Input[_builtins.bool]] = ...,
        match_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def phrase(self) -> pulumi.Input[_builtins.str]: ...
    @phrase.setter
    def phrase(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreDiacritics")
    def ignore_diacritics(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_diacritics.setter
    def ignore_diacritics(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="matchType")
    def match_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @match_type.setter
    def match_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AssistantCustomerPolicyModelArmorConfigArgsDict(TypedDict):
    response_template: pulumi.Input[_builtins.str]
    user_prompt_template: pulumi.Input[_builtins.str]
    failure_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AssistantCustomerPolicyModelArmorConfigArgs:
    def __init__(
        __self__,
        *,
        response_template: pulumi.Input[_builtins.str],
        user_prompt_template: pulumi.Input[_builtins.str],
        failure_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="responseTemplate")
    def response_template(self) -> pulumi.Input[_builtins.str]: ...
    @response_template.setter
    def response_template(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="userPromptTemplate")
    def user_prompt_template(self) -> pulumi.Input[_builtins.str]: ...
    @user_prompt_template.setter
    def user_prompt_template(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="failureMode")
    def failure_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @failure_mode.setter
    def failure_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AssistantGenerationConfigArgsDict(TypedDict):
    default_language: NotRequired[pulumi.Input[_builtins.str]]
    system_instruction: NotRequired[
        pulumi.Input[AssistantGenerationConfigSystemInstructionArgsDict]
    ]

@pulumi.input_type
class AssistantGenerationConfigArgs:
    def __init__(
        __self__,
        *,
        default_language: Optional[pulumi.Input[_builtins.str]] = ...,
        system_instruction: Optional[
            pulumi.Input[AssistantGenerationConfigSystemInstructionArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultLanguage")
    def default_language(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_language.setter
    def default_language(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="systemInstruction")
    def system_instruction(
        self,
    ) -> Optional[pulumi.Input[AssistantGenerationConfigSystemInstructionArgs]]: ...
    @system_instruction.setter
    def system_instruction(
        self,
        value: Optional[pulumi.Input[AssistantGenerationConfigSystemInstructionArgs]],
    ): ...

class AssistantGenerationConfigSystemInstructionArgsDict(TypedDict):
    additional_system_instruction: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AssistantGenerationConfigSystemInstructionArgs:
    def __init__(
        __self__,
        *,
        additional_system_instruction: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalSystemInstruction")
    def additional_system_instruction(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_system_instruction.setter
    def additional_system_instruction(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ChatEngineChatEngineConfigArgsDict(TypedDict):
    agent_creation_config: NotRequired[
        pulumi.Input[ChatEngineChatEngineConfigAgentCreationConfigArgsDict]
    ]
    allow_cross_region: NotRequired[pulumi.Input[_builtins.bool]]
    dialogflow_agent_to_link: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChatEngineChatEngineConfigArgs:
    def __init__(
        __self__,
        *,
        agent_creation_config: Optional[
            pulumi.Input[ChatEngineChatEngineConfigAgentCreationConfigArgs]
        ] = ...,
        allow_cross_region: Optional[pulumi.Input[_builtins.bool]] = ...,
        dialogflow_agent_to_link: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentCreationConfig")
    def agent_creation_config(
        self,
    ) -> Optional[pulumi.Input[ChatEngineChatEngineConfigAgentCreationConfigArgs]]: ...
    @agent_creation_config.setter
    def agent_creation_config(
        self,
        value: Optional[
            pulumi.Input[ChatEngineChatEngineConfigAgentCreationConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="allowCrossRegion")
    def allow_cross_region(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_cross_region.setter
    def allow_cross_region(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="dialogflowAgentToLink")
    def dialogflow_agent_to_link(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dialogflow_agent_to_link.setter
    def dialogflow_agent_to_link(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class ChatEngineChatEngineConfigAgentCreationConfigArgsDict(TypedDict):
    default_language_code: pulumi.Input[_builtins.str]
    time_zone: pulumi.Input[_builtins.str]
    business: NotRequired[pulumi.Input[_builtins.str]]
    location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChatEngineChatEngineConfigAgentCreationConfigArgs:
    def __init__(
        __self__,
        *,
        default_language_code: pulumi.Input[_builtins.str],
        time_zone: pulumi.Input[_builtins.str],
        business: Optional[pulumi.Input[_builtins.str]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultLanguageCode")
    def default_language_code(self) -> pulumi.Input[_builtins.str]: ...
    @default_language_code.setter
    def default_language_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Input[_builtins.str]: ...
    @time_zone.setter
    def time_zone(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def business(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @business.setter
    def business(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChatEngineChatEngineMetadataArgsDict(TypedDict):
    dialogflow_agent: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChatEngineChatEngineMetadataArgs:
    def __init__(
        __self__, *, dialogflow_agent: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dialogflowAgent")
    def dialogflow_agent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dialogflow_agent.setter
    def dialogflow_agent(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ChatEngineCommonConfigArgsDict(TypedDict):
    company_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ChatEngineCommonConfigArgs:
    def __init__(
        __self__, *, company_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @company_name.setter
    def company_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class CmekConfigSingleRegionKeyArgsDict(TypedDict):
    kms_key: pulumi.Input[_builtins.str]

@pulumi.input_type
class CmekConfigSingleRegionKeyArgs:
    def __init__(__self__, *, kms_key: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Input[_builtins.str]: ...
    @kms_key.setter
    def kms_key(self, value: pulumi.Input[_builtins.str]): ...

class ControlBoostActionArgsDict(TypedDict):
    data_store: pulumi.Input[_builtins.str]
    filter: pulumi.Input[_builtins.str]
    fixed_boost: NotRequired[pulumi.Input[_builtins.float]]
    interpolation_boost_spec: NotRequired[
        pulumi.Input[ControlBoostActionInterpolationBoostSpecArgsDict]
    ]

@pulumi.input_type
class ControlBoostActionArgs:
    def __init__(
        __self__,
        *,
        data_store: pulumi.Input[_builtins.str],
        filter: pulumi.Input[_builtins.str],
        fixed_boost: Optional[pulumi.Input[_builtins.float]] = ...,
        interpolation_boost_spec: Optional[
            pulumi.Input[ControlBoostActionInterpolationBoostSpecArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> pulumi.Input[_builtins.str]: ...
    @data_store.setter
    def data_store(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]: ...
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fixedBoost")
    def fixed_boost(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @fixed_boost.setter
    def fixed_boost(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="interpolationBoostSpec")
    def interpolation_boost_spec(
        self,
    ) -> Optional[pulumi.Input[ControlBoostActionInterpolationBoostSpecArgs]]: ...
    @interpolation_boost_spec.setter
    def interpolation_boost_spec(
        self,
        value: Optional[pulumi.Input[ControlBoostActionInterpolationBoostSpecArgs]],
    ): ...

class ControlBoostActionInterpolationBoostSpecArgsDict(TypedDict):
    attribute_type: NotRequired[pulumi.Input[_builtins.str]]
    control_point: NotRequired[
        pulumi.Input[ControlBoostActionInterpolationBoostSpecControlPointArgsDict]
    ]
    field_name: NotRequired[pulumi.Input[_builtins.str]]
    interpolation_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ControlBoostActionInterpolationBoostSpecArgs:
    def __init__(
        __self__,
        *,
        attribute_type: Optional[pulumi.Input[_builtins.str]] = ...,
        control_point: Optional[
            pulumi.Input[ControlBoostActionInterpolationBoostSpecControlPointArgs]
        ] = ...,
        field_name: Optional[pulumi.Input[_builtins.str]] = ...,
        interpolation_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeType")
    def attribute_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attribute_type.setter
    def attribute_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="controlPoint")
    def control_point(
        self,
    ) -> Optional[
        pulumi.Input[ControlBoostActionInterpolationBoostSpecControlPointArgs]
    ]: ...
    @control_point.setter
    def control_point(
        self,
        value: Optional[
            pulumi.Input[ControlBoostActionInterpolationBoostSpecControlPointArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @field_name.setter
    def field_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="interpolationType")
    def interpolation_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interpolation_type.setter
    def interpolation_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ControlBoostActionInterpolationBoostSpecControlPointArgsDict(TypedDict):
    attribute_value: NotRequired[pulumi.Input[_builtins.str]]
    boost_amount: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class ControlBoostActionInterpolationBoostSpecControlPointArgs:
    def __init__(
        __self__,
        *,
        attribute_value: Optional[pulumi.Input[_builtins.str]] = ...,
        boost_amount: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @attribute_value.setter
    def attribute_value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="boostAmount")
    def boost_amount(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @boost_amount.setter
    def boost_amount(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ControlConditionArgsDict(TypedDict):
    active_time_ranges: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ControlConditionActiveTimeRangeArgsDict]]]
    ]
    query_regex: NotRequired[pulumi.Input[_builtins.str]]
    query_terms: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ControlConditionQueryTermArgsDict]]]
    ]

@pulumi.input_type
class ControlConditionArgs:
    def __init__(
        __self__,
        *,
        active_time_ranges: Optional[
            pulumi.Input[Sequence[pulumi.Input[ControlConditionActiveTimeRangeArgs]]]
        ] = ...,
        query_regex: Optional[pulumi.Input[_builtins.str]] = ...,
        query_terms: Optional[
            pulumi.Input[Sequence[pulumi.Input[ControlConditionQueryTermArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="activeTimeRanges")
    def active_time_ranges(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ControlConditionActiveTimeRangeArgs]]]
    ]: ...
    @active_time_ranges.setter
    def active_time_ranges(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ControlConditionActiveTimeRangeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="queryRegex")
    def query_regex(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @query_regex.setter
    def query_regex(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="queryTerms")
    def query_terms(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ControlConditionQueryTermArgs]]]
    ]: ...
    @query_terms.setter
    def query_terms(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ControlConditionQueryTermArgs]]]
        ],
    ): ...

class ControlConditionActiveTimeRangeArgsDict(TypedDict):
    end_time: NotRequired[pulumi.Input[_builtins.str]]
    start_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ControlConditionActiveTimeRangeArgs:
    def __init__(
        __self__,
        *,
        end_time: Optional[pulumi.Input[_builtins.str]] = ...,
        start_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endTime")
    def end_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @end_time.setter
    def end_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="startTime")
    def start_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @start_time.setter
    def start_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ControlConditionQueryTermArgsDict(TypedDict):
    full_match: NotRequired[pulumi.Input[_builtins.bool]]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ControlConditionQueryTermArgs:
    def __init__(
        __self__,
        *,
        full_match: Optional[pulumi.Input[_builtins.bool]] = ...,
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fullMatch")
    def full_match(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @full_match.setter
    def full_match(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ControlFilterActionArgsDict(TypedDict):
    data_store: pulumi.Input[_builtins.str]
    filter: pulumi.Input[_builtins.str]

@pulumi.input_type
class ControlFilterActionArgs:
    def __init__(
        __self__,
        *,
        data_store: pulumi.Input[_builtins.str],
        filter: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> pulumi.Input[_builtins.str]: ...
    @data_store.setter
    def data_store(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> pulumi.Input[_builtins.str]: ...
    @filter.setter
    def filter(self, value: pulumi.Input[_builtins.str]): ...

class ControlPromoteActionArgsDict(TypedDict):
    data_store: pulumi.Input[_builtins.str]
    search_link_promotion: pulumi.Input[ControlPromoteActionSearchLinkPromotionArgsDict]

@pulumi.input_type
class ControlPromoteActionArgs:
    def __init__(
        __self__,
        *,
        data_store: pulumi.Input[_builtins.str],
        search_link_promotion: pulumi.Input[
            ControlPromoteActionSearchLinkPromotionArgs
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> pulumi.Input[_builtins.str]: ...
    @data_store.setter
    def data_store(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="searchLinkPromotion")
    def search_link_promotion(
        self,
    ) -> pulumi.Input[ControlPromoteActionSearchLinkPromotionArgs]: ...
    @search_link_promotion.setter
    def search_link_promotion(
        self, value: pulumi.Input[ControlPromoteActionSearchLinkPromotionArgs]
    ): ...

class ControlPromoteActionSearchLinkPromotionArgsDict(TypedDict):
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    document: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    image_uri: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ControlPromoteActionSearchLinkPromotionArgs:
    def __init__(
        __self__,
        *,
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        document: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        image_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
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
    @_builtins.property
    @pulumi.getter
    def document(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @document.setter
    def document(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_uri.setter
    def image_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ControlRedirectActionArgsDict(TypedDict):
    redirect_uri: pulumi.Input[_builtins.str]

@pulumi.input_type
class ControlRedirectActionArgs:
    def __init__(__self__, *, redirect_uri: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="redirectUri")
    def redirect_uri(self) -> pulumi.Input[_builtins.str]: ...
    @redirect_uri.setter
    def redirect_uri(self, value: pulumi.Input[_builtins.str]): ...

class ControlSynonymsActionArgsDict(TypedDict):
    synonyms: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ControlSynonymsActionArgs:
    def __init__(
        __self__,
        *,
        synonyms: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def synonyms(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @synonyms.setter
    def synonyms(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DataConnectorActionConfigArgsDict(TypedDict):
    action_params: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    create_bap_connection: NotRequired[pulumi.Input[_builtins.bool]]
    is_action_configured: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DataConnectorActionConfigArgs:
    def __init__(
        __self__,
        *,
        action_params: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        create_bap_connection: Optional[pulumi.Input[_builtins.bool]] = ...,
        is_action_configured: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="actionParams")
    def action_params(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @action_params.setter
    def action_params(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createBapConnection")
    def create_bap_connection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @create_bap_connection.setter
    def create_bap_connection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="isActionConfigured")
    def is_action_configured(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @is_action_configured.setter
    def is_action_configured(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DataConnectorBapConfigArgsDict(TypedDict):
    enabled_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    supported_connector_modes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class DataConnectorBapConfigArgs:
    def __init__(
        __self__,
        *,
        enabled_actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        supported_connector_modes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enabledActions")
    def enabled_actions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enabled_actions.setter
    def enabled_actions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="supportedConnectorModes")
    def supported_connector_modes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @supported_connector_modes.setter
    def supported_connector_modes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DataConnectorDestinationConfigArgsDict(TypedDict):
    destinations: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[DataConnectorDestinationConfigDestinationArgsDict]]
        ]
    ]
    key: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataConnectorDestinationConfigArgs:
    def __init__(
        __self__,
        *,
        destinations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DataConnectorDestinationConfigDestinationArgs]]
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
            Sequence[pulumi.Input[DataConnectorDestinationConfigDestinationArgs]]
        ]
    ]: ...
    @destinations.setter
    def destinations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[DataConnectorDestinationConfigDestinationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataConnectorDestinationConfigDestinationArgsDict(TypedDict):
    host: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataConnectorDestinationConfigDestinationArgs:
    def __init__(
        __self__, *, host: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def host(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @host.setter
    def host(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataConnectorEntityArgsDict(TypedDict):
    data_store: NotRequired[pulumi.Input[_builtins.str]]
    entity_name: NotRequired[pulumi.Input[_builtins.str]]
    key_property_mappings: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    params: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataConnectorEntityArgs:
    def __init__(
        __self__,
        *,
        data_store: Optional[pulumi.Input[_builtins.str]] = ...,
        entity_name: Optional[pulumi.Input[_builtins.str]] = ...,
        key_property_mappings: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        params: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_store.setter
    def data_store(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entityName")
    def entity_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entity_name.setter
    def entity_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyPropertyMappings")
    def key_property_mappings(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @key_property_mappings.setter
    def key_property_mappings(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def params(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @params.setter
    def params(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataConnectorErrorArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class DataConnectorErrorArgs:
    def __init__(
        __self__,
        *,
        code: Optional[pulumi.Input[_builtins.int]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DataStoreAdvancedSiteSearchConfigArgsDict(TypedDict):
    disable_automatic_refresh: NotRequired[pulumi.Input[_builtins.bool]]
    disable_initial_index: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DataStoreAdvancedSiteSearchConfigArgs:
    def __init__(
        __self__,
        *,
        disable_automatic_refresh: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_initial_index: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableAutomaticRefresh")
    def disable_automatic_refresh(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_automatic_refresh.setter
    def disable_automatic_refresh(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableInitialIndex")
    def disable_initial_index(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_initial_index.setter
    def disable_initial_index(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DataStoreDocumentProcessingConfigArgsDict(TypedDict):
    chunking_config: NotRequired[
        pulumi.Input[DataStoreDocumentProcessingConfigChunkingConfigArgsDict]
    ]
    default_parsing_config: NotRequired[
        pulumi.Input[DataStoreDocumentProcessingConfigDefaultParsingConfigArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    parsing_config_overrides: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    DataStoreDocumentProcessingConfigParsingConfigOverrideArgsDict
                ]
            ]
        ]
    ]

@pulumi.input_type
class DataStoreDocumentProcessingConfigArgs:
    def __init__(
        __self__,
        *,
        chunking_config: Optional[
            pulumi.Input[DataStoreDocumentProcessingConfigChunkingConfigArgs]
        ] = ...,
        default_parsing_config: Optional[
            pulumi.Input[DataStoreDocumentProcessingConfigDefaultParsingConfigArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parsing_config_overrides: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DataStoreDocumentProcessingConfigParsingConfigOverrideArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="chunkingConfig")
    def chunking_config(
        self,
    ) -> Optional[
        pulumi.Input[DataStoreDocumentProcessingConfigChunkingConfigArgs]
    ]: ...
    @chunking_config.setter
    def chunking_config(
        self,
        value: Optional[
            pulumi.Input[DataStoreDocumentProcessingConfigChunkingConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultParsingConfig")
    def default_parsing_config(
        self,
    ) -> Optional[
        pulumi.Input[DataStoreDocumentProcessingConfigDefaultParsingConfigArgs]
    ]: ...
    @default_parsing_config.setter
    def default_parsing_config(
        self,
        value: Optional[
            pulumi.Input[DataStoreDocumentProcessingConfigDefaultParsingConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="parsingConfigOverrides")
    def parsing_config_overrides(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[DataStoreDocumentProcessingConfigParsingConfigOverrideArgs]
            ]
        ]
    ]: ...
    @parsing_config_overrides.setter
    def parsing_config_overrides(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        DataStoreDocumentProcessingConfigParsingConfigOverrideArgs
                    ]
                ]
            ]
        ],
    ): ...

class DataStoreDocumentProcessingConfigChunkingConfigArgsDict(TypedDict):
    layout_based_chunking_config: NotRequired[
        pulumi.Input[
            DataStoreDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfigArgsDict
        ]
    ]

@pulumi.input_type
class DataStoreDocumentProcessingConfigChunkingConfigArgs:
    def __init__(
        __self__,
        *,
        layout_based_chunking_config: Optional[
            pulumi.Input[
                DataStoreDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="layoutBasedChunkingConfig")
    def layout_based_chunking_config(
        self,
    ) -> Optional[
        pulumi.Input[
            DataStoreDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfigArgs
        ]
    ]: ...
    @layout_based_chunking_config.setter
    def layout_based_chunking_config(
        self,
        value: Optional[
            pulumi.Input[
                DataStoreDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfigArgs
            ]
        ],
    ): ...

class DataStoreDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfigArgsDict(
    TypedDict
):
    chunk_size: NotRequired[pulumi.Input[_builtins.int]]
    include_ancestor_headings: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DataStoreDocumentProcessingConfigChunkingConfigLayoutBasedChunkingConfigArgs:
    def __init__(
        __self__,
        *,
        chunk_size: Optional[pulumi.Input[_builtins.int]] = ...,
        include_ancestor_headings: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="chunkSize")
    def chunk_size(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @chunk_size.setter
    def chunk_size(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="includeAncestorHeadings")
    def include_ancestor_headings(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @include_ancestor_headings.setter
    def include_ancestor_headings(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class DataStoreDocumentProcessingConfigDefaultParsingConfigArgsDict(TypedDict):
    digital_parsing_config: NotRequired[
        pulumi.Input[
            DataStoreDocumentProcessingConfigDefaultParsingConfigDigitalParsingConfigArgsDict
        ]
    ]
    layout_parsing_config: NotRequired[
        pulumi.Input[
            DataStoreDocumentProcessingConfigDefaultParsingConfigLayoutParsingConfigArgsDict
        ]
    ]
    ocr_parsing_config: NotRequired[
        pulumi.Input[
            DataStoreDocumentProcessingConfigDefaultParsingConfigOcrParsingConfigArgsDict
        ]
    ]

@pulumi.input_type
class DataStoreDocumentProcessingConfigDefaultParsingConfigArgs:
    def __init__(
        __self__,
        *,
        digital_parsing_config: Optional[
            pulumi.Input[
                DataStoreDocumentProcessingConfigDefaultParsingConfigDigitalParsingConfigArgs
            ]
        ] = ...,
        layout_parsing_config: Optional[
            pulumi.Input[
                DataStoreDocumentProcessingConfigDefaultParsingConfigLayoutParsingConfigArgs
            ]
        ] = ...,
        ocr_parsing_config: Optional[
            pulumi.Input[
                DataStoreDocumentProcessingConfigDefaultParsingConfigOcrParsingConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="digitalParsingConfig")
    def digital_parsing_config(
        self,
    ) -> Optional[
        pulumi.Input[
            DataStoreDocumentProcessingConfigDefaultParsingConfigDigitalParsingConfigArgs
        ]
    ]: ...
    @digital_parsing_config.setter
    def digital_parsing_config(
        self,
        value: Optional[
            pulumi.Input[
                DataStoreDocumentProcessingConfigDefaultParsingConfigDigitalParsingConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="layoutParsingConfig")
    def layout_parsing_config(
        self,
    ) -> Optional[
        pulumi.Input[
            DataStoreDocumentProcessingConfigDefaultParsingConfigLayoutParsingConfigArgs
        ]
    ]: ...
    @layout_parsing_config.setter
    def layout_parsing_config(
        self,
        value: Optional[
            pulumi.Input[
                DataStoreDocumentProcessingConfigDefaultParsingConfigLayoutParsingConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ocrParsingConfig")
    def ocr_parsing_config(
        self,
    ) -> Optional[
        pulumi.Input[
            DataStoreDocumentProcessingConfigDefaultParsingConfigOcrParsingConfigArgs
        ]
    ]: ...
    @ocr_parsing_config.setter
    def ocr_parsing_config(
        self,
        value: Optional[
            pulumi.Input[
                DataStoreDocumentProcessingConfigDefaultParsingConfigOcrParsingConfigArgs
            ]
        ],
    ): ...

class DataStoreDocumentProcessingConfigDefaultParsingConfigDigitalParsingConfigArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DataStoreDocumentProcessingConfigDefaultParsingConfigDigitalParsingConfigArgs:
    def __init__(__self__) -> None: ...

class DataStoreDocumentProcessingConfigDefaultParsingConfigLayoutParsingConfigArgsDict(
    TypedDict
):
    enable_image_annotation: NotRequired[pulumi.Input[_builtins.bool]]
    enable_table_annotation: NotRequired[pulumi.Input[_builtins.bool]]
    exclude_html_classes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    exclude_html_elements: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    exclude_html_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    structured_content_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class DataStoreDocumentProcessingConfigDefaultParsingConfigLayoutParsingConfigArgs:
    def __init__(
        __self__,
        *,
        enable_image_annotation: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_table_annotation: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclude_html_classes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        exclude_html_elements: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        exclude_html_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        structured_content_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableImageAnnotation")
    def enable_image_annotation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_image_annotation.setter
    def enable_image_annotation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableTableAnnotation")
    def enable_table_annotation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_table_annotation.setter
    def enable_table_annotation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeHtmlClasses")
    def exclude_html_classes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_html_classes.setter
    def exclude_html_classes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeHtmlElements")
    def exclude_html_elements(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_html_elements.setter
    def exclude_html_elements(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeHtmlIds")
    def exclude_html_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_html_ids.setter
    def exclude_html_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="structuredContentTypes")
    def structured_content_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @structured_content_types.setter
    def structured_content_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DataStoreDocumentProcessingConfigDefaultParsingConfigOcrParsingConfigArgsDict(
    TypedDict
):
    use_native_text: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DataStoreDocumentProcessingConfigDefaultParsingConfigOcrParsingConfigArgs:
    def __init__(
        __self__, *, use_native_text: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="useNativeText")
    def use_native_text(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_native_text.setter
    def use_native_text(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class DataStoreDocumentProcessingConfigParsingConfigOverrideArgsDict(TypedDict):
    file_type: pulumi.Input[_builtins.str]
    digital_parsing_config: NotRequired[
        pulumi.Input[
            DataStoreDocumentProcessingConfigParsingConfigOverrideDigitalParsingConfigArgsDict
        ]
    ]
    layout_parsing_config: NotRequired[
        pulumi.Input[
            DataStoreDocumentProcessingConfigParsingConfigOverrideLayoutParsingConfigArgsDict
        ]
    ]
    ocr_parsing_config: NotRequired[
        pulumi.Input[
            DataStoreDocumentProcessingConfigParsingConfigOverrideOcrParsingConfigArgsDict
        ]
    ]

@pulumi.input_type
class DataStoreDocumentProcessingConfigParsingConfigOverrideArgs:
    def __init__(
        __self__,
        *,
        file_type: pulumi.Input[_builtins.str],
        digital_parsing_config: Optional[
            pulumi.Input[
                DataStoreDocumentProcessingConfigParsingConfigOverrideDigitalParsingConfigArgs
            ]
        ] = ...,
        layout_parsing_config: Optional[
            pulumi.Input[
                DataStoreDocumentProcessingConfigParsingConfigOverrideLayoutParsingConfigArgs
            ]
        ] = ...,
        ocr_parsing_config: Optional[
            pulumi.Input[
                DataStoreDocumentProcessingConfigParsingConfigOverrideOcrParsingConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fileType")
    def file_type(self) -> pulumi.Input[_builtins.str]: ...
    @file_type.setter
    def file_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="digitalParsingConfig")
    def digital_parsing_config(
        self,
    ) -> Optional[
        pulumi.Input[
            DataStoreDocumentProcessingConfigParsingConfigOverrideDigitalParsingConfigArgs
        ]
    ]: ...
    @digital_parsing_config.setter
    def digital_parsing_config(
        self,
        value: Optional[
            pulumi.Input[
                DataStoreDocumentProcessingConfigParsingConfigOverrideDigitalParsingConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="layoutParsingConfig")
    def layout_parsing_config(
        self,
    ) -> Optional[
        pulumi.Input[
            DataStoreDocumentProcessingConfigParsingConfigOverrideLayoutParsingConfigArgs
        ]
    ]: ...
    @layout_parsing_config.setter
    def layout_parsing_config(
        self,
        value: Optional[
            pulumi.Input[
                DataStoreDocumentProcessingConfigParsingConfigOverrideLayoutParsingConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ocrParsingConfig")
    def ocr_parsing_config(
        self,
    ) -> Optional[
        pulumi.Input[
            DataStoreDocumentProcessingConfigParsingConfigOverrideOcrParsingConfigArgs
        ]
    ]: ...
    @ocr_parsing_config.setter
    def ocr_parsing_config(
        self,
        value: Optional[
            pulumi.Input[
                DataStoreDocumentProcessingConfigParsingConfigOverrideOcrParsingConfigArgs
            ]
        ],
    ): ...

class DataStoreDocumentProcessingConfigParsingConfigOverrideDigitalParsingConfigArgsDict(
    TypedDict
): ...

@pulumi.input_type
class DataStoreDocumentProcessingConfigParsingConfigOverrideDigitalParsingConfigArgs:
    def __init__(__self__) -> None: ...

class DataStoreDocumentProcessingConfigParsingConfigOverrideLayoutParsingConfigArgsDict(
    TypedDict
):
    enable_image_annotation: NotRequired[pulumi.Input[_builtins.bool]]
    enable_table_annotation: NotRequired[pulumi.Input[_builtins.bool]]
    exclude_html_classes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    exclude_html_elements: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    exclude_html_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    structured_content_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]

@pulumi.input_type
class DataStoreDocumentProcessingConfigParsingConfigOverrideLayoutParsingConfigArgs:
    def __init__(
        __self__,
        *,
        enable_image_annotation: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_table_annotation: Optional[pulumi.Input[_builtins.bool]] = ...,
        exclude_html_classes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        exclude_html_elements: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        exclude_html_ids: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        structured_content_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableImageAnnotation")
    def enable_image_annotation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_image_annotation.setter
    def enable_image_annotation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableTableAnnotation")
    def enable_table_annotation(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_table_annotation.setter
    def enable_table_annotation(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeHtmlClasses")
    def exclude_html_classes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_html_classes.setter
    def exclude_html_classes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeHtmlElements")
    def exclude_html_elements(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_html_elements.setter
    def exclude_html_elements(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="excludeHtmlIds")
    def exclude_html_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_html_ids.setter
    def exclude_html_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="structuredContentTypes")
    def structured_content_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @structured_content_types.setter
    def structured_content_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class DataStoreDocumentProcessingConfigParsingConfigOverrideOcrParsingConfigArgsDict(
    TypedDict
):
    use_native_text: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class DataStoreDocumentProcessingConfigParsingConfigOverrideOcrParsingConfigArgs:
    def __init__(
        __self__, *, use_native_text: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="useNativeText")
    def use_native_text(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_native_text.setter
    def use_native_text(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class LicenseConfigEndDateArgsDict(TypedDict):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class LicenseConfigEndDateArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class LicenseConfigStartDateArgsDict(TypedDict):
    day: NotRequired[pulumi.Input[_builtins.int]]
    month: NotRequired[pulumi.Input[_builtins.int]]
    year: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class LicenseConfigStartDateArgs:
    def __init__(
        __self__,
        *,
        day: Optional[pulumi.Input[_builtins.int]] = ...,
        month: Optional[pulumi.Input[_builtins.int]] = ...,
        year: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def day(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @day.setter
    def day(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def month(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @month.setter
    def month(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def year(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @year.setter
    def year(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RecommendationEngineCommonConfigArgsDict(TypedDict):
    company_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RecommendationEngineCommonConfigArgs:
    def __init__(
        __self__, *, company_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @company_name.setter
    def company_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RecommendationEngineMediaRecommendationEngineConfigArgsDict(TypedDict):
    engine_features_config: NotRequired[
        pulumi.Input[
            RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigArgsDict
        ]
    ]
    optimization_objective: NotRequired[pulumi.Input[_builtins.str]]
    optimization_objective_config: NotRequired[
        pulumi.Input[
            RecommendationEngineMediaRecommendationEngineConfigOptimizationObjectiveConfigArgsDict
        ]
    ]
    training_state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RecommendationEngineMediaRecommendationEngineConfigArgs:
    def __init__(
        __self__,
        *,
        engine_features_config: Optional[
            pulumi.Input[
                RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigArgs
            ]
        ] = ...,
        optimization_objective: Optional[pulumi.Input[_builtins.str]] = ...,
        optimization_objective_config: Optional[
            pulumi.Input[
                RecommendationEngineMediaRecommendationEngineConfigOptimizationObjectiveConfigArgs
            ]
        ] = ...,
        training_state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="engineFeaturesConfig")
    def engine_features_config(
        self,
    ) -> Optional[
        pulumi.Input[
            RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigArgs
        ]
    ]: ...
    @engine_features_config.setter
    def engine_features_config(
        self,
        value: Optional[
            pulumi.Input[
                RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="optimizationObjective")
    def optimization_objective(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @optimization_objective.setter
    def optimization_objective(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="optimizationObjectiveConfig")
    def optimization_objective_config(
        self,
    ) -> Optional[
        pulumi.Input[
            RecommendationEngineMediaRecommendationEngineConfigOptimizationObjectiveConfigArgs
        ]
    ]: ...
    @optimization_objective_config.setter
    def optimization_objective_config(
        self,
        value: Optional[
            pulumi.Input[
                RecommendationEngineMediaRecommendationEngineConfigOptimizationObjectiveConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="trainingState")
    def training_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @training_state.setter
    def training_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigArgsDict(
    TypedDict
):
    most_popular_config: NotRequired[
        pulumi.Input[
            RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigMostPopularConfigArgsDict
        ]
    ]
    recommended_for_you_config: NotRequired[
        pulumi.Input[
            RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigRecommendedForYouConfigArgsDict
        ]
    ]

@pulumi.input_type
class RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigArgs:
    def __init__(
        __self__,
        *,
        most_popular_config: Optional[
            pulumi.Input[
                RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigMostPopularConfigArgs
            ]
        ] = ...,
        recommended_for_you_config: Optional[
            pulumi.Input[
                RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigRecommendedForYouConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mostPopularConfig")
    def most_popular_config(
        self,
    ) -> Optional[
        pulumi.Input[
            RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigMostPopularConfigArgs
        ]
    ]: ...
    @most_popular_config.setter
    def most_popular_config(
        self,
        value: Optional[
            pulumi.Input[
                RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigMostPopularConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="recommendedForYouConfig")
    def recommended_for_you_config(
        self,
    ) -> Optional[
        pulumi.Input[
            RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigRecommendedForYouConfigArgs
        ]
    ]: ...
    @recommended_for_you_config.setter
    def recommended_for_you_config(
        self,
        value: Optional[
            pulumi.Input[
                RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigRecommendedForYouConfigArgs
            ]
        ],
    ): ...

class RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigMostPopularConfigArgsDict(
    TypedDict
):
    time_window_days: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigMostPopularConfigArgs:
    def __init__(
        __self__, *, time_window_days: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="timeWindowDays")
    def time_window_days(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @time_window_days.setter
    def time_window_days(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigRecommendedForYouConfigArgsDict(
    TypedDict
):
    context_event_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class RecommendationEngineMediaRecommendationEngineConfigEngineFeaturesConfigRecommendedForYouConfigArgs:
    def __init__(
        __self__, *, context_event_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="contextEventType")
    def context_event_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @context_event_type.setter
    def context_event_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class RecommendationEngineMediaRecommendationEngineConfigOptimizationObjectiveConfigArgsDict(
    TypedDict
):
    target_field: NotRequired[pulumi.Input[_builtins.str]]
    target_field_value_float: NotRequired[pulumi.Input[_builtins.float]]

@pulumi.input_type
class RecommendationEngineMediaRecommendationEngineConfigOptimizationObjectiveConfigArgs:
    def __init__(
        __self__,
        *,
        target_field: Optional[pulumi.Input[_builtins.str]] = ...,
        target_field_value_float: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetField")
    def target_field(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_field.setter
    def target_field(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetFieldValueFloat")
    def target_field_value_float(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @target_field_value_float.setter
    def target_field_value_float(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

class SearchEngineCommonConfigArgsDict(TypedDict):
    company_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SearchEngineCommonConfigArgs:
    def __init__(
        __self__, *, company_name: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="companyName")
    def company_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @company_name.setter
    def company_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class SearchEngineKnowledgeGraphConfigArgsDict(TypedDict):
    cloud_knowledge_graph_types: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    enable_cloud_knowledge_graph: NotRequired[pulumi.Input[_builtins.bool]]
    enable_private_knowledge_graph: NotRequired[pulumi.Input[_builtins.bool]]
    feature_config: NotRequired[
        pulumi.Input[SearchEngineKnowledgeGraphConfigFeatureConfigArgsDict]
    ]

@pulumi.input_type
class SearchEngineKnowledgeGraphConfigArgs:
    def __init__(
        __self__,
        *,
        cloud_knowledge_graph_types: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_cloud_knowledge_graph: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_private_knowledge_graph: Optional[pulumi.Input[_builtins.bool]] = ...,
        feature_config: Optional[
            pulumi.Input[SearchEngineKnowledgeGraphConfigFeatureConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudKnowledgeGraphTypes")
    def cloud_knowledge_graph_types(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @cloud_knowledge_graph_types.setter
    def cloud_knowledge_graph_types(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableCloudKnowledgeGraph")
    def enable_cloud_knowledge_graph(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_cloud_knowledge_graph.setter
    def enable_cloud_knowledge_graph(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enablePrivateKnowledgeGraph")
    def enable_private_knowledge_graph(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_private_knowledge_graph.setter
    def enable_private_knowledge_graph(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="featureConfig")
    def feature_config(
        self,
    ) -> Optional[pulumi.Input[SearchEngineKnowledgeGraphConfigFeatureConfigArgs]]: ...
    @feature_config.setter
    def feature_config(
        self,
        value: Optional[
            pulumi.Input[SearchEngineKnowledgeGraphConfigFeatureConfigArgs]
        ],
    ): ...

class SearchEngineKnowledgeGraphConfigFeatureConfigArgsDict(TypedDict):
    disable_private_kg_auto_complete: NotRequired[pulumi.Input[_builtins.bool]]
    disable_private_kg_enrichment: NotRequired[pulumi.Input[_builtins.bool]]
    disable_private_kg_query_ui_chips: NotRequired[pulumi.Input[_builtins.bool]]
    disable_private_kg_query_understanding: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class SearchEngineKnowledgeGraphConfigFeatureConfigArgs:
    def __init__(
        __self__,
        *,
        disable_private_kg_auto_complete: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_private_kg_enrichment: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_private_kg_query_ui_chips: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_private_kg_query_understanding: Optional[
            pulumi.Input[_builtins.bool]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disablePrivateKgAutoComplete")
    def disable_private_kg_auto_complete(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_private_kg_auto_complete.setter
    def disable_private_kg_auto_complete(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disablePrivateKgEnrichment")
    def disable_private_kg_enrichment(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_private_kg_enrichment.setter
    def disable_private_kg_enrichment(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disablePrivateKgQueryUiChips")
    def disable_private_kg_query_ui_chips(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_private_kg_query_ui_chips.setter
    def disable_private_kg_query_ui_chips(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disablePrivateKgQueryUnderstanding")
    def disable_private_kg_query_understanding(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_private_kg_query_understanding.setter
    def disable_private_kg_query_understanding(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class SearchEngineSearchEngineConfigArgsDict(TypedDict):
    required_subscription_tier: NotRequired[pulumi.Input[_builtins.str]]
    search_add_ons: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    search_tier: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class SearchEngineSearchEngineConfigArgs:
    def __init__(
        __self__,
        *,
        required_subscription_tier: Optional[pulumi.Input[_builtins.str]] = ...,
        search_add_ons: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        search_tier: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="requiredSubscriptionTier")
    def required_subscription_tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @required_subscription_tier.setter
    def required_subscription_tier(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="searchAddOns")
    def search_add_ons(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @search_add_ons.setter
    def search_add_ons(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="searchTier")
    def search_tier(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @search_tier.setter
    def search_tier(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class TargetSiteFailureReasonArgsDict(TypedDict):
    quota_failure: NotRequired[
        pulumi.Input[TargetSiteFailureReasonQuotaFailureArgsDict]
    ]

@pulumi.input_type
class TargetSiteFailureReasonArgs:
    def __init__(
        __self__,
        *,
        quota_failure: Optional[
            pulumi.Input[TargetSiteFailureReasonQuotaFailureArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="quotaFailure")
    def quota_failure(
        self,
    ) -> Optional[pulumi.Input[TargetSiteFailureReasonQuotaFailureArgs]]: ...
    @quota_failure.setter
    def quota_failure(
        self, value: Optional[pulumi.Input[TargetSiteFailureReasonQuotaFailureArgs]]
    ): ...

class TargetSiteFailureReasonQuotaFailureArgsDict(TypedDict):
    total_required_quota: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class TargetSiteFailureReasonQuotaFailureArgs:
    def __init__(
        __self__, *, total_required_quota: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="totalRequiredQuota")
    def total_required_quota(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @total_required_quota.setter
    def total_required_quota(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class TargetSiteSiteVerificationInfoArgsDict(TypedDict):
    site_verification_state: NotRequired[pulumi.Input[_builtins.str]]
    verify_time: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class TargetSiteSiteVerificationInfoArgs:
    def __init__(
        __self__,
        *,
        site_verification_state: Optional[pulumi.Input[_builtins.str]] = ...,
        verify_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="siteVerificationState")
    def site_verification_state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @site_verification_state.setter
    def site_verification_state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="verifyTime")
    def verify_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @verify_time.setter
    def verify_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WidgetConfigAccessSettingsArgsDict(TypedDict):
    allow_public_access: NotRequired[pulumi.Input[_builtins.bool]]
    allowlisted_domains: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    enable_web_app: NotRequired[pulumi.Input[_builtins.bool]]
    language_code: NotRequired[pulumi.Input[_builtins.str]]
    workforce_identity_pool_provider: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WidgetConfigAccessSettingsArgs:
    def __init__(
        __self__,
        *,
        allow_public_access: Optional[pulumi.Input[_builtins.bool]] = ...,
        allowlisted_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        enable_web_app: Optional[pulumi.Input[_builtins.bool]] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        workforce_identity_pool_provider: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPublicAccess")
    def allow_public_access(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_public_access.setter
    def allow_public_access(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="allowlistedDomains")
    def allowlisted_domains(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @allowlisted_domains.setter
    def allowlisted_domains(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableWebApp")
    def enable_web_app(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_web_app.setter
    def enable_web_app(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workforceIdentityPoolProvider")
    def workforce_identity_pool_provider(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @workforce_identity_pool_provider.setter
    def workforce_identity_pool_provider(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...

class WidgetConfigHomepageSettingArgsDict(TypedDict):
    shortcuts: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[WidgetConfigHomepageSettingShortcutArgsDict]]
        ]
    ]

@pulumi.input_type
class WidgetConfigHomepageSettingArgs:
    def __init__(
        __self__,
        *,
        shortcuts: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WidgetConfigHomepageSettingShortcutArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def shortcuts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WidgetConfigHomepageSettingShortcutArgs]]]
    ]: ...
    @shortcuts.setter
    def shortcuts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WidgetConfigHomepageSettingShortcutArgs]]
            ]
        ],
    ): ...

class WidgetConfigHomepageSettingShortcutArgsDict(TypedDict):
    destination_uri: NotRequired[pulumi.Input[_builtins.str]]
    icon: NotRequired[pulumi.Input[WidgetConfigHomepageSettingShortcutIconArgsDict]]
    title: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WidgetConfigHomepageSettingShortcutArgs:
    def __init__(
        __self__,
        *,
        destination_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        icon: Optional[pulumi.Input[WidgetConfigHomepageSettingShortcutIconArgs]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="destinationUri")
    def destination_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @destination_uri.setter
    def destination_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def icon(
        self,
    ) -> Optional[pulumi.Input[WidgetConfigHomepageSettingShortcutIconArgs]]: ...
    @icon.setter
    def icon(
        self, value: Optional[pulumi.Input[WidgetConfigHomepageSettingShortcutIconArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WidgetConfigHomepageSettingShortcutIconArgsDict(TypedDict):
    url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WidgetConfigHomepageSettingShortcutIconArgs:
    def __init__(
        __self__, *, url: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WidgetConfigUiBrandingArgsDict(TypedDict):
    logo: NotRequired[pulumi.Input[WidgetConfigUiBrandingLogoArgsDict]]

@pulumi.input_type
class WidgetConfigUiBrandingArgs:
    def __init__(
        __self__, *, logo: Optional[pulumi.Input[WidgetConfigUiBrandingLogoArgs]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def logo(self) -> Optional[pulumi.Input[WidgetConfigUiBrandingLogoArgs]]: ...
    @logo.setter
    def logo(self, value: Optional[pulumi.Input[WidgetConfigUiBrandingLogoArgs]]): ...

class WidgetConfigUiBrandingLogoArgsDict(TypedDict):
    url: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WidgetConfigUiBrandingLogoArgs:
    def __init__(
        __self__, *, url: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WidgetConfigUiSettingsArgsDict(TypedDict):
    data_store_ui_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[WidgetConfigUiSettingsDataStoreUiConfigArgsDict]]
        ]
    ]
    default_search_request_order_by: NotRequired[pulumi.Input[_builtins.str]]
    disable_user_events_collection: NotRequired[pulumi.Input[_builtins.bool]]
    enable_autocomplete: NotRequired[pulumi.Input[_builtins.bool]]
    enable_create_agent_button: NotRequired[pulumi.Input[_builtins.bool]]
    enable_people_search: NotRequired[pulumi.Input[_builtins.bool]]
    enable_quality_feedback: NotRequired[pulumi.Input[_builtins.bool]]
    enable_safe_search: NotRequired[pulumi.Input[_builtins.bool]]
    enable_search_as_you_type: NotRequired[pulumi.Input[_builtins.bool]]
    enable_visual_content_summary: NotRequired[pulumi.Input[_builtins.bool]]
    generative_answer_config: NotRequired[
        pulumi.Input[WidgetConfigUiSettingsGenerativeAnswerConfigArgsDict]
    ]
    interaction_type: NotRequired[pulumi.Input[_builtins.str]]
    result_description_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WidgetConfigUiSettingsArgs:
    def __init__(
        __self__,
        *,
        data_store_ui_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WidgetConfigUiSettingsDataStoreUiConfigArgs]]
            ]
        ] = ...,
        default_search_request_order_by: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_user_events_collection: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_autocomplete: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_create_agent_button: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_people_search: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_quality_feedback: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_safe_search: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_search_as_you_type: Optional[pulumi.Input[_builtins.bool]] = ...,
        enable_visual_content_summary: Optional[pulumi.Input[_builtins.bool]] = ...,
        generative_answer_config: Optional[
            pulumi.Input[WidgetConfigUiSettingsGenerativeAnswerConfigArgs]
        ] = ...,
        interaction_type: Optional[pulumi.Input[_builtins.str]] = ...,
        result_description_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreUiConfigs")
    def data_store_ui_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[WidgetConfigUiSettingsDataStoreUiConfigArgs]]
        ]
    ]: ...
    @data_store_ui_configs.setter
    def data_store_ui_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WidgetConfigUiSettingsDataStoreUiConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultSearchRequestOrderBy")
    def default_search_request_order_by(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_search_request_order_by.setter
    def default_search_request_order_by(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableUserEventsCollection")
    def disable_user_events_collection(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_user_events_collection.setter
    def disable_user_events_collection(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableAutocomplete")
    def enable_autocomplete(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_autocomplete.setter
    def enable_autocomplete(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableCreateAgentButton")
    def enable_create_agent_button(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_create_agent_button.setter
    def enable_create_agent_button(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enablePeopleSearch")
    def enable_people_search(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_people_search.setter
    def enable_people_search(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableQualityFeedback")
    def enable_quality_feedback(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_quality_feedback.setter
    def enable_quality_feedback(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableSafeSearch")
    def enable_safe_search(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_safe_search.setter
    def enable_safe_search(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="enableSearchAsYouType")
    def enable_search_as_you_type(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_search_as_you_type.setter
    def enable_search_as_you_type(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="enableVisualContentSummary")
    def enable_visual_content_summary(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_visual_content_summary.setter
    def enable_visual_content_summary(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="generativeAnswerConfig")
    def generative_answer_config(
        self,
    ) -> Optional[pulumi.Input[WidgetConfigUiSettingsGenerativeAnswerConfigArgs]]: ...
    @generative_answer_config.setter
    def generative_answer_config(
        self,
        value: Optional[pulumi.Input[WidgetConfigUiSettingsGenerativeAnswerConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="interactionType")
    def interaction_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @interaction_type.setter
    def interaction_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resultDescriptionType")
    def result_description_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @result_description_type.setter
    def result_description_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WidgetConfigUiSettingsDataStoreUiConfigArgsDict(TypedDict):
    facet_fields: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[WidgetConfigUiSettingsDataStoreUiConfigFacetFieldArgsDict]
            ]
        ]
    ]
    fields_ui_components_maps: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WidgetConfigUiSettingsDataStoreUiConfigFieldsUiComponentsMapArgsDict
                ]
            ]
        ]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WidgetConfigUiSettingsDataStoreUiConfigArgs:
    def __init__(
        __self__,
        *,
        facet_fields: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[WidgetConfigUiSettingsDataStoreUiConfigFacetFieldArgs]
                ]
            ]
        ] = ...,
        fields_ui_components_maps: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WidgetConfigUiSettingsDataStoreUiConfigFieldsUiComponentsMapArgs
                    ]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="facetFields")
    def facet_fields(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[WidgetConfigUiSettingsDataStoreUiConfigFacetFieldArgs]
            ]
        ]
    ]: ...
    @facet_fields.setter
    def facet_fields(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[WidgetConfigUiSettingsDataStoreUiConfigFacetFieldArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="fieldsUiComponentsMaps")
    def fields_ui_components_maps(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    WidgetConfigUiSettingsDataStoreUiConfigFieldsUiComponentsMapArgs
                ]
            ]
        ]
    ]: ...
    @fields_ui_components_maps.setter
    def fields_ui_components_maps(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        WidgetConfigUiSettingsDataStoreUiConfigFieldsUiComponentsMapArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WidgetConfigUiSettingsDataStoreUiConfigFacetFieldArgsDict(TypedDict):
    field: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WidgetConfigUiSettingsDataStoreUiConfigFacetFieldArgs:
    def __init__(
        __self__,
        *,
        field: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> pulumi.Input[_builtins.str]: ...
    @field.setter
    def field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WidgetConfigUiSettingsDataStoreUiConfigFieldsUiComponentsMapArgsDict(TypedDict):
    field: pulumi.Input[_builtins.str]
    ui_component: pulumi.Input[_builtins.str]
    device_visibilities: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    display_template: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WidgetConfigUiSettingsDataStoreUiConfigFieldsUiComponentsMapArgs:
    def __init__(
        __self__,
        *,
        field: pulumi.Input[_builtins.str],
        ui_component: pulumi.Input[_builtins.str],
        device_visibilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        display_template: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def field(self) -> pulumi.Input[_builtins.str]: ...
    @field.setter
    def field(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="uiComponent")
    def ui_component(self) -> pulumi.Input[_builtins.str]: ...
    @ui_component.setter
    def ui_component(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="deviceVisibilities")
    def device_visibilities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @device_visibilities.setter
    def device_visibilities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayTemplate")
    def display_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_template.setter
    def display_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WidgetConfigUiSettingsGenerativeAnswerConfigArgsDict(TypedDict):
    disable_related_questions: NotRequired[pulumi.Input[_builtins.bool]]
    ignore_adversarial_query: NotRequired[pulumi.Input[_builtins.bool]]
    ignore_low_relevant_content: NotRequired[pulumi.Input[_builtins.bool]]
    ignore_non_answer_seeking_query: NotRequired[pulumi.Input[_builtins.bool]]
    image_source: NotRequired[pulumi.Input[_builtins.str]]
    language_code: NotRequired[pulumi.Input[_builtins.str]]
    max_rephrase_steps: NotRequired[pulumi.Input[_builtins.int]]
    model_prompt_preamble: NotRequired[pulumi.Input[_builtins.str]]
    model_version: NotRequired[pulumi.Input[_builtins.str]]
    result_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WidgetConfigUiSettingsGenerativeAnswerConfigArgs:
    def __init__(
        __self__,
        *,
        disable_related_questions: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_adversarial_query: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_low_relevant_content: Optional[pulumi.Input[_builtins.bool]] = ...,
        ignore_non_answer_seeking_query: Optional[pulumi.Input[_builtins.bool]] = ...,
        image_source: Optional[pulumi.Input[_builtins.str]] = ...,
        language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        max_rephrase_steps: Optional[pulumi.Input[_builtins.int]] = ...,
        model_prompt_preamble: Optional[pulumi.Input[_builtins.str]] = ...,
        model_version: Optional[pulumi.Input[_builtins.str]] = ...,
        result_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableRelatedQuestions")
    def disable_related_questions(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_related_questions.setter
    def disable_related_questions(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ignoreAdversarialQuery")
    def ignore_adversarial_query(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_adversarial_query.setter
    def ignore_adversarial_query(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ignoreLowRelevantContent")
    def ignore_low_relevant_content(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_low_relevant_content.setter
    def ignore_low_relevant_content(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ignoreNonAnswerSeekingQuery")
    def ignore_non_answer_seeking_query(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_non_answer_seeking_query.setter
    def ignore_non_answer_seeking_query(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="imageSource")
    def image_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_source.setter
    def image_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxRephraseSteps")
    def max_rephrase_steps(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_rephrase_steps.setter
    def max_rephrase_steps(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="modelPromptPreamble")
    def model_prompt_preamble(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_prompt_preamble.setter
    def model_prompt_preamble(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="modelVersion")
    def model_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model_version.setter
    def model_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="resultCount")
    def result_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @result_count.setter
    def result_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
