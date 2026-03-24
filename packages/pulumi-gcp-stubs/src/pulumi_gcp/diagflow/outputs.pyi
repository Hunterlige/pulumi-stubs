import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "ConversationProfileAutomatedAgentConfig",
    "ConversationProfileHumanAgentAssistantConfig",
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
    "ConversationProfileHumanAgentHandoffConfig",
    ...,
    "ConversationProfileLoggingConfig",
    ...,
    ...,
    "ConversationProfileNotificationConfig",
    "ConversationProfileSttConfig",
    "ConversationProfileTtsConfig",
    "ConversationProfileTtsConfigVoice",
    "CxAgentAdvancedSettings",
    "CxAgentAdvancedSettingsAudioExportGcsDestination",
    "CxAgentAdvancedSettingsDtmfSettings",
    "CxAgentAdvancedSettingsLoggingSettings",
    "CxAgentAdvancedSettingsSpeechSettings",
    "CxAgentAnswerFeedbackSettings",
    "CxAgentClientCertificateSettings",
    "CxAgentGenAppBuilderSettings",
    "CxAgentGitIntegrationSettings",
    "CxAgentGitIntegrationSettingsGithubSettings",
    "CxAgentPersonalizationSettings",
    "CxAgentSpeechToTextSettings",
    "CxAgentTextToSpeechSettings",
    "CxEntityTypeEntity",
    "CxEntityTypeExcludedPhrase",
    "CxEnvironmentVersionConfig",
    "CxFlowAdvancedSettings",
    "CxFlowAdvancedSettingsAudioExportGcsDestination",
    "CxFlowAdvancedSettingsDtmfSettings",
    "CxFlowAdvancedSettingsLoggingSettings",
    "CxFlowAdvancedSettingsSpeechSettings",
    "CxFlowEventHandler",
    "CxFlowEventHandlerTriggerFulfillment",
    ...,
    "CxFlowEventHandlerTriggerFulfillmentMessage",
    ...,
    ...,
    ...,
    ...,
    ...,
    "CxFlowEventHandlerTriggerFulfillmentMessageText",
    ...,
    "CxFlowKnowledgeConnectorSettings",
    ...,
    "CxFlowKnowledgeConnectorSettingsTriggerFulfillment",
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
    "CxFlowNluSettings",
    "CxFlowTransitionRoute",
    "CxFlowTransitionRouteTriggerFulfillment",
    ...,
    "CxFlowTransitionRouteTriggerFulfillmentMessage",
    ...,
    ...,
    ...,
    ...,
    ...,
    "CxFlowTransitionRouteTriggerFulfillmentMessageText",
    ...,
    "CxGenerativeSettingsFallbackSettings",
    "CxGenerativeSettingsFallbackSettingsPromptTemplate",
    "CxGenerativeSettingsGenerativeSafetySettings",
    ...,
    "CxGenerativeSettingsKnowledgeConnectorSettings",
    "CxGenerativeSettingsLlmModelSettings",
    "CxGeneratorLlmModelSettings",
    "CxGeneratorModelParameter",
    "CxGeneratorPlaceholder",
    "CxGeneratorPromptText",
    "CxIntentParameter",
    "CxIntentTrainingPhrase",
    "CxIntentTrainingPhrasePart",
    "CxPageAdvancedSettings",
    "CxPageAdvancedSettingsDtmfSettings",
    "CxPageEntryFulfillment",
    "CxPageEntryFulfillmentConditionalCase",
    "CxPageEntryFulfillmentMessage",
    "CxPageEntryFulfillmentMessageConversationSuccess",
    "CxPageEntryFulfillmentMessageLiveAgentHandoff",
    "CxPageEntryFulfillmentMessageOutputAudioText",
    "CxPageEntryFulfillmentMessagePlayAudio",
    "CxPageEntryFulfillmentMessageTelephonyTransferCall",
    "CxPageEntryFulfillmentMessageText",
    "CxPageEntryFulfillmentSetParameterAction",
    "CxPageEventHandler",
    "CxPageEventHandlerTriggerFulfillment",
    ...,
    "CxPageEventHandlerTriggerFulfillmentMessage",
    ...,
    ...,
    ...,
    ...,
    ...,
    "CxPageEventHandlerTriggerFulfillmentMessageText",
    ...,
    "CxPageForm",
    "CxPageFormParameter",
    "CxPageFormParameterAdvancedSettings",
    "CxPageFormParameterAdvancedSettingsDtmfSettings",
    "CxPageFormParameterFillBehavior",
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
    "CxPageKnowledgeConnectorSettings",
    ...,
    "CxPageKnowledgeConnectorSettingsTriggerFulfillment",
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
    "CxPageTransitionRoute",
    "CxPageTransitionRouteTriggerFulfillment",
    ...,
    "CxPageTransitionRouteTriggerFulfillmentMessage",
    ...,
    ...,
    ...,
    ...,
    ...,
    "CxPageTransitionRouteTriggerFulfillmentMessageText",
    ...,
    "CxPlaybookInstruction",
    "CxPlaybookInstructionStep",
    "CxPlaybookLlmModelSettings",
    "CxSecuritySettingsAudioExportSettings",
    "CxSecuritySettingsInsightsExportSettings",
    "CxTestCaseLastTestResult",
    "CxTestCaseLastTestResultConversationTurn",
    "CxTestCaseLastTestResultConversationTurnUserInput",
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
    "CxTestCaseTestCaseConversationTurn",
    "CxTestCaseTestCaseConversationTurnUserInput",
    "CxTestCaseTestCaseConversationTurnUserInputInput",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "CxTestCaseTestConfig",
    "CxToolConnectorSpec",
    "CxToolConnectorSpecAction",
    "CxToolConnectorSpecActionEntityOperation",
    "CxToolConnectorSpecEndUserAuthConfig",
    ...,
    ...,
    "CxToolDataStoreSpec",
    "CxToolDataStoreSpecDataStoreConnection",
    "CxToolDataStoreSpecFallbackPrompt",
    "CxToolFunctionSpec",
    "CxToolOpenApiSpec",
    "CxToolOpenApiSpecAuthentication",
    "CxToolOpenApiSpecAuthenticationApiKeyConfig",
    "CxToolOpenApiSpecAuthenticationBearerTokenConfig",
    "CxToolOpenApiSpecAuthenticationOauthConfig",
    ...,
    "CxToolOpenApiSpecServiceDirectoryConfig",
    "CxToolOpenApiSpecTlsConfig",
    "CxToolOpenApiSpecTlsConfigCaCert",
    "CxToolVersionTool",
    "CxToolVersionToolConnectorSpec",
    "CxToolVersionToolConnectorSpecAction",
    ...,
    "CxToolVersionToolConnectorSpecEndUserAuthConfig",
    ...,
    ...,
    "CxToolVersionToolDataStoreSpec",
    "CxToolVersionToolDataStoreSpecDataStoreConnection",
    "CxToolVersionToolDataStoreSpecFallbackPrompt",
    "CxToolVersionToolFunctionSpec",
    "CxToolVersionToolOpenApiSpec",
    "CxToolVersionToolOpenApiSpecAuthentication",
    ...,
    ...,
    ...,
    ...,
    "CxToolVersionToolOpenApiSpecServiceDirectoryConfig",
    "CxToolVersionToolOpenApiSpecTlsConfig",
    "CxToolVersionToolOpenApiSpecTlsConfigCaCert",
    "CxVersionNluSetting",
    "CxWebhookGenericWebService",
    "CxWebhookGenericWebServiceOauthConfig",
    ...,
    "CxWebhookGenericWebServiceServiceAccountAuthConfig",
    "CxWebhookServiceDirectory",
    "CxWebhookServiceDirectoryGenericWebService",
    ...,
    ...,
    ...,
    "EncryptionSpecEncryptionSpec",
    "EntityTypeEntity",
    "FulfillmentFeature",
    "FulfillmentGenericWebService",
    "GeneratorInferenceParameter",
    "GeneratorSummarizationContext",
    "GeneratorSummarizationContextFewShotExample",
    ...,
    ...,
    "GeneratorSummarizationContextFewShotExampleOutput",
    ...,
    ...,
    ...,
    ...,
    "GeneratorSummarizationContextSummarizationSection",
    "IntentFollowupIntentInfo",
]

@pulumi.output_type
class ConversationProfileAutomatedAgentConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, agent: _builtins.str, session_ttl: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def agent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sessionTtl")
    def session_ttl(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        end_user_suggestion_config: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfig
        ] = ...,
        human_agent_suggestion_config: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfig
        ] = ...,
        message_analysis_config: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigMessageAnalysisConfig
        ] = ...,
        notification_config: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigNotificationConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endUserSuggestionConfig")
    def end_user_suggestion_config(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="humanAgentSuggestionConfig")
    def human_agent_suggestion_config(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="messageAnalysisConfig")
    def message_analysis_config(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigMessageAnalysisConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    def notification_config(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigNotificationConfig
    ]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_high_latency_features_sync_delivery: Optional[_builtins.bool] = ...,
        feature_configs: Optional[
            Sequence[
                outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfig
            ]
        ] = ...,
        generators: Optional[Sequence[_builtins.str]] = ...,
        group_suggestion_responses: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableHighLatencyFeaturesSyncDelivery")
    def disable_high_latency_features_sync_delivery(
        self,
    ) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="featureConfigs")
    def feature_configs(
        self,
    ) -> Optional[
        Sequence[
            outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfig
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def generators(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="groupSuggestionResponses")
    def group_suggestion_responses(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conversation_model_config: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationModelConfig
        ] = ...,
        conversation_process_config: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationProcessConfig
        ] = ...,
        disable_agent_query_logging: Optional[_builtins.bool] = ...,
        enable_conversation_augmented_query: Optional[_builtins.bool] = ...,
        enable_event_based_suggestion: Optional[_builtins.bool] = ...,
        enable_query_suggestion_only: Optional[_builtins.bool] = ...,
        enable_query_suggestion_when_no_answer: Optional[_builtins.bool] = ...,
        query_config: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfig
        ] = ...,
        suggestion_feature: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionFeature
        ] = ...,
        suggestion_trigger_settings: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionTriggerSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conversationModelConfig")
    def conversation_model_config(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationModelConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="conversationProcessConfig")
    def conversation_process_config(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationProcessConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="disableAgentQueryLogging")
    def disable_agent_query_logging(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableConversationAugmentedQuery")
    def enable_conversation_augmented_query(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableEventBasedSuggestion")
    def enable_event_based_suggestion(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableQuerySuggestionOnly")
    def enable_query_suggestion_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableQuerySuggestionWhenNoAnswer")
    def enable_query_suggestion_when_no_answer(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="queryConfig")
    def query_config(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="suggestionFeature")
    def suggestion_feature(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionFeature
    ]: ...
    @_builtins.property
    @pulumi.getter(name="suggestionTriggerSettings")
    def suggestion_trigger_settings(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionTriggerSettings
    ]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationModelConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        baseline_model_version: Optional[_builtins.str] = ...,
        model: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baselineModelVersion")
    def baseline_model_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationProcessConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, recent_sentences_count: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recentSentencesCount")
    def recent_sentences_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        confidence_threshold: Optional[_builtins.float] = ...,
        context_filter_settings: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigContextFilterSettings
        ] = ...,
        dialogflow_query_source: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySource
        ] = ...,
        document_query_source: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDocumentQuerySource
        ] = ...,
        knowledge_base_query_source: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigKnowledgeBaseQuerySource
        ] = ...,
        max_results: Optional[_builtins.int] = ...,
        sections: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigSections
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="confidenceThreshold")
    def confidence_threshold(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="contextFilterSettings")
    def context_filter_settings(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigContextFilterSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dialogflowQuerySource")
    def dialogflow_query_source(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySource
    ]: ...
    @_builtins.property
    @pulumi.getter(name="documentQuerySource")
    def document_query_source(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDocumentQuerySource
    ]: ...
    @_builtins.property
    @pulumi.getter(name="knowledgeBaseQuerySource")
    def knowledge_base_query_source(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigKnowledgeBaseQuerySource
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maxResults")
    def max_results(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def sections(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigSections
    ]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigContextFilterSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        drop_handoff_messages: Optional[_builtins.bool] = ...,
        drop_ivr_messages: Optional[_builtins.bool] = ...,
        drop_virtual_agent_messages: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dropHandoffMessages")
    def drop_handoff_messages(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dropIvrMessages")
    def drop_ivr_messages(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dropVirtualAgentMessages")
    def drop_virtual_agent_messages(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        agent: _builtins.str,
        human_agent_side_config: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def agent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="humanAgentSideConfig")
    def human_agent_side_config(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfig
    ]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfig(
    dict
):
    def __init__(__self__, *, agent: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def agent(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDocumentQuerySource(
    dict
):
    def __init__(__self__, *, documents: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def documents(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigKnowledgeBaseQuerySource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, knowledge_bases: Sequence[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="knowledgeBases")
    def knowledge_bases(self) -> Sequence[_builtins.str]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigSections(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, section_types: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sectionTypes")
    def section_types(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionFeature(
    dict
):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionTriggerSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        no_small_talk: Optional[_builtins.bool] = ...,
        only_end_user: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="noSmallTalk")
    def no_small_talk(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="onlyEndUser")
    def only_end_user(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        disable_high_latency_features_sync_delivery: Optional[_builtins.bool] = ...,
        feature_configs: Optional[
            Sequence[
                outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfig
            ]
        ] = ...,
        generators: Optional[Sequence[_builtins.str]] = ...,
        group_suggestion_responses: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableHighLatencyFeaturesSyncDelivery")
    def disable_high_latency_features_sync_delivery(
        self,
    ) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="featureConfigs")
    def feature_configs(
        self,
    ) -> Optional[
        Sequence[
            outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfig
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def generators(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="groupSuggestionResponses")
    def group_suggestion_responses(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conversation_model_config: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationModelConfig
        ] = ...,
        conversation_process_config: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationProcessConfig
        ] = ...,
        disable_agent_query_logging: Optional[_builtins.bool] = ...,
        enable_conversation_augmented_query: Optional[_builtins.bool] = ...,
        enable_event_based_suggestion: Optional[_builtins.bool] = ...,
        enable_query_suggestion_only: Optional[_builtins.bool] = ...,
        enable_query_suggestion_when_no_answer: Optional[_builtins.bool] = ...,
        query_config: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfig
        ] = ...,
        suggestion_feature: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionFeature
        ] = ...,
        suggestion_trigger_settings: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionTriggerSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conversationModelConfig")
    def conversation_model_config(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationModelConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="conversationProcessConfig")
    def conversation_process_config(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationProcessConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="disableAgentQueryLogging")
    def disable_agent_query_logging(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableConversationAugmentedQuery")
    def enable_conversation_augmented_query(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableEventBasedSuggestion")
    def enable_event_based_suggestion(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableQuerySuggestionOnly")
    def enable_query_suggestion_only(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableQuerySuggestionWhenNoAnswer")
    def enable_query_suggestion_when_no_answer(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="queryConfig")
    def query_config(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="suggestionFeature")
    def suggestion_feature(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionFeature
    ]: ...
    @_builtins.property
    @pulumi.getter(name="suggestionTriggerSettings")
    def suggestion_trigger_settings(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionTriggerSettings
    ]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationModelConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        baseline_model_version: Optional[_builtins.str] = ...,
        model: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baselineModelVersion")
    def baseline_model_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationProcessConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, recent_sentences_count: Optional[_builtins.int] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="recentSentencesCount")
    def recent_sentences_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfig(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        confidence_threshold: Optional[_builtins.float] = ...,
        context_filter_settings: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigContextFilterSettings
        ] = ...,
        dialogflow_query_source: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySource
        ] = ...,
        max_results: Optional[_builtins.int] = ...,
        sections: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigSections
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="confidenceThreshold")
    def confidence_threshold(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="contextFilterSettings")
    def context_filter_settings(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigContextFilterSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="dialogflowQuerySource")
    def dialogflow_query_source(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySource
    ]: ...
    @_builtins.property
    @pulumi.getter(name="maxResults")
    def max_results(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def sections(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigSections
    ]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigContextFilterSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        drop_handoff_messages: Optional[_builtins.bool] = ...,
        drop_ivr_messages: Optional[_builtins.bool] = ...,
        drop_virtual_agent_messages: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dropHandoffMessages")
    def drop_handoff_messages(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dropIvrMessages")
    def drop_ivr_messages(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="dropVirtualAgentMessages")
    def drop_virtual_agent_messages(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySource(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        agent: _builtins.str,
        human_agent_side_config: Optional[
            outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def agent(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="humanAgentSideConfig")
    def human_agent_side_config(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfig
    ]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfig(
    dict
):
    def __init__(__self__, *, agent: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def agent(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigSections(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, section_types: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="sectionTypes")
    def section_types(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionFeature(
    dict
):
    def __init__(__self__, *, type: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionTriggerSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        no_small_talk: Optional[_builtins.bool] = ...,
        only_end_user: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="noSmallTalk")
    def no_small_talk(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="onlyEndUser")
    def only_end_user(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigMessageAnalysisConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_entity_extraction: Optional[_builtins.bool] = ...,
        enable_sentiment_analysis: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableEntityExtraction")
    def enable_entity_extraction(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableSentimentAnalysis")
    def enable_sentiment_analysis(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConversationProfileHumanAgentAssistantConfigNotificationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        message_format: Optional[_builtins.str] = ...,
        topic: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConversationProfileHumanAgentHandoffConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        live_person_config: Optional[
            outputs.ConversationProfileHumanAgentHandoffConfigLivePersonConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="livePersonConfig")
    def live_person_config(
        self,
    ) -> Optional[
        outputs.ConversationProfileHumanAgentHandoffConfigLivePersonConfig
    ]: ...

@pulumi.output_type
class ConversationProfileHumanAgentHandoffConfigLivePersonConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, account_number: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accountNumber")
    def account_number(self) -> _builtins.str: ...

@pulumi.output_type
class ConversationProfileLoggingConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, enable_stackdriver_logging: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConversationProfileNewMessageEventNotificationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        message_format: Optional[_builtins.str] = ...,
        topic: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConversationProfileNewRecognitionResultNotificationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        message_format: Optional[_builtins.str] = ...,
        topic: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConversationProfileNotificationConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        message_format: Optional[_builtins.str] = ...,
        topic: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class ConversationProfileSttConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_encoding: Optional[_builtins.str] = ...,
        enable_word_info: Optional[_builtins.bool] = ...,
        language_code: Optional[_builtins.str] = ...,
        model: Optional[_builtins.str] = ...,
        sample_rate_hertz: Optional[_builtins.int] = ...,
        speech_model_variant: Optional[_builtins.str] = ...,
        use_timeout_based_endpointing: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioEncoding")
    def audio_encoding(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableWordInfo")
    def enable_word_info(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="sampleRateHertz")
    def sample_rate_hertz(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="speechModelVariant")
    def speech_model_variant(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useTimeoutBasedEndpointing")
    def use_timeout_based_endpointing(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class ConversationProfileTtsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        effects_profile_ids: Optional[Sequence[_builtins.str]] = ...,
        pitch: Optional[_builtins.float] = ...,
        speaking_rate: Optional[_builtins.float] = ...,
        voice: Optional[outputs.ConversationProfileTtsConfigVoice] = ...,
        volume_gain_db: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="effectsProfileIds")
    def effects_profile_ids(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def pitch(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="speakingRate")
    def speaking_rate(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter
    def voice(self) -> Optional[outputs.ConversationProfileTtsConfigVoice]: ...
    @_builtins.property
    @pulumi.getter(name="volumeGainDb")
    def volume_gain_db(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class ConversationProfileTtsConfigVoice(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        name: Optional[_builtins.str] = ...,
        ssml_gender: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ssmlGender")
    def ssml_gender(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxAgentAdvancedSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_export_gcs_destination: Optional[
            outputs.CxAgentAdvancedSettingsAudioExportGcsDestination
        ] = ...,
        dtmf_settings: Optional[outputs.CxAgentAdvancedSettingsDtmfSettings] = ...,
        logging_settings: Optional[
            outputs.CxAgentAdvancedSettingsLoggingSettings
        ] = ...,
        speech_settings: Optional[outputs.CxAgentAdvancedSettingsSpeechSettings] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioExportGcsDestination")
    def audio_export_gcs_destination(
        self,
    ) -> Optional[outputs.CxAgentAdvancedSettingsAudioExportGcsDestination]: ...
    @_builtins.property
    @pulumi.getter(name="dtmfSettings")
    def dtmf_settings(
        self,
    ) -> Optional[outputs.CxAgentAdvancedSettingsDtmfSettings]: ...
    @_builtins.property
    @pulumi.getter(name="loggingSettings")
    def logging_settings(
        self,
    ) -> Optional[outputs.CxAgentAdvancedSettingsLoggingSettings]: ...
    @_builtins.property
    @pulumi.getter(name="speechSettings")
    def speech_settings(
        self,
    ) -> Optional[outputs.CxAgentAdvancedSettingsSpeechSettings]: ...

@pulumi.output_type
class CxAgentAdvancedSettingsAudioExportGcsDestination(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxAgentAdvancedSettingsDtmfSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        finish_digit: Optional[_builtins.str] = ...,
        max_digits: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxDigits")
    def max_digits(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CxAgentAdvancedSettingsLoggingSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_consent_based_redaction: Optional[_builtins.bool] = ...,
        enable_interaction_logging: Optional[_builtins.bool] = ...,
        enable_stackdriver_logging: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableConsentBasedRedaction")
    def enable_consent_based_redaction(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableInteractionLogging")
    def enable_interaction_logging(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxAgentAdvancedSettingsSpeechSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpointer_sensitivity: Optional[_builtins.int] = ...,
        models: Optional[Mapping[str, _builtins.str]] = ...,
        no_speech_timeout: Optional[_builtins.str] = ...,
        use_timeout_based_endpointing: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointerSensitivity")
    def endpointer_sensitivity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def models(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="noSpeechTimeout")
    def no_speech_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useTimeoutBasedEndpointing")
    def use_timeout_based_endpointing(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxAgentAnswerFeedbackSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, enable_answer_feedback: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableAnswerFeedback")
    def enable_answer_feedback(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxAgentClientCertificateSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        private_key: _builtins.str,
        ssl_certificate: _builtins.str,
        passphrase: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="sslCertificate")
    def ssl_certificate(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxAgentGenAppBuilderSettings(dict):
    def __init__(__self__, *, engine: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> _builtins.str: ...

@pulumi.output_type
class CxAgentGitIntegrationSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        github_settings: Optional[
            outputs.CxAgentGitIntegrationSettingsGithubSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="githubSettings")
    def github_settings(
        self,
    ) -> Optional[outputs.CxAgentGitIntegrationSettingsGithubSettings]: ...

@pulumi.output_type
class CxAgentGitIntegrationSettingsGithubSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        access_token: Optional[_builtins.str] = ...,
        branches: Optional[Sequence[_builtins.str]] = ...,
        display_name: Optional[_builtins.str] = ...,
        repository_uri: Optional[_builtins.str] = ...,
        tracking_branch: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def branches(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repositoryUri")
    def repository_uri(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trackingBranch")
    def tracking_branch(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxAgentPersonalizationSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, default_end_user_metadata: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultEndUserMetadata")
    def default_end_user_metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxAgentSpeechToTextSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, enable_speech_adaptation: Optional[_builtins.bool] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableSpeechAdaptation")
    def enable_speech_adaptation(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxAgentTextToSpeechSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, synthesize_speech_configs: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="synthesizeSpeechConfigs")
    def synthesize_speech_configs(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxEntityTypeEntity(dict):
    def __init__(
        __self__,
        *,
        synonyms: Optional[Sequence[_builtins.str]] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def synonyms(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxEntityTypeExcludedPhrase(dict):
    def __init__(__self__, *, value: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxEnvironmentVersionConfig(dict):
    def __init__(__self__, *, version: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> _builtins.str: ...

@pulumi.output_type
class CxFlowAdvancedSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_export_gcs_destination: Optional[
            outputs.CxFlowAdvancedSettingsAudioExportGcsDestination
        ] = ...,
        dtmf_settings: Optional[outputs.CxFlowAdvancedSettingsDtmfSettings] = ...,
        logging_settings: Optional[outputs.CxFlowAdvancedSettingsLoggingSettings] = ...,
        speech_settings: Optional[outputs.CxFlowAdvancedSettingsSpeechSettings] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioExportGcsDestination")
    def audio_export_gcs_destination(
        self,
    ) -> Optional[outputs.CxFlowAdvancedSettingsAudioExportGcsDestination]: ...
    @_builtins.property
    @pulumi.getter(name="dtmfSettings")
    def dtmf_settings(self) -> Optional[outputs.CxFlowAdvancedSettingsDtmfSettings]: ...
    @_builtins.property
    @pulumi.getter(name="loggingSettings")
    def logging_settings(
        self,
    ) -> Optional[outputs.CxFlowAdvancedSettingsLoggingSettings]: ...
    @_builtins.property
    @pulumi.getter(name="speechSettings")
    def speech_settings(
        self,
    ) -> Optional[outputs.CxFlowAdvancedSettingsSpeechSettings]: ...

@pulumi.output_type
class CxFlowAdvancedSettingsAudioExportGcsDestination(dict):
    def __init__(__self__, *, uri: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowAdvancedSettingsDtmfSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        finish_digit: Optional[_builtins.str] = ...,
        max_digits: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxDigits")
    def max_digits(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CxFlowAdvancedSettingsLoggingSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_consent_based_redaction: Optional[_builtins.bool] = ...,
        enable_interaction_logging: Optional[_builtins.bool] = ...,
        enable_stackdriver_logging: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableConsentBasedRedaction")
    def enable_consent_based_redaction(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableInteractionLogging")
    def enable_interaction_logging(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxFlowAdvancedSettingsSpeechSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpointer_sensitivity: Optional[_builtins.int] = ...,
        models: Optional[Mapping[str, _builtins.str]] = ...,
        no_speech_timeout: Optional[_builtins.str] = ...,
        use_timeout_based_endpointing: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointerSensitivity")
    def endpointer_sensitivity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def models(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="noSpeechTimeout")
    def no_speech_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useTimeoutBasedEndpointing")
    def use_timeout_based_endpointing(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxFlowEventHandler(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        target_flow: Optional[_builtins.str] = ...,
        target_page: Optional[_builtins.str] = ...,
        trigger_fulfillment: Optional[
            outputs.CxFlowEventHandlerTriggerFulfillment
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def event(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetFlow")
    def target_flow(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetPage")
    def target_page(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="triggerFulfillment")
    def trigger_fulfillment(
        self,
    ) -> Optional[outputs.CxFlowEventHandlerTriggerFulfillment]: ...

@pulumi.output_type
class CxFlowEventHandlerTriggerFulfillment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conditional_cases: Optional[
            Sequence[outputs.CxFlowEventHandlerTriggerFulfillmentConditionalCase]
        ] = ...,
        enable_generative_fallback: Optional[_builtins.bool] = ...,
        messages: Optional[
            Sequence[outputs.CxFlowEventHandlerTriggerFulfillmentMessage]
        ] = ...,
        return_partial_responses: Optional[_builtins.bool] = ...,
        set_parameter_actions: Optional[
            Sequence[outputs.CxFlowEventHandlerTriggerFulfillmentSetParameterAction]
        ] = ...,
        tag: Optional[_builtins.str] = ...,
        webhook: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(
        self,
    ) -> Optional[
        Sequence[outputs.CxFlowEventHandlerTriggerFulfillmentConditionalCase]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableGenerativeFallback")
    def enable_generative_fallback(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def messages(
        self,
    ) -> Optional[Sequence[outputs.CxFlowEventHandlerTriggerFulfillmentMessage]]: ...
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> Optional[
        Sequence[outputs.CxFlowEventHandlerTriggerFulfillmentSetParameterAction]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowEventHandlerTriggerFulfillmentConditionalCase(dict):
    def __init__(__self__, *, cases: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowEventHandlerTriggerFulfillmentMessage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channel: Optional[_builtins.str] = ...,
        conversation_success: Optional[
            outputs.CxFlowEventHandlerTriggerFulfillmentMessageConversationSuccess
        ] = ...,
        live_agent_handoff: Optional[
            outputs.CxFlowEventHandlerTriggerFulfillmentMessageLiveAgentHandoff
        ] = ...,
        output_audio_text: Optional[
            outputs.CxFlowEventHandlerTriggerFulfillmentMessageOutputAudioText
        ] = ...,
        payload: Optional[_builtins.str] = ...,
        play_audio: Optional[
            outputs.CxFlowEventHandlerTriggerFulfillmentMessagePlayAudio
        ] = ...,
        telephony_transfer_call: Optional[
            outputs.CxFlowEventHandlerTriggerFulfillmentMessageTelephonyTransferCall
        ] = ...,
        text: Optional[outputs.CxFlowEventHandlerTriggerFulfillmentMessageText] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(
        self,
    ) -> Optional[
        outputs.CxFlowEventHandlerTriggerFulfillmentMessageConversationSuccess
    ]: ...
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> Optional[
        outputs.CxFlowEventHandlerTriggerFulfillmentMessageLiveAgentHandoff
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(
        self,
    ) -> Optional[
        outputs.CxFlowEventHandlerTriggerFulfillmentMessageOutputAudioText
    ]: ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(
        self,
    ) -> Optional[outputs.CxFlowEventHandlerTriggerFulfillmentMessagePlayAudio]: ...
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> Optional[
        outputs.CxFlowEventHandlerTriggerFulfillmentMessageTelephonyTransferCall
    ]: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[outputs.CxFlowEventHandlerTriggerFulfillmentMessageText]: ...

@pulumi.output_type
class CxFlowEventHandlerTriggerFulfillmentMessageConversationSuccess(dict):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowEventHandlerTriggerFulfillmentMessageLiveAgentHandoff(dict):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowEventHandlerTriggerFulfillmentMessageOutputAudioText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        ssml: Optional[_builtins.str] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowEventHandlerTriggerFulfillmentMessagePlayAudio(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_uri: _builtins.str,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxFlowEventHandlerTriggerFulfillmentMessageTelephonyTransferCall(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, phone_number: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str: ...

@pulumi.output_type
class CxFlowEventHandlerTriggerFulfillmentMessageText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        texts: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CxFlowEventHandlerTriggerFulfillmentSetParameterAction(dict):
    def __init__(
        __self__,
        *,
        parameter: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_store_connections: Optional[
            Sequence[outputs.CxFlowKnowledgeConnectorSettingsDataStoreConnection]
        ] = ...,
        enabled: Optional[_builtins.bool] = ...,
        target_flow: Optional[_builtins.str] = ...,
        target_page: Optional[_builtins.str] = ...,
        trigger_fulfillment: Optional[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillment
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreConnections")
    def data_store_connections(
        self,
    ) -> Optional[
        Sequence[outputs.CxFlowKnowledgeConnectorSettingsDataStoreConnection]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="targetFlow")
    def target_flow(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetPage")
    def target_page(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="triggerFulfillment")
    def trigger_fulfillment(
        self,
    ) -> Optional[outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillment]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsDataStoreConnection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_store: Optional[_builtins.str] = ...,
        data_store_type: Optional[_builtins.str] = ...,
        document_processing_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreType")
    def data_store_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentProcessingMode")
    def document_processing_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        advanced_settings: Optional[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettings
        ] = ...,
        conditional_cases: Optional[
            Sequence[
                outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentConditionalCase
            ]
        ] = ...,
        enable_generative_fallback: Optional[_builtins.bool] = ...,
        messages: Optional[
            Sequence[outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessage]
        ] = ...,
        return_partial_responses: Optional[_builtins.bool] = ...,
        set_parameter_actions: Optional[
            Sequence[
                outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentSetParameterAction
            ]
        ] = ...,
        tag: Optional[_builtins.str] = ...,
        webhook: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(
        self,
    ) -> Optional[
        outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentConditionalCase
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableGenerativeFallback")
    def enable_generative_fallback(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def messages(
        self,
    ) -> Optional[
        Sequence[outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessage]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentSetParameterAction
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dtmf_settings: Optional[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettings
        ] = ...,
        logging_settings: Optional[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettings
        ] = ...,
        speech_settings: Optional[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dtmfSettings")
    def dtmf_settings(
        self,
    ) -> Optional[
        outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="loggingSettings")
    def logging_settings(
        self,
    ) -> Optional[
        outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="speechSettings")
    def speech_settings(
        self,
    ) -> Optional[
        outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettings
    ]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        endpointing_timeout_duration: Optional[_builtins.str] = ...,
        finish_digit: Optional[_builtins.str] = ...,
        interdigit_timeout_duration: Optional[_builtins.str] = ...,
        max_digits: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="endpointingTimeoutDuration")
    def endpointing_timeout_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="interdigitTimeoutDuration")
    def interdigit_timeout_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxDigits")
    def max_digits(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_consent_based_redaction: Optional[_builtins.bool] = ...,
        enable_interaction_logging: Optional[_builtins.bool] = ...,
        enable_stackdriver_logging: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableConsentBasedRedaction")
    def enable_consent_based_redaction(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableInteractionLogging")
    def enable_interaction_logging(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpointer_sensitivity: Optional[_builtins.int] = ...,
        models: Optional[Mapping[str, _builtins.str]] = ...,
        no_speech_timeout: Optional[_builtins.str] = ...,
        use_timeout_based_endpointing: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointerSensitivity")
    def endpointer_sensitivity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def models(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="noSpeechTimeout")
    def no_speech_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useTimeoutBasedEndpointing")
    def use_timeout_based_endpointing(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentConditionalCase(dict):
    def __init__(__self__, *, cases: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channel: Optional[_builtins.str] = ...,
        conversation_success: Optional[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccess
        ] = ...,
        end_interactions: Optional[
            Sequence[
                outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteraction
            ]
        ] = ...,
        knowledge_info_card: Optional[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCard
        ] = ...,
        live_agent_handoff: Optional[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoff
        ] = ...,
        mixed_audios: Optional[
            Sequence[
                outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudio
            ]
        ] = ...,
        output_audio_text: Optional[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioText
        ] = ...,
        payload: Optional[_builtins.str] = ...,
        play_audio: Optional[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudio
        ] = ...,
        telephony_transfer_call: Optional[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCall
        ] = ...,
        text: Optional[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageText
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(
        self,
    ) -> Optional[
        outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccess
    ]: ...
    @_builtins.property
    @pulumi.getter(name="endInteractions")
    def end_interactions(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteraction
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="knowledgeInfoCard")
    def knowledge_info_card(
        self,
    ) -> Optional[
        outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCard
    ]: ...
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> Optional[
        outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoff
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mixedAudios")
    def mixed_audios(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudio
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(
        self,
    ) -> Optional[
        outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioText
    ]: ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(
        self,
    ) -> Optional[
        outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudio
    ]: ...
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> Optional[
        outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCall
    ]: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[
        outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageText
    ]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccess(
    dict
):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteraction(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCard(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoff(dict):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudio(dict):
    def __init__(
        __self__,
        *,
        segments: Optional[
            Sequence[
                outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegment
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def segments(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegment
        ]
    ]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        audio: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def audio(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        ssml: Optional[_builtins.str] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudio(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_uri: _builtins.str,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCall(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, phone_number: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        texts: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentSetParameterAction(dict):
    def __init__(
        __self__,
        *,
        parameter: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowNluSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        classification_threshold: Optional[_builtins.float] = ...,
        model_training_mode: Optional[_builtins.str] = ...,
        model_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="classificationThreshold")
    def classification_threshold(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="modelTrainingMode")
    def model_training_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelType")
    def model_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowTransitionRoute(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        condition: Optional[_builtins.str] = ...,
        intent: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        target_flow: Optional[_builtins.str] = ...,
        target_page: Optional[_builtins.str] = ...,
        trigger_fulfillment: Optional[
            outputs.CxFlowTransitionRouteTriggerFulfillment
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetFlow")
    def target_flow(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetPage")
    def target_page(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="triggerFulfillment")
    def trigger_fulfillment(
        self,
    ) -> Optional[outputs.CxFlowTransitionRouteTriggerFulfillment]: ...

@pulumi.output_type
class CxFlowTransitionRouteTriggerFulfillment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conditional_cases: Optional[
            Sequence[outputs.CxFlowTransitionRouteTriggerFulfillmentConditionalCase]
        ] = ...,
        messages: Optional[
            Sequence[outputs.CxFlowTransitionRouteTriggerFulfillmentMessage]
        ] = ...,
        return_partial_responses: Optional[_builtins.bool] = ...,
        set_parameter_actions: Optional[
            Sequence[outputs.CxFlowTransitionRouteTriggerFulfillmentSetParameterAction]
        ] = ...,
        tag: Optional[_builtins.str] = ...,
        webhook: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(
        self,
    ) -> Optional[
        Sequence[outputs.CxFlowTransitionRouteTriggerFulfillmentConditionalCase]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def messages(
        self,
    ) -> Optional[Sequence[outputs.CxFlowTransitionRouteTriggerFulfillmentMessage]]: ...
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> Optional[
        Sequence[outputs.CxFlowTransitionRouteTriggerFulfillmentSetParameterAction]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowTransitionRouteTriggerFulfillmentConditionalCase(dict):
    def __init__(__self__, *, cases: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowTransitionRouteTriggerFulfillmentMessage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channel: Optional[_builtins.str] = ...,
        conversation_success: Optional[
            outputs.CxFlowTransitionRouteTriggerFulfillmentMessageConversationSuccess
        ] = ...,
        live_agent_handoff: Optional[
            outputs.CxFlowTransitionRouteTriggerFulfillmentMessageLiveAgentHandoff
        ] = ...,
        output_audio_text: Optional[
            outputs.CxFlowTransitionRouteTriggerFulfillmentMessageOutputAudioText
        ] = ...,
        payload: Optional[_builtins.str] = ...,
        play_audio: Optional[
            outputs.CxFlowTransitionRouteTriggerFulfillmentMessagePlayAudio
        ] = ...,
        telephony_transfer_call: Optional[
            outputs.CxFlowTransitionRouteTriggerFulfillmentMessageTelephonyTransferCall
        ] = ...,
        text: Optional[
            outputs.CxFlowTransitionRouteTriggerFulfillmentMessageText
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(
        self,
    ) -> Optional[
        outputs.CxFlowTransitionRouteTriggerFulfillmentMessageConversationSuccess
    ]: ...
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> Optional[
        outputs.CxFlowTransitionRouteTriggerFulfillmentMessageLiveAgentHandoff
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(
        self,
    ) -> Optional[
        outputs.CxFlowTransitionRouteTriggerFulfillmentMessageOutputAudioText
    ]: ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(
        self,
    ) -> Optional[outputs.CxFlowTransitionRouteTriggerFulfillmentMessagePlayAudio]: ...
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> Optional[
        outputs.CxFlowTransitionRouteTriggerFulfillmentMessageTelephonyTransferCall
    ]: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[outputs.CxFlowTransitionRouteTriggerFulfillmentMessageText]: ...

@pulumi.output_type
class CxFlowTransitionRouteTriggerFulfillmentMessageConversationSuccess(dict):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowTransitionRouteTriggerFulfillmentMessageLiveAgentHandoff(dict):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowTransitionRouteTriggerFulfillmentMessageOutputAudioText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        ssml: Optional[_builtins.str] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxFlowTransitionRouteTriggerFulfillmentMessagePlayAudio(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_uri: _builtins.str,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxFlowTransitionRouteTriggerFulfillmentMessageTelephonyTransferCall(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, phone_number: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str: ...

@pulumi.output_type
class CxFlowTransitionRouteTriggerFulfillmentMessageText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        texts: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CxFlowTransitionRouteTriggerFulfillmentSetParameterAction(dict):
    def __init__(
        __self__,
        *,
        parameter: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxGenerativeSettingsFallbackSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        prompt_templates: Optional[
            Sequence[outputs.CxGenerativeSettingsFallbackSettingsPromptTemplate]
        ] = ...,
        selected_prompt: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="promptTemplates")
    def prompt_templates(
        self,
    ) -> Optional[
        Sequence[outputs.CxGenerativeSettingsFallbackSettingsPromptTemplate]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="selectedPrompt")
    def selected_prompt(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxGenerativeSettingsFallbackSettingsPromptTemplate(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        display_name: Optional[_builtins.str] = ...,
        frozen: Optional[_builtins.bool] = ...,
        prompt_text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def frozen(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="promptText")
    def prompt_text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxGenerativeSettingsGenerativeSafetySettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        banned_phrases: Optional[
            Sequence[outputs.CxGenerativeSettingsGenerativeSafetySettingsBannedPhrase]
        ] = ...,
        default_banned_phrase_match_strategy: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bannedPhrases")
    def banned_phrases(
        self,
    ) -> Optional[
        Sequence[outputs.CxGenerativeSettingsGenerativeSafetySettingsBannedPhrase]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="defaultBannedPhraseMatchStrategy")
    def default_banned_phrase_match_strategy(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxGenerativeSettingsGenerativeSafetySettingsBannedPhrase(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, language_code: _builtins.str, text: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str: ...

@pulumi.output_type
class CxGenerativeSettingsKnowledgeConnectorSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        agent: Optional[_builtins.str] = ...,
        agent_identity: Optional[_builtins.str] = ...,
        agent_scope: Optional[_builtins.str] = ...,
        business: Optional[_builtins.str] = ...,
        business_description: Optional[_builtins.str] = ...,
        disable_data_store_fallback: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def agent(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="agentIdentity")
    def agent_identity(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="agentScope")
    def agent_scope(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def business(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="businessDescription")
    def business_description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="disableDataStoreFallback")
    def disable_data_store_fallback(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxGenerativeSettingsLlmModelSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        model: Optional[_builtins.str] = ...,
        prompt_text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="promptText")
    def prompt_text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxGeneratorLlmModelSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        model: Optional[_builtins.str] = ...,
        prompt_text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="promptText")
    def prompt_text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxGeneratorModelParameter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_decode_steps: Optional[_builtins.int] = ...,
        temperature: Optional[_builtins.float] = ...,
        top_k: Optional[_builtins.int] = ...,
        top_p: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxDecodeSteps")
    def max_decode_steps(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="topK")
    def top_k(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="topP")
    def top_p(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class CxGeneratorPlaceholder(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxGeneratorPromptText(dict):
    def __init__(__self__, *, text: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxIntentParameter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        entity_type: _builtins.str,
        id: _builtins.str,
        is_list: Optional[_builtins.bool] = ...,
        redact: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="isList")
    def is_list(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def redact(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxIntentTrainingPhrase(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        parts: Sequence[outputs.CxIntentTrainingPhrasePart],
        id: Optional[_builtins.str] = ...,
        repeat_count: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parts(self) -> Sequence[outputs.CxIntentTrainingPhrasePart]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="repeatCount")
    def repeat_count(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CxIntentTrainingPhrasePart(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, text: _builtins.str, parameter_id: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="parameterId")
    def parameter_id(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageAdvancedSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dtmf_settings: Optional[outputs.CxPageAdvancedSettingsDtmfSettings] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dtmfSettings")
    def dtmf_settings(self) -> Optional[outputs.CxPageAdvancedSettingsDtmfSettings]: ...

@pulumi.output_type
class CxPageAdvancedSettingsDtmfSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        finish_digit: Optional[_builtins.str] = ...,
        max_digits: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxDigits")
    def max_digits(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CxPageEntryFulfillment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conditional_cases: Optional[
            Sequence[outputs.CxPageEntryFulfillmentConditionalCase]
        ] = ...,
        messages: Optional[Sequence[outputs.CxPageEntryFulfillmentMessage]] = ...,
        return_partial_responses: Optional[_builtins.bool] = ...,
        set_parameter_actions: Optional[
            Sequence[outputs.CxPageEntryFulfillmentSetParameterAction]
        ] = ...,
        tag: Optional[_builtins.str] = ...,
        webhook: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(
        self,
    ) -> Optional[Sequence[outputs.CxPageEntryFulfillmentConditionalCase]]: ...
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Optional[Sequence[outputs.CxPageEntryFulfillmentMessage]]: ...
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> Optional[Sequence[outputs.CxPageEntryFulfillmentSetParameterAction]]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageEntryFulfillmentConditionalCase(dict):
    def __init__(__self__, *, cases: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageEntryFulfillmentMessage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channel: Optional[_builtins.str] = ...,
        conversation_success: Optional[
            outputs.CxPageEntryFulfillmentMessageConversationSuccess
        ] = ...,
        live_agent_handoff: Optional[
            outputs.CxPageEntryFulfillmentMessageLiveAgentHandoff
        ] = ...,
        output_audio_text: Optional[
            outputs.CxPageEntryFulfillmentMessageOutputAudioText
        ] = ...,
        payload: Optional[_builtins.str] = ...,
        play_audio: Optional[outputs.CxPageEntryFulfillmentMessagePlayAudio] = ...,
        telephony_transfer_call: Optional[
            outputs.CxPageEntryFulfillmentMessageTelephonyTransferCall
        ] = ...,
        text: Optional[outputs.CxPageEntryFulfillmentMessageText] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(
        self,
    ) -> Optional[outputs.CxPageEntryFulfillmentMessageConversationSuccess]: ...
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> Optional[outputs.CxPageEntryFulfillmentMessageLiveAgentHandoff]: ...
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(
        self,
    ) -> Optional[outputs.CxPageEntryFulfillmentMessageOutputAudioText]: ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(
        self,
    ) -> Optional[outputs.CxPageEntryFulfillmentMessagePlayAudio]: ...
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> Optional[outputs.CxPageEntryFulfillmentMessageTelephonyTransferCall]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[outputs.CxPageEntryFulfillmentMessageText]: ...

@pulumi.output_type
class CxPageEntryFulfillmentMessageConversationSuccess(dict):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageEntryFulfillmentMessageLiveAgentHandoff(dict):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageEntryFulfillmentMessageOutputAudioText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        ssml: Optional[_builtins.str] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageEntryFulfillmentMessagePlayAudio(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_uri: _builtins.str,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxPageEntryFulfillmentMessageTelephonyTransferCall(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, phone_number: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str: ...

@pulumi.output_type
class CxPageEntryFulfillmentMessageText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        texts: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CxPageEntryFulfillmentSetParameterAction(dict):
    def __init__(
        __self__,
        *,
        parameter: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageEventHandler(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        target_flow: Optional[_builtins.str] = ...,
        target_page: Optional[_builtins.str] = ...,
        trigger_fulfillment: Optional[
            outputs.CxPageEventHandlerTriggerFulfillment
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def event(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetFlow")
    def target_flow(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetPage")
    def target_page(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="triggerFulfillment")
    def trigger_fulfillment(
        self,
    ) -> Optional[outputs.CxPageEventHandlerTriggerFulfillment]: ...

@pulumi.output_type
class CxPageEventHandlerTriggerFulfillment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conditional_cases: Optional[
            Sequence[outputs.CxPageEventHandlerTriggerFulfillmentConditionalCase]
        ] = ...,
        messages: Optional[
            Sequence[outputs.CxPageEventHandlerTriggerFulfillmentMessage]
        ] = ...,
        return_partial_responses: Optional[_builtins.bool] = ...,
        set_parameter_actions: Optional[
            Sequence[outputs.CxPageEventHandlerTriggerFulfillmentSetParameterAction]
        ] = ...,
        tag: Optional[_builtins.str] = ...,
        webhook: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(
        self,
    ) -> Optional[
        Sequence[outputs.CxPageEventHandlerTriggerFulfillmentConditionalCase]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def messages(
        self,
    ) -> Optional[Sequence[outputs.CxPageEventHandlerTriggerFulfillmentMessage]]: ...
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> Optional[
        Sequence[outputs.CxPageEventHandlerTriggerFulfillmentSetParameterAction]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageEventHandlerTriggerFulfillmentConditionalCase(dict):
    def __init__(__self__, *, cases: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageEventHandlerTriggerFulfillmentMessage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channel: Optional[_builtins.str] = ...,
        conversation_success: Optional[
            outputs.CxPageEventHandlerTriggerFulfillmentMessageConversationSuccess
        ] = ...,
        live_agent_handoff: Optional[
            outputs.CxPageEventHandlerTriggerFulfillmentMessageLiveAgentHandoff
        ] = ...,
        output_audio_text: Optional[
            outputs.CxPageEventHandlerTriggerFulfillmentMessageOutputAudioText
        ] = ...,
        payload: Optional[_builtins.str] = ...,
        play_audio: Optional[
            outputs.CxPageEventHandlerTriggerFulfillmentMessagePlayAudio
        ] = ...,
        telephony_transfer_call: Optional[
            outputs.CxPageEventHandlerTriggerFulfillmentMessageTelephonyTransferCall
        ] = ...,
        text: Optional[outputs.CxPageEventHandlerTriggerFulfillmentMessageText] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(
        self,
    ) -> Optional[
        outputs.CxPageEventHandlerTriggerFulfillmentMessageConversationSuccess
    ]: ...
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> Optional[
        outputs.CxPageEventHandlerTriggerFulfillmentMessageLiveAgentHandoff
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(
        self,
    ) -> Optional[
        outputs.CxPageEventHandlerTriggerFulfillmentMessageOutputAudioText
    ]: ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(
        self,
    ) -> Optional[outputs.CxPageEventHandlerTriggerFulfillmentMessagePlayAudio]: ...
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> Optional[
        outputs.CxPageEventHandlerTriggerFulfillmentMessageTelephonyTransferCall
    ]: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[outputs.CxPageEventHandlerTriggerFulfillmentMessageText]: ...

@pulumi.output_type
class CxPageEventHandlerTriggerFulfillmentMessageConversationSuccess(dict):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageEventHandlerTriggerFulfillmentMessageLiveAgentHandoff(dict):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageEventHandlerTriggerFulfillmentMessageOutputAudioText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        ssml: Optional[_builtins.str] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageEventHandlerTriggerFulfillmentMessagePlayAudio(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_uri: _builtins.str,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxPageEventHandlerTriggerFulfillmentMessageTelephonyTransferCall(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, phone_number: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str: ...

@pulumi.output_type
class CxPageEventHandlerTriggerFulfillmentMessageText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        texts: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CxPageEventHandlerTriggerFulfillmentSetParameterAction(dict):
    def __init__(
        __self__,
        *,
        parameter: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageForm(dict):
    def __init__(
        __self__, *, parameters: Optional[Sequence[outputs.CxPageFormParameter]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[outputs.CxPageFormParameter]]: ...

@pulumi.output_type
class CxPageFormParameter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        advanced_settings: Optional[outputs.CxPageFormParameterAdvancedSettings] = ...,
        default_value: Optional[_builtins.str] = ...,
        display_name: Optional[_builtins.str] = ...,
        entity_type: Optional[_builtins.str] = ...,
        fill_behavior: Optional[outputs.CxPageFormParameterFillBehavior] = ...,
        is_list: Optional[_builtins.bool] = ...,
        redact: Optional[_builtins.bool] = ...,
        required: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(
        self,
    ) -> Optional[outputs.CxPageFormParameterAdvancedSettings]: ...
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="fillBehavior")
    def fill_behavior(self) -> Optional[outputs.CxPageFormParameterFillBehavior]: ...
    @_builtins.property
    @pulumi.getter(name="isList")
    def is_list(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def redact(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxPageFormParameterAdvancedSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dtmf_settings: Optional[
            outputs.CxPageFormParameterAdvancedSettingsDtmfSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dtmfSettings")
    def dtmf_settings(
        self,
    ) -> Optional[outputs.CxPageFormParameterAdvancedSettingsDtmfSettings]: ...

@pulumi.output_type
class CxPageFormParameterAdvancedSettingsDtmfSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        finish_digit: Optional[_builtins.str] = ...,
        max_digits: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxDigits")
    def max_digits(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CxPageFormParameterFillBehavior(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        initial_prompt_fulfillment: Optional[
            outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillment
        ] = ...,
        reprompt_event_handlers: Optional[
            Sequence[outputs.CxPageFormParameterFillBehaviorRepromptEventHandler]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="initialPromptFulfillment")
    def initial_prompt_fulfillment(
        self,
    ) -> Optional[outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillment]: ...
    @_builtins.property
    @pulumi.getter(name="repromptEventHandlers")
    def reprompt_event_handlers(
        self,
    ) -> Optional[
        Sequence[outputs.CxPageFormParameterFillBehaviorRepromptEventHandler]
    ]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conditional_cases: Optional[
            Sequence[
                outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentConditionalCase
            ]
        ] = ...,
        messages: Optional[
            Sequence[
                outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessage
            ]
        ] = ...,
        return_partial_responses: Optional[_builtins.bool] = ...,
        set_parameter_actions: Optional[
            Sequence[
                outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentSetParameterAction
            ]
        ] = ...,
        tag: Optional[_builtins.str] = ...,
        webhook: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentConditionalCase
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def messages(
        self,
    ) -> Optional[
        Sequence[outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessage]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentSetParameterAction
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentConditionalCase(dict):
    def __init__(__self__, *, cases: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channel: Optional[_builtins.str] = ...,
        conversation_success: Optional[
            outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageConversationSuccess
        ] = ...,
        live_agent_handoff: Optional[
            outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageLiveAgentHandoff
        ] = ...,
        output_audio_text: Optional[
            outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageOutputAudioText
        ] = ...,
        payload: Optional[_builtins.str] = ...,
        play_audio: Optional[
            outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessagePlayAudio
        ] = ...,
        telephony_transfer_call: Optional[
            outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageTelephonyTransferCall
        ] = ...,
        text: Optional[
            outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageText
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(
        self,
    ) -> Optional[
        outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageConversationSuccess
    ]: ...
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> Optional[
        outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageLiveAgentHandoff
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(
        self,
    ) -> Optional[
        outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageOutputAudioText
    ]: ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(
        self,
    ) -> Optional[
        outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessagePlayAudio
    ]: ...
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> Optional[
        outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageTelephonyTransferCall
    ]: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[
        outputs.CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageText
    ]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageConversationSuccess(
    dict
):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageLiveAgentHandoff(
    dict
):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageOutputAudioText(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        ssml: Optional[_builtins.str] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessagePlayAudio(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_uri: _builtins.str,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageTelephonyTransferCall(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, phone_number: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        texts: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentSetParameterAction(dict):
    def __init__(
        __self__,
        *,
        parameter: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorRepromptEventHandler(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        event: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        target_flow: Optional[_builtins.str] = ...,
        target_page: Optional[_builtins.str] = ...,
        trigger_fulfillment: Optional[
            outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillment
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def event(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetFlow")
    def target_flow(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetPage")
    def target_page(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="triggerFulfillment")
    def trigger_fulfillment(
        self,
    ) -> Optional[
        outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillment
    ]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conditional_cases: Optional[
            Sequence[
                outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentConditionalCase
            ]
        ] = ...,
        messages: Optional[
            Sequence[
                outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessage
            ]
        ] = ...,
        return_partial_responses: Optional[_builtins.bool] = ...,
        set_parameter_actions: Optional[
            Sequence[
                outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentSetParameterAction
            ]
        ] = ...,
        tag: Optional[_builtins.str] = ...,
        webhook: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentConditionalCase
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def messages(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessage
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentSetParameterAction
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentConditionalCase(
    dict
):
    def __init__(__self__, *, cases: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessage(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channel: Optional[_builtins.str] = ...,
        conversation_success: Optional[
            outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageConversationSuccess
        ] = ...,
        live_agent_handoff: Optional[
            outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageLiveAgentHandoff
        ] = ...,
        output_audio_text: Optional[
            outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageOutputAudioText
        ] = ...,
        payload: Optional[_builtins.str] = ...,
        play_audio: Optional[
            outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessagePlayAudio
        ] = ...,
        telephony_transfer_call: Optional[
            outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageTelephonyTransferCall
        ] = ...,
        text: Optional[
            outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageText
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(
        self,
    ) -> Optional[
        outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageConversationSuccess
    ]: ...
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> Optional[
        outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageLiveAgentHandoff
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(
        self,
    ) -> Optional[
        outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageOutputAudioText
    ]: ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(
        self,
    ) -> Optional[
        outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessagePlayAudio
    ]: ...
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> Optional[
        outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageTelephonyTransferCall
    ]: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[
        outputs.CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageText
    ]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageConversationSuccess(
    dict
):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageLiveAgentHandoff(
    dict
):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageOutputAudioText(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        ssml: Optional[_builtins.str] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessagePlayAudio(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_uri: _builtins.str,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageTelephonyTransferCall(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, phone_number: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageText(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        texts: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentSetParameterAction(
    dict
):
    def __init__(
        __self__,
        *,
        parameter: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_store_connections: Optional[
            Sequence[outputs.CxPageKnowledgeConnectorSettingsDataStoreConnection]
        ] = ...,
        enabled: Optional[_builtins.bool] = ...,
        target_flow: Optional[_builtins.str] = ...,
        target_page: Optional[_builtins.str] = ...,
        trigger_fulfillment: Optional[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillment
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreConnections")
    def data_store_connections(
        self,
    ) -> Optional[
        Sequence[outputs.CxPageKnowledgeConnectorSettingsDataStoreConnection]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="targetFlow")
    def target_flow(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetPage")
    def target_page(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="triggerFulfillment")
    def trigger_fulfillment(
        self,
    ) -> Optional[outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillment]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsDataStoreConnection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_store: Optional[_builtins.str] = ...,
        data_store_type: Optional[_builtins.str] = ...,
        document_processing_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreType")
    def data_store_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentProcessingMode")
    def document_processing_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        advanced_settings: Optional[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettings
        ] = ...,
        conditional_cases: Optional[
            Sequence[
                outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentConditionalCase
            ]
        ] = ...,
        enable_generative_fallback: Optional[_builtins.bool] = ...,
        messages: Optional[
            Sequence[outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessage]
        ] = ...,
        return_partial_responses: Optional[_builtins.bool] = ...,
        set_parameter_actions: Optional[
            Sequence[
                outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentSetParameterAction
            ]
        ] = ...,
        tag: Optional[_builtins.str] = ...,
        webhook: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(
        self,
    ) -> Optional[
        outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentConditionalCase
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="enableGenerativeFallback")
    def enable_generative_fallback(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def messages(
        self,
    ) -> Optional[
        Sequence[outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessage]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentSetParameterAction
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dtmf_settings: Optional[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettings
        ] = ...,
        logging_settings: Optional[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettings
        ] = ...,
        speech_settings: Optional[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettings
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dtmfSettings")
    def dtmf_settings(
        self,
    ) -> Optional[
        outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="loggingSettings")
    def logging_settings(
        self,
    ) -> Optional[
        outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettings
    ]: ...
    @_builtins.property
    @pulumi.getter(name="speechSettings")
    def speech_settings(
        self,
    ) -> Optional[
        outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettings
    ]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enabled: Optional[_builtins.bool] = ...,
        endpointing_timeout_duration: Optional[_builtins.str] = ...,
        finish_digit: Optional[_builtins.str] = ...,
        interdigit_timeout_duration: Optional[_builtins.str] = ...,
        max_digits: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="endpointingTimeoutDuration")
    def endpointing_timeout_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="interdigitTimeoutDuration")
    def interdigit_timeout_duration(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="maxDigits")
    def max_digits(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_consent_based_redaction: Optional[_builtins.bool] = ...,
        enable_interaction_logging: Optional[_builtins.bool] = ...,
        enable_stackdriver_logging: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableConsentBasedRedaction")
    def enable_consent_based_redaction(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableInteractionLogging")
    def enable_interaction_logging(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettings(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        endpointer_sensitivity: Optional[_builtins.int] = ...,
        models: Optional[Mapping[str, _builtins.str]] = ...,
        no_speech_timeout: Optional[_builtins.str] = ...,
        use_timeout_based_endpointing: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="endpointerSensitivity")
    def endpointer_sensitivity(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def models(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="noSpeechTimeout")
    def no_speech_timeout(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="useTimeoutBasedEndpointing")
    def use_timeout_based_endpointing(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentConditionalCase(dict):
    def __init__(__self__, *, cases: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channel: Optional[_builtins.str] = ...,
        conversation_success: Optional[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccess
        ] = ...,
        end_interactions: Optional[
            Sequence[
                outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteraction
            ]
        ] = ...,
        knowledge_info_card: Optional[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCard
        ] = ...,
        live_agent_handoff: Optional[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoff
        ] = ...,
        mixed_audios: Optional[
            Sequence[
                outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudio
            ]
        ] = ...,
        output_audio_text: Optional[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioText
        ] = ...,
        payload: Optional[_builtins.str] = ...,
        play_audio: Optional[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudio
        ] = ...,
        telephony_transfer_call: Optional[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCall
        ] = ...,
        text: Optional[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageText
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(
        self,
    ) -> Optional[
        outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccess
    ]: ...
    @_builtins.property
    @pulumi.getter(name="endInteractions")
    def end_interactions(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteraction
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="knowledgeInfoCard")
    def knowledge_info_card(
        self,
    ) -> Optional[
        outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCard
    ]: ...
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> Optional[
        outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoff
    ]: ...
    @_builtins.property
    @pulumi.getter(name="mixedAudios")
    def mixed_audios(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudio
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(
        self,
    ) -> Optional[
        outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioText
    ]: ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(
        self,
    ) -> Optional[
        outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudio
    ]: ...
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> Optional[
        outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCall
    ]: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[
        outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageText
    ]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccess(
    dict
):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteraction(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCard(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoff(dict):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudio(dict):
    def __init__(
        __self__,
        *,
        segments: Optional[
            Sequence[
                outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegment
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def segments(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegment
        ]
    ]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        audio: Optional[_builtins.str] = ...,
        uri: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def audio(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        ssml: Optional[_builtins.str] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudio(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_uri: _builtins.str,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCall(
    dict
):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, phone_number: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        texts: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentSetParameterAction(dict):
    def __init__(
        __self__,
        *,
        parameter: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageTransitionRoute(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        condition: Optional[_builtins.str] = ...,
        intent: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        target_flow: Optional[_builtins.str] = ...,
        target_page: Optional[_builtins.str] = ...,
        trigger_fulfillment: Optional[
            outputs.CxPageTransitionRouteTriggerFulfillment
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetFlow")
    def target_flow(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="targetPage")
    def target_page(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="triggerFulfillment")
    def trigger_fulfillment(
        self,
    ) -> Optional[outputs.CxPageTransitionRouteTriggerFulfillment]: ...

@pulumi.output_type
class CxPageTransitionRouteTriggerFulfillment(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conditional_cases: Optional[
            Sequence[outputs.CxPageTransitionRouteTriggerFulfillmentConditionalCase]
        ] = ...,
        messages: Optional[
            Sequence[outputs.CxPageTransitionRouteTriggerFulfillmentMessage]
        ] = ...,
        return_partial_responses: Optional[_builtins.bool] = ...,
        set_parameter_actions: Optional[
            Sequence[outputs.CxPageTransitionRouteTriggerFulfillmentSetParameterAction]
        ] = ...,
        tag: Optional[_builtins.str] = ...,
        webhook: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(
        self,
    ) -> Optional[
        Sequence[outputs.CxPageTransitionRouteTriggerFulfillmentConditionalCase]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def messages(
        self,
    ) -> Optional[Sequence[outputs.CxPageTransitionRouteTriggerFulfillmentMessage]]: ...
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(
        self,
    ) -> Optional[
        Sequence[outputs.CxPageTransitionRouteTriggerFulfillmentSetParameterAction]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageTransitionRouteTriggerFulfillmentConditionalCase(dict):
    def __init__(__self__, *, cases: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageTransitionRouteTriggerFulfillmentMessage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        channel: Optional[_builtins.str] = ...,
        conversation_success: Optional[
            outputs.CxPageTransitionRouteTriggerFulfillmentMessageConversationSuccess
        ] = ...,
        live_agent_handoff: Optional[
            outputs.CxPageTransitionRouteTriggerFulfillmentMessageLiveAgentHandoff
        ] = ...,
        output_audio_text: Optional[
            outputs.CxPageTransitionRouteTriggerFulfillmentMessageOutputAudioText
        ] = ...,
        payload: Optional[_builtins.str] = ...,
        play_audio: Optional[
            outputs.CxPageTransitionRouteTriggerFulfillmentMessagePlayAudio
        ] = ...,
        telephony_transfer_call: Optional[
            outputs.CxPageTransitionRouteTriggerFulfillmentMessageTelephonyTransferCall
        ] = ...,
        text: Optional[
            outputs.CxPageTransitionRouteTriggerFulfillmentMessageText
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(
        self,
    ) -> Optional[
        outputs.CxPageTransitionRouteTriggerFulfillmentMessageConversationSuccess
    ]: ...
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(
        self,
    ) -> Optional[
        outputs.CxPageTransitionRouteTriggerFulfillmentMessageLiveAgentHandoff
    ]: ...
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(
        self,
    ) -> Optional[
        outputs.CxPageTransitionRouteTriggerFulfillmentMessageOutputAudioText
    ]: ...
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(
        self,
    ) -> Optional[outputs.CxPageTransitionRouteTriggerFulfillmentMessagePlayAudio]: ...
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(
        self,
    ) -> Optional[
        outputs.CxPageTransitionRouteTriggerFulfillmentMessageTelephonyTransferCall
    ]: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[outputs.CxPageTransitionRouteTriggerFulfillmentMessageText]: ...

@pulumi.output_type
class CxPageTransitionRouteTriggerFulfillmentMessageConversationSuccess(dict):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageTransitionRouteTriggerFulfillmentMessageLiveAgentHandoff(dict):
    def __init__(__self__, *, metadata: Optional[_builtins.str] = ...) -> None: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageTransitionRouteTriggerFulfillmentMessageOutputAudioText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        ssml: Optional[_builtins.str] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPageTransitionRouteTriggerFulfillmentMessagePlayAudio(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_uri: _builtins.str,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxPageTransitionRouteTriggerFulfillmentMessageTelephonyTransferCall(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, phone_number: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> _builtins.str: ...

@pulumi.output_type
class CxPageTransitionRouteTriggerFulfillmentMessageText(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        allow_playback_interruption: Optional[_builtins.bool] = ...,
        texts: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CxPageTransitionRouteTriggerFulfillmentSetParameterAction(dict):
    def __init__(
        __self__,
        *,
        parameter: Optional[_builtins.str] = ...,
        value: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPlaybookInstruction(dict):
    def __init__(
        __self__,
        *,
        guidelines: Optional[_builtins.str] = ...,
        steps: Optional[Sequence[outputs.CxPlaybookInstructionStep]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def guidelines(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def steps(self) -> Optional[Sequence[outputs.CxPlaybookInstructionStep]]: ...

@pulumi.output_type
class CxPlaybookInstructionStep(dict):
    def __init__(
        __self__,
        *,
        steps: Optional[_builtins.str] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def steps(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxPlaybookLlmModelSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        model: Optional[_builtins.str] = ...,
        prompt_text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="promptText")
    def prompt_text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxSecuritySettingsAudioExportSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        audio_export_pattern: Optional[_builtins.str] = ...,
        audio_format: Optional[_builtins.str] = ...,
        enable_audio_redaction: Optional[_builtins.bool] = ...,
        gcs_bucket: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioExportPattern")
    def audio_export_pattern(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="audioFormat")
    def audio_format(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="enableAudioRedaction")
    def enable_audio_redaction(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="gcsBucket")
    def gcs_bucket(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxSecuritySettingsInsightsExportSettings(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, enable_insights_export: _builtins.bool) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableInsightsExport")
    def enable_insights_export(self) -> _builtins.bool: ...

@pulumi.output_type
class CxTestCaseLastTestResult(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        conversation_turns: Optional[
            Sequence[outputs.CxTestCaseLastTestResultConversationTurn]
        ] = ...,
        environment: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        test_result: Optional[_builtins.str] = ...,
        test_time: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conversationTurns")
    def conversation_turns(
        self,
    ) -> Optional[Sequence[outputs.CxTestCaseLastTestResultConversationTurn]]: ...
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="testResult")
    def test_result(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="testTime")
    def test_time(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxTestCaseLastTestResultConversationTurn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        user_input: Optional[
            outputs.CxTestCaseLastTestResultConversationTurnUserInput
        ] = ...,
        virtual_agent_output: Optional[
            outputs.CxTestCaseLastTestResultConversationTurnVirtualAgentOutput
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userInput")
    def user_input(
        self,
    ) -> Optional[outputs.CxTestCaseLastTestResultConversationTurnUserInput]: ...
    @_builtins.property
    @pulumi.getter(name="virtualAgentOutput")
    def virtual_agent_output(
        self,
    ) -> Optional[
        outputs.CxTestCaseLastTestResultConversationTurnVirtualAgentOutput
    ]: ...

@pulumi.output_type
class CxTestCaseLastTestResultConversationTurnUserInput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_sentiment_analysis: Optional[_builtins.bool] = ...,
        injected_parameters: Optional[_builtins.str] = ...,
        input: Optional[
            outputs.CxTestCaseLastTestResultConversationTurnUserInputInput
        ] = ...,
        is_webhook_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableSentimentAnalysis")
    def enable_sentiment_analysis(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="injectedParameters")
    def injected_parameters(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def input(
        self,
    ) -> Optional[outputs.CxTestCaseLastTestResultConversationTurnUserInputInput]: ...
    @_builtins.property
    @pulumi.getter(name="isWebhookEnabled")
    def is_webhook_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxTestCaseLastTestResultConversationTurnUserInputInput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dtmf: Optional[
            outputs.CxTestCaseLastTestResultConversationTurnUserInputInputDtmf
        ] = ...,
        event: Optional[
            outputs.CxTestCaseLastTestResultConversationTurnUserInputInputEvent
        ] = ...,
        language_code: Optional[_builtins.str] = ...,
        text: Optional[
            outputs.CxTestCaseLastTestResultConversationTurnUserInputInputText
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dtmf(
        self,
    ) -> Optional[
        outputs.CxTestCaseLastTestResultConversationTurnUserInputInputDtmf
    ]: ...
    @_builtins.property
    @pulumi.getter
    def event(
        self,
    ) -> Optional[
        outputs.CxTestCaseLastTestResultConversationTurnUserInputInputEvent
    ]: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[
        outputs.CxTestCaseLastTestResultConversationTurnUserInputInputText
    ]: ...

@pulumi.output_type
class CxTestCaseLastTestResultConversationTurnUserInputInputDtmf(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        digits: Optional[_builtins.str] = ...,
        finish_digit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def digits(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxTestCaseLastTestResultConversationTurnUserInputInputEvent(dict):
    def __init__(__self__, *, event: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def event(self) -> _builtins.str: ...

@pulumi.output_type
class CxTestCaseLastTestResultConversationTurnUserInputInputText(dict):
    def __init__(__self__, *, text: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str: ...

@pulumi.output_type
class CxTestCaseLastTestResultConversationTurnVirtualAgentOutput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        current_page: Optional[
            outputs.CxTestCaseLastTestResultConversationTurnVirtualAgentOutputCurrentPage
        ] = ...,
        differences: Optional[
            Sequence[
                outputs.CxTestCaseLastTestResultConversationTurnVirtualAgentOutputDifference
            ]
        ] = ...,
        session_parameters: Optional[_builtins.str] = ...,
        status: Optional[
            outputs.CxTestCaseLastTestResultConversationTurnVirtualAgentOutputStatus
        ] = ...,
        text_responses: Optional[
            Sequence[
                outputs.CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTextResponse
            ]
        ] = ...,
        triggered_intent: Optional[
            outputs.CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTriggeredIntent
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentPage")
    def current_page(
        self,
    ) -> Optional[
        outputs.CxTestCaseLastTestResultConversationTurnVirtualAgentOutputCurrentPage
    ]: ...
    @_builtins.property
    @pulumi.getter
    def differences(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxTestCaseLastTestResultConversationTurnVirtualAgentOutputDifference
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sessionParameters")
    def session_parameters(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def status(
        self,
    ) -> Optional[
        outputs.CxTestCaseLastTestResultConversationTurnVirtualAgentOutputStatus
    ]: ...
    @_builtins.property
    @pulumi.getter(name="textResponses")
    def text_responses(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTextResponse
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="triggeredIntent")
    def triggered_intent(
        self,
    ) -> Optional[
        outputs.CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTriggeredIntent
    ]: ...

@pulumi.output_type
class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputCurrentPage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        display_name: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputDifference(dict):
    def __init__(
        __self__,
        *,
        description: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputStatus(dict):
    def __init__(
        __self__,
        *,
        code: Optional[_builtins.int] = ...,
        details: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTextResponse(dict):
    def __init__(
        __self__, *, texts: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTriggeredIntent(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        display_name: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxTestCaseTestCaseConversationTurn(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        user_input: Optional[outputs.CxTestCaseTestCaseConversationTurnUserInput] = ...,
        virtual_agent_output: Optional[
            outputs.CxTestCaseTestCaseConversationTurnVirtualAgentOutput
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="userInput")
    def user_input(
        self,
    ) -> Optional[outputs.CxTestCaseTestCaseConversationTurnUserInput]: ...
    @_builtins.property
    @pulumi.getter(name="virtualAgentOutput")
    def virtual_agent_output(
        self,
    ) -> Optional[outputs.CxTestCaseTestCaseConversationTurnVirtualAgentOutput]: ...

@pulumi.output_type
class CxTestCaseTestCaseConversationTurnUserInput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        enable_sentiment_analysis: Optional[_builtins.bool] = ...,
        injected_parameters: Optional[_builtins.str] = ...,
        input: Optional[outputs.CxTestCaseTestCaseConversationTurnUserInputInput] = ...,
        is_webhook_enabled: Optional[_builtins.bool] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableSentimentAnalysis")
    def enable_sentiment_analysis(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="injectedParameters")
    def injected_parameters(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def input(
        self,
    ) -> Optional[outputs.CxTestCaseTestCaseConversationTurnUserInputInput]: ...
    @_builtins.property
    @pulumi.getter(name="isWebhookEnabled")
    def is_webhook_enabled(self) -> Optional[_builtins.bool]: ...

@pulumi.output_type
class CxTestCaseTestCaseConversationTurnUserInputInput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        dtmf: Optional[
            outputs.CxTestCaseTestCaseConversationTurnUserInputInputDtmf
        ] = ...,
        event: Optional[
            outputs.CxTestCaseTestCaseConversationTurnUserInputInputEvent
        ] = ...,
        language_code: Optional[_builtins.str] = ...,
        text: Optional[
            outputs.CxTestCaseTestCaseConversationTurnUserInputInputText
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dtmf(
        self,
    ) -> Optional[outputs.CxTestCaseTestCaseConversationTurnUserInputInputDtmf]: ...
    @_builtins.property
    @pulumi.getter
    def event(
        self,
    ) -> Optional[outputs.CxTestCaseTestCaseConversationTurnUserInputInputEvent]: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def text(
        self,
    ) -> Optional[outputs.CxTestCaseTestCaseConversationTurnUserInputInputText]: ...

@pulumi.output_type
class CxTestCaseTestCaseConversationTurnUserInputInputDtmf(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        digits: Optional[_builtins.str] = ...,
        finish_digit: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def digits(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxTestCaseTestCaseConversationTurnUserInputInputEvent(dict):
    def __init__(__self__, *, event: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def event(self) -> _builtins.str: ...

@pulumi.output_type
class CxTestCaseTestCaseConversationTurnUserInputInputText(dict):
    def __init__(__self__, *, text: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str: ...

@pulumi.output_type
class CxTestCaseTestCaseConversationTurnVirtualAgentOutput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        current_page: Optional[
            outputs.CxTestCaseTestCaseConversationTurnVirtualAgentOutputCurrentPage
        ] = ...,
        session_parameters: Optional[_builtins.str] = ...,
        text_responses: Optional[
            Sequence[
                outputs.CxTestCaseTestCaseConversationTurnVirtualAgentOutputTextResponse
            ]
        ] = ...,
        triggered_intent: Optional[
            outputs.CxTestCaseTestCaseConversationTurnVirtualAgentOutputTriggeredIntent
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="currentPage")
    def current_page(
        self,
    ) -> Optional[
        outputs.CxTestCaseTestCaseConversationTurnVirtualAgentOutputCurrentPage
    ]: ...
    @_builtins.property
    @pulumi.getter(name="sessionParameters")
    def session_parameters(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="textResponses")
    def text_responses(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxTestCaseTestCaseConversationTurnVirtualAgentOutputTextResponse
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="triggeredIntent")
    def triggered_intent(
        self,
    ) -> Optional[
        outputs.CxTestCaseTestCaseConversationTurnVirtualAgentOutputTriggeredIntent
    ]: ...

@pulumi.output_type
class CxTestCaseTestCaseConversationTurnVirtualAgentOutputCurrentPage(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        display_name: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxTestCaseTestCaseConversationTurnVirtualAgentOutputTextResponse(dict):
    def __init__(
        __self__, *, texts: Optional[Sequence[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CxTestCaseTestCaseConversationTurnVirtualAgentOutputTriggeredIntent(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        display_name: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxTestCaseTestConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        flow: Optional[_builtins.str] = ...,
        page: Optional[_builtins.str] = ...,
        tracking_parameters: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def flow(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def page(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="trackingParameters")
    def tracking_parameters(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CxToolConnectorSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions: Sequence[outputs.CxToolConnectorSpecAction],
        name: _builtins.str,
        end_user_auth_config: Optional[
            outputs.CxToolConnectorSpecEndUserAuthConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[outputs.CxToolConnectorSpecAction]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endUserAuthConfig")
    def end_user_auth_config(
        self,
    ) -> Optional[outputs.CxToolConnectorSpecEndUserAuthConfig]: ...

@pulumi.output_type
class CxToolConnectorSpecAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_action_id: Optional[_builtins.str] = ...,
        entity_operation: Optional[
            outputs.CxToolConnectorSpecActionEntityOperation
        ] = ...,
        input_fields: Optional[Sequence[_builtins.str]] = ...,
        output_fields: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionActionId")
    def connection_action_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityOperation")
    def entity_operation(
        self,
    ) -> Optional[outputs.CxToolConnectorSpecActionEntityOperation]: ...
    @_builtins.property
    @pulumi.getter(name="inputFields")
    def input_fields(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="outputFields")
    def output_fields(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CxToolConnectorSpecActionEntityOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, entity_id: _builtins.str, operation: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> _builtins.str: ...

@pulumi.output_type
class CxToolConnectorSpecEndUserAuthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        oauth2_auth_code_config: Optional[
            outputs.CxToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfig
        ] = ...,
        oauth2_jwt_bearer_config: Optional[
            outputs.CxToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oauth2AuthCodeConfig")
    def oauth2_auth_code_config(
        self,
    ) -> Optional[outputs.CxToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfig]: ...
    @_builtins.property
    @pulumi.getter(name="oauth2JwtBearerConfig")
    def oauth2_jwt_bearer_config(
        self,
    ) -> Optional[
        outputs.CxToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfig
    ]: ...

@pulumi.output_type
class CxToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, oauth_token: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oauthToken")
    def oauth_token(self) -> _builtins.str: ...

@pulumi.output_type
class CxToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_key: _builtins.str,
        issuer: _builtins.str,
        subject: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str: ...

@pulumi.output_type
class CxToolDataStoreSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_store_connections: Sequence[
            outputs.CxToolDataStoreSpecDataStoreConnection
        ],
        fallback_prompt: outputs.CxToolDataStoreSpecFallbackPrompt,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreConnections")
    def data_store_connections(
        self,
    ) -> Sequence[outputs.CxToolDataStoreSpecDataStoreConnection]: ...
    @_builtins.property
    @pulumi.getter(name="fallbackPrompt")
    def fallback_prompt(self) -> outputs.CxToolDataStoreSpecFallbackPrompt: ...

@pulumi.output_type
class CxToolDataStoreSpecDataStoreConnection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_store: Optional[_builtins.str] = ...,
        data_store_type: Optional[_builtins.str] = ...,
        document_processing_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreType")
    def data_store_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentProcessingMode")
    def document_processing_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxToolDataStoreSpecFallbackPrompt(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class CxToolFunctionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        input_schema: Optional[_builtins.str] = ...,
        output_schema: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputSchema")
    def input_schema(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputSchema")
    def output_schema(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxToolOpenApiSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        text_schema: _builtins.str,
        authentication: Optional[outputs.CxToolOpenApiSpecAuthentication] = ...,
        service_directory_config: Optional[
            outputs.CxToolOpenApiSpecServiceDirectoryConfig
        ] = ...,
        tls_config: Optional[outputs.CxToolOpenApiSpecTlsConfig] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="textSchema")
    def text_schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[outputs.CxToolOpenApiSpecAuthentication]: ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(
        self,
    ) -> Optional[outputs.CxToolOpenApiSpecServiceDirectoryConfig]: ...
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[outputs.CxToolOpenApiSpecTlsConfig]: ...

@pulumi.output_type
class CxToolOpenApiSpecAuthentication(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_key_config: Optional[
            outputs.CxToolOpenApiSpecAuthenticationApiKeyConfig
        ] = ...,
        bearer_token_config: Optional[
            outputs.CxToolOpenApiSpecAuthenticationBearerTokenConfig
        ] = ...,
        oauth_config: Optional[
            outputs.CxToolOpenApiSpecAuthenticationOauthConfig
        ] = ...,
        service_agent_auth_config: Optional[
            outputs.CxToolOpenApiSpecAuthenticationServiceAgentAuthConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyConfig")
    def api_key_config(
        self,
    ) -> Optional[outputs.CxToolOpenApiSpecAuthenticationApiKeyConfig]: ...
    @_builtins.property
    @pulumi.getter(name="bearerTokenConfig")
    def bearer_token_config(
        self,
    ) -> Optional[outputs.CxToolOpenApiSpecAuthenticationBearerTokenConfig]: ...
    @_builtins.property
    @pulumi.getter(name="oauthConfig")
    def oauth_config(
        self,
    ) -> Optional[outputs.CxToolOpenApiSpecAuthenticationOauthConfig]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAgentAuthConfig")
    def service_agent_auth_config(
        self,
    ) -> Optional[outputs.CxToolOpenApiSpecAuthenticationServiceAgentAuthConfig]: ...

@pulumi.output_type
class CxToolOpenApiSpecAuthenticationApiKeyConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_name: _builtins.str,
        request_location: _builtins.str,
        api_key: Optional[_builtins.str] = ...,
        secret_version_for_api_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requestLocation")
    def request_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretVersionForApiKey")
    def secret_version_for_api_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxToolOpenApiSpecAuthenticationBearerTokenConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        secret_version_for_token: Optional[_builtins.str] = ...,
        token: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersionForToken")
    def secret_version_for_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxToolOpenApiSpecAuthenticationOauthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: _builtins.str,
        oauth_grant_type: _builtins.str,
        token_endpoint: _builtins.str,
        client_secret: Optional[_builtins.str] = ...,
        scopes: Optional[Sequence[_builtins.str]] = ...,
        secret_version_for_client_secret: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oauthGrantType")
    def oauth_grant_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secretVersionForClientSecret")
    def secret_version_for_client_secret(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxToolOpenApiSpecAuthenticationServiceAgentAuthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, service_agent_auth: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAgentAuth")
    def service_agent_auth(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxToolOpenApiSpecServiceDirectoryConfig(dict):
    def __init__(__self__, *, service: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...

@pulumi.output_type
class CxToolOpenApiSpecTlsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, ca_certs: Sequence[outputs.CxToolOpenApiSpecTlsConfigCaCert]
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(self) -> Sequence[outputs.CxToolOpenApiSpecTlsConfigCaCert]: ...

@pulumi.output_type
class CxToolOpenApiSpecTlsConfigCaCert(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, cert: _builtins.str, display_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...

@pulumi.output_type
class CxToolVersionTool(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        description: _builtins.str,
        display_name: _builtins.str,
        connector_spec: Optional[outputs.CxToolVersionToolConnectorSpec] = ...,
        data_store_spec: Optional[outputs.CxToolVersionToolDataStoreSpec] = ...,
        function_spec: Optional[outputs.CxToolVersionToolFunctionSpec] = ...,
        name: Optional[_builtins.str] = ...,
        open_api_spec: Optional[outputs.CxToolVersionToolOpenApiSpec] = ...,
        tool_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="connectorSpec")
    def connector_spec(self) -> Optional[outputs.CxToolVersionToolConnectorSpec]: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreSpec")
    def data_store_spec(self) -> Optional[outputs.CxToolVersionToolDataStoreSpec]: ...
    @_builtins.property
    @pulumi.getter(name="functionSpec")
    def function_spec(self) -> Optional[outputs.CxToolVersionToolFunctionSpec]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="openApiSpec")
    def open_api_spec(self) -> Optional[outputs.CxToolVersionToolOpenApiSpec]: ...
    @_builtins.property
    @pulumi.getter(name="toolType")
    def tool_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxToolVersionToolConnectorSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        actions: Sequence[outputs.CxToolVersionToolConnectorSpecAction],
        name: _builtins.str,
        end_user_auth_config: Optional[
            outputs.CxToolVersionToolConnectorSpecEndUserAuthConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Sequence[outputs.CxToolVersionToolConnectorSpecAction]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="endUserAuthConfig")
    def end_user_auth_config(
        self,
    ) -> Optional[outputs.CxToolVersionToolConnectorSpecEndUserAuthConfig]: ...

@pulumi.output_type
class CxToolVersionToolConnectorSpecAction(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        connection_action_id: Optional[_builtins.str] = ...,
        entity_operation: Optional[
            outputs.CxToolVersionToolConnectorSpecActionEntityOperation
        ] = ...,
        input_fields: Optional[Sequence[_builtins.str]] = ...,
        output_fields: Optional[Sequence[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectionActionId")
    def connection_action_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="entityOperation")
    def entity_operation(
        self,
    ) -> Optional[outputs.CxToolVersionToolConnectorSpecActionEntityOperation]: ...
    @_builtins.property
    @pulumi.getter(name="inputFields")
    def input_fields(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="outputFields")
    def output_fields(self) -> Optional[Sequence[_builtins.str]]: ...

@pulumi.output_type
class CxToolVersionToolConnectorSpecActionEntityOperation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, entity_id: _builtins.str, operation: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def operation(self) -> _builtins.str: ...

@pulumi.output_type
class CxToolVersionToolConnectorSpecEndUserAuthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        oauth2_auth_code_config: Optional[
            outputs.CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfig
        ] = ...,
        oauth2_jwt_bearer_config: Optional[
            outputs.CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oauth2AuthCodeConfig")
    def oauth2_auth_code_config(
        self,
    ) -> Optional[
        outputs.CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="oauth2JwtBearerConfig")
    def oauth2_jwt_bearer_config(
        self,
    ) -> Optional[
        outputs.CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfig
    ]: ...

@pulumi.output_type
class CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, oauth_token: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="oauthToken")
    def oauth_token(self) -> _builtins.str: ...

@pulumi.output_type
class CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_key: _builtins.str,
        issuer: _builtins.str,
        subject: _builtins.str,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def subject(self) -> _builtins.str: ...

@pulumi.output_type
class CxToolVersionToolDataStoreSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_store_connections: Sequence[
            outputs.CxToolVersionToolDataStoreSpecDataStoreConnection
        ],
        fallback_prompt: outputs.CxToolVersionToolDataStoreSpecFallbackPrompt,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreConnections")
    def data_store_connections(
        self,
    ) -> Sequence[outputs.CxToolVersionToolDataStoreSpecDataStoreConnection]: ...
    @_builtins.property
    @pulumi.getter(name="fallbackPrompt")
    def fallback_prompt(
        self,
    ) -> outputs.CxToolVersionToolDataStoreSpecFallbackPrompt: ...

@pulumi.output_type
class CxToolVersionToolDataStoreSpecDataStoreConnection(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        data_store: Optional[_builtins.str] = ...,
        data_store_type: Optional[_builtins.str] = ...,
        document_processing_mode: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreType")
    def data_store_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="documentProcessingMode")
    def document_processing_mode(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxToolVersionToolDataStoreSpecFallbackPrompt(dict):
    def __init__(__self__) -> None: ...

@pulumi.output_type
class CxToolVersionToolFunctionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        input_schema: Optional[_builtins.str] = ...,
        output_schema: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="inputSchema")
    def input_schema(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="outputSchema")
    def output_schema(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxToolVersionToolOpenApiSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        text_schema: _builtins.str,
        authentication: Optional[
            outputs.CxToolVersionToolOpenApiSpecAuthentication
        ] = ...,
        service_directory_config: Optional[
            outputs.CxToolVersionToolOpenApiSpecServiceDirectoryConfig
        ] = ...,
        tls_config: Optional[outputs.CxToolVersionToolOpenApiSpecTlsConfig] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="textSchema")
    def text_schema(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def authentication(
        self,
    ) -> Optional[outputs.CxToolVersionToolOpenApiSpecAuthentication]: ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(
        self,
    ) -> Optional[outputs.CxToolVersionToolOpenApiSpecServiceDirectoryConfig]: ...
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[outputs.CxToolVersionToolOpenApiSpecTlsConfig]: ...

@pulumi.output_type
class CxToolVersionToolOpenApiSpecAuthentication(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        api_key_config: Optional[
            outputs.CxToolVersionToolOpenApiSpecAuthenticationApiKeyConfig
        ] = ...,
        bearer_token_config: Optional[
            outputs.CxToolVersionToolOpenApiSpecAuthenticationBearerTokenConfig
        ] = ...,
        oauth_config: Optional[
            outputs.CxToolVersionToolOpenApiSpecAuthenticationOauthConfig
        ] = ...,
        service_agent_auth_config: Optional[
            outputs.CxToolVersionToolOpenApiSpecAuthenticationServiceAgentAuthConfig
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyConfig")
    def api_key_config(
        self,
    ) -> Optional[outputs.CxToolVersionToolOpenApiSpecAuthenticationApiKeyConfig]: ...
    @_builtins.property
    @pulumi.getter(name="bearerTokenConfig")
    def bearer_token_config(
        self,
    ) -> Optional[
        outputs.CxToolVersionToolOpenApiSpecAuthenticationBearerTokenConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="oauthConfig")
    def oauth_config(
        self,
    ) -> Optional[outputs.CxToolVersionToolOpenApiSpecAuthenticationOauthConfig]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAgentAuthConfig")
    def service_agent_auth_config(
        self,
    ) -> Optional[
        outputs.CxToolVersionToolOpenApiSpecAuthenticationServiceAgentAuthConfig
    ]: ...

@pulumi.output_type
class CxToolVersionToolOpenApiSpecAuthenticationApiKeyConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        key_name: _builtins.str,
        request_location: _builtins.str,
        api_key: Optional[_builtins.str] = ...,
        secret_version_for_api_key: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requestLocation")
    def request_location(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretVersionForApiKey")
    def secret_version_for_api_key(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxToolVersionToolOpenApiSpecAuthenticationBearerTokenConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        secret_version_for_token: Optional[_builtins.str] = ...,
        token: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretVersionForToken")
    def secret_version_for_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxToolVersionToolOpenApiSpecAuthenticationOauthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: _builtins.str,
        oauth_grant_type: _builtins.str,
        token_endpoint: _builtins.str,
        client_secret: Optional[_builtins.str] = ...,
        scopes: Optional[Sequence[_builtins.str]] = ...,
        secret_version_for_client_secret: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="oauthGrantType")
    def oauth_grant_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secretVersionForClientSecret")
    def secret_version_for_client_secret(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxToolVersionToolOpenApiSpecAuthenticationServiceAgentAuthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, service_agent_auth: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAgentAuth")
    def service_agent_auth(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxToolVersionToolOpenApiSpecServiceDirectoryConfig(dict):
    def __init__(__self__, *, service: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...

@pulumi.output_type
class CxToolVersionToolOpenApiSpecTlsConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        ca_certs: Sequence[outputs.CxToolVersionToolOpenApiSpecTlsConfigCaCert],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(
        self,
    ) -> Sequence[outputs.CxToolVersionToolOpenApiSpecTlsConfigCaCert]: ...

@pulumi.output_type
class CxToolVersionToolOpenApiSpecTlsConfigCaCert(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, cert: _builtins.str, display_name: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str: ...

@pulumi.output_type
class CxVersionNluSetting(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        classification_threshold: Optional[_builtins.float] = ...,
        model_training_mode: Optional[_builtins.str] = ...,
        model_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="classificationThreshold")
    def classification_threshold(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="modelTrainingMode")
    def model_training_mode(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="modelType")
    def model_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxWebhookGenericWebService(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        uri: _builtins.str,
        allowed_ca_certs: Optional[Sequence[_builtins.str]] = ...,
        http_method: Optional[_builtins.str] = ...,
        oauth_config: Optional[outputs.CxWebhookGenericWebServiceOauthConfig] = ...,
        parameter_mapping: Optional[Mapping[str, _builtins.str]] = ...,
        request_body: Optional[_builtins.str] = ...,
        request_headers: Optional[Mapping[str, _builtins.str]] = ...,
        secret_version_for_username_password: Optional[_builtins.str] = ...,
        secret_versions_for_request_headers: Optional[
            Sequence[outputs.CxWebhookGenericWebServiceSecretVersionsForRequestHeader]
        ] = ...,
        service_account_auth_config: Optional[
            outputs.CxWebhookGenericWebServiceServiceAccountAuthConfig
        ] = ...,
        service_agent_auth: Optional[_builtins.str] = ...,
        webhook_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowedCaCerts")
    def allowed_ca_certs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthConfig")
    def oauth_config(
        self,
    ) -> Optional[outputs.CxWebhookGenericWebServiceOauthConfig]: ...
    @_builtins.property
    @pulumi.getter(name="parameterMapping")
    def parameter_mapping(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="requestBody")
    def request_body(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestHeaders")
    def request_headers(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secretVersionForUsernamePassword")
    def secret_version_for_username_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretVersionsForRequestHeaders")
    def secret_versions_for_request_headers(
        self,
    ) -> Optional[
        Sequence[outputs.CxWebhookGenericWebServiceSecretVersionsForRequestHeader]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountAuthConfig")
    def service_account_auth_config(
        self,
    ) -> Optional[outputs.CxWebhookGenericWebServiceServiceAccountAuthConfig]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAgentAuth")
    def service_agent_auth(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="webhookType")
    def webhook_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxWebhookGenericWebServiceOauthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: _builtins.str,
        token_endpoint: _builtins.str,
        client_secret: Optional[_builtins.str] = ...,
        scopes: Optional[Sequence[_builtins.str]] = ...,
        secret_version_for_client_secret: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secretVersionForClientSecret")
    def secret_version_for_client_secret(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxWebhookGenericWebServiceSecretVersionsForRequestHeader(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, key: _builtins.str, secret_version: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class CxWebhookGenericWebServiceServiceAccountAuthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, service_account: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str: ...

@pulumi.output_type
class CxWebhookServiceDirectory(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        service: _builtins.str,
        generic_web_service: Optional[
            outputs.CxWebhookServiceDirectoryGenericWebService
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="genericWebService")
    def generic_web_service(
        self,
    ) -> Optional[outputs.CxWebhookServiceDirectoryGenericWebService]: ...

@pulumi.output_type
class CxWebhookServiceDirectoryGenericWebService(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        uri: _builtins.str,
        allowed_ca_certs: Optional[Sequence[_builtins.str]] = ...,
        http_method: Optional[_builtins.str] = ...,
        oauth_config: Optional[
            outputs.CxWebhookServiceDirectoryGenericWebServiceOauthConfig
        ] = ...,
        parameter_mapping: Optional[Mapping[str, _builtins.str]] = ...,
        request_body: Optional[_builtins.str] = ...,
        request_headers: Optional[Mapping[str, _builtins.str]] = ...,
        secret_version_for_username_password: Optional[_builtins.str] = ...,
        secret_versions_for_request_headers: Optional[
            Sequence[
                outputs.CxWebhookServiceDirectoryGenericWebServiceSecretVersionsForRequestHeader
            ]
        ] = ...,
        service_account_auth_config: Optional[
            outputs.CxWebhookServiceDirectoryGenericWebServiceServiceAccountAuthConfig
        ] = ...,
        service_agent_auth: Optional[_builtins.str] = ...,
        webhook_type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="allowedCaCerts")
    def allowed_ca_certs(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="oauthConfig")
    def oauth_config(
        self,
    ) -> Optional[outputs.CxWebhookServiceDirectoryGenericWebServiceOauthConfig]: ...
    @_builtins.property
    @pulumi.getter(name="parameterMapping")
    def parameter_mapping(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="requestBody")
    def request_body(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestHeaders")
    def request_headers(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secretVersionForUsernamePassword")
    def secret_version_for_username_password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="secretVersionsForRequestHeaders")
    def secret_versions_for_request_headers(
        self,
    ) -> Optional[
        Sequence[
            outputs.CxWebhookServiceDirectoryGenericWebServiceSecretVersionsForRequestHeader
        ]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountAuthConfig")
    def service_account_auth_config(
        self,
    ) -> Optional[
        outputs.CxWebhookServiceDirectoryGenericWebServiceServiceAccountAuthConfig
    ]: ...
    @_builtins.property
    @pulumi.getter(name="serviceAgentAuth")
    def service_agent_auth(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="webhookType")
    def webhook_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxWebhookServiceDirectoryGenericWebServiceOauthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        client_id: _builtins.str,
        token_endpoint: _builtins.str,
        client_secret: Optional[_builtins.str] = ...,
        scopes: Optional[Sequence[_builtins.str]] = ...,
        secret_version_for_client_secret: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="secretVersionForClientSecret")
    def secret_version_for_client_secret(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class CxWebhookServiceDirectoryGenericWebServiceSecretVersionsForRequestHeader(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, key: _builtins.str, secret_version: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> _builtins.str: ...

@pulumi.output_type
class CxWebhookServiceDirectoryGenericWebServiceServiceAccountAuthConfig(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, service_account: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str: ...

@pulumi.output_type
class EncryptionSpecEncryptionSpec(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, kms_key: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> _builtins.str: ...

@pulumi.output_type
class EntityTypeEntity(dict):
    def __init__(
        __self__, *, synonyms: Sequence[_builtins.str], value: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def synonyms(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> _builtins.str: ...

@pulumi.output_type
class FulfillmentFeature(dict):
    def __init__(__self__, *, type: _builtins.str) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...

@pulumi.output_type
class FulfillmentGenericWebService(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        uri: _builtins.str,
        password: Optional[_builtins.str] = ...,
        request_headers: Optional[Mapping[str, _builtins.str]] = ...,
        username: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requestHeaders")
    def request_headers(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GeneratorInferenceParameter(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        max_output_tokens: Optional[_builtins.int] = ...,
        temperature: Optional[_builtins.float] = ...,
        top_k: Optional[_builtins.int] = ...,
        top_p: Optional[_builtins.float] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxOutputTokens")
    def max_output_tokens(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]: ...
    @_builtins.property
    @pulumi.getter(name="topK")
    def top_k(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="topP")
    def top_p(self) -> Optional[_builtins.float]: ...

@pulumi.output_type
class GeneratorSummarizationContext(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        few_shot_examples: Optional[
            Sequence[outputs.GeneratorSummarizationContextFewShotExample]
        ] = ...,
        output_language_code: Optional[_builtins.str] = ...,
        summarization_sections: Optional[
            Sequence[outputs.GeneratorSummarizationContextSummarizationSection]
        ] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fewShotExamples")
    def few_shot_examples(
        self,
    ) -> Optional[Sequence[outputs.GeneratorSummarizationContextFewShotExample]]: ...
    @_builtins.property
    @pulumi.getter(name="outputLanguageCode")
    def output_language_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="summarizationSections")
    def summarization_sections(
        self,
    ) -> Optional[
        Sequence[outputs.GeneratorSummarizationContextSummarizationSection]
    ]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GeneratorSummarizationContextFewShotExample(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        output: outputs.GeneratorSummarizationContextFewShotExampleOutput,
        conversation_context: Optional[
            outputs.GeneratorSummarizationContextFewShotExampleConversationContext
        ] = ...,
        extra_info: Optional[Mapping[str, _builtins.str]] = ...,
        summarization_section_list: Optional[
            outputs.GeneratorSummarizationContextFewShotExampleSummarizationSectionList
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def output(self) -> outputs.GeneratorSummarizationContextFewShotExampleOutput: ...
    @_builtins.property
    @pulumi.getter(name="conversationContext")
    def conversation_context(
        self,
    ) -> Optional[
        outputs.GeneratorSummarizationContextFewShotExampleConversationContext
    ]: ...
    @_builtins.property
    @pulumi.getter(name="extraInfo")
    def extra_info(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="summarizationSectionList")
    def summarization_section_list(
        self,
    ) -> Optional[
        outputs.GeneratorSummarizationContextFewShotExampleSummarizationSectionList
    ]: ...

@pulumi.output_type
class GeneratorSummarizationContextFewShotExampleConversationContext(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        message_entries: Optional[
            Sequence[
                outputs.GeneratorSummarizationContextFewShotExampleConversationContextMessageEntry
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="messageEntries")
    def message_entries(
        self,
    ) -> Optional[
        Sequence[
            outputs.GeneratorSummarizationContextFewShotExampleConversationContextMessageEntry
        ]
    ]: ...

@pulumi.output_type
class GeneratorSummarizationContextFewShotExampleConversationContextMessageEntry(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        create_time: Optional[_builtins.str] = ...,
        language_code: Optional[_builtins.str] = ...,
        role: Optional[_builtins.str] = ...,
        text: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GeneratorSummarizationContextFewShotExampleOutput(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        summary_suggestion: Optional[
            outputs.GeneratorSummarizationContextFewShotExampleOutputSummarySuggestion
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="summarySuggestion")
    def summary_suggestion(
        self,
    ) -> Optional[
        outputs.GeneratorSummarizationContextFewShotExampleOutputSummarySuggestion
    ]: ...

@pulumi.output_type
class GeneratorSummarizationContextFewShotExampleOutputSummarySuggestion(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        summary_sections: Sequence[
            outputs.GeneratorSummarizationContextFewShotExampleOutputSummarySuggestionSummarySection
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="summarySections")
    def summary_sections(
        self,
    ) -> Sequence[
        outputs.GeneratorSummarizationContextFewShotExampleOutputSummarySuggestionSummarySection
    ]: ...

@pulumi.output_type
class GeneratorSummarizationContextFewShotExampleOutputSummarySuggestionSummarySection(
    dict
):
    def __init__(
        __self__, *, section: _builtins.str, summary: _builtins.str
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def section(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def summary(self) -> _builtins.str: ...

@pulumi.output_type
class GeneratorSummarizationContextFewShotExampleSummarizationSectionList(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        summarization_sections: Optional[
            Sequence[
                outputs.GeneratorSummarizationContextFewShotExampleSummarizationSectionListSummarizationSection
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="summarizationSections")
    def summarization_sections(
        self,
    ) -> Optional[
        Sequence[
            outputs.GeneratorSummarizationContextFewShotExampleSummarizationSectionListSummarizationSection
        ]
    ]: ...

@pulumi.output_type
class GeneratorSummarizationContextFewShotExampleSummarizationSectionListSummarizationSection(
    dict
):
    def __init__(
        __self__,
        *,
        definition: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def definition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GeneratorSummarizationContextSummarizationSection(dict):
    def __init__(
        __self__,
        *,
        definition: Optional[_builtins.str] = ...,
        key: Optional[_builtins.str] = ...,
        type: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def definition(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class IntentFollowupIntentInfo(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        followup_intent_name: Optional[_builtins.str] = ...,
        parent_followup_intent_name: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="followupIntentName")
    def followup_intent_name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="parentFollowupIntentName")
    def parent_followup_intent_name(self) -> Optional[_builtins.str]: ...
