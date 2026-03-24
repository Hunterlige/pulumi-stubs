

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConversationProfileAutomatedAgentConfigArgs', 'ConversationProfileAutomatedAgentConfigArgsDict', 'ConversationProfileHumanAgentAssistantConfigArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'ConversationProfileHumanAgentHandoffConfigArgs', 'ConversationProfileHumanAgentHandoffConfigArgsDict', ..., ..., 'ConversationProfileLoggingConfigArgs', 'ConversationProfileLoggingConfigArgsDict', ..., ..., ..., ..., 'ConversationProfileNotificationConfigArgs', 'ConversationProfileNotificationConfigArgsDict', 'ConversationProfileSttConfigArgs', 'ConversationProfileSttConfigArgsDict', 'ConversationProfileTtsConfigArgs', 'ConversationProfileTtsConfigArgsDict', 'ConversationProfileTtsConfigVoiceArgs', 'ConversationProfileTtsConfigVoiceArgsDict', 'CxAgentAdvancedSettingsArgs', 'CxAgentAdvancedSettingsArgsDict', ..., ..., 'CxAgentAdvancedSettingsDtmfSettingsArgs', 'CxAgentAdvancedSettingsDtmfSettingsArgsDict', 'CxAgentAdvancedSettingsLoggingSettingsArgs', 'CxAgentAdvancedSettingsLoggingSettingsArgsDict', 'CxAgentAdvancedSettingsSpeechSettingsArgs', 'CxAgentAdvancedSettingsSpeechSettingsArgsDict', 'CxAgentAnswerFeedbackSettingsArgs', 'CxAgentAnswerFeedbackSettingsArgsDict', 'CxAgentClientCertificateSettingsArgs', 'CxAgentClientCertificateSettingsArgsDict', 'CxAgentGenAppBuilderSettingsArgs', 'CxAgentGenAppBuilderSettingsArgsDict', 'CxAgentGitIntegrationSettingsArgs', 'CxAgentGitIntegrationSettingsArgsDict', 'CxAgentGitIntegrationSettingsGithubSettingsArgs', ..., 'CxAgentPersonalizationSettingsArgs', 'CxAgentPersonalizationSettingsArgsDict', 'CxAgentSpeechToTextSettingsArgs', 'CxAgentSpeechToTextSettingsArgsDict', 'CxAgentTextToSpeechSettingsArgs', 'CxAgentTextToSpeechSettingsArgsDict', 'CxEntityTypeEntityArgs', 'CxEntityTypeEntityArgsDict', 'CxEntityTypeExcludedPhraseArgs', 'CxEntityTypeExcludedPhraseArgsDict', 'CxEnvironmentVersionConfigArgs', 'CxEnvironmentVersionConfigArgsDict', 'CxFlowAdvancedSettingsArgs', 'CxFlowAdvancedSettingsArgsDict', ..., ..., 'CxFlowAdvancedSettingsDtmfSettingsArgs', 'CxFlowAdvancedSettingsDtmfSettingsArgsDict', 'CxFlowAdvancedSettingsLoggingSettingsArgs', 'CxFlowAdvancedSettingsLoggingSettingsArgsDict', 'CxFlowAdvancedSettingsSpeechSettingsArgs', 'CxFlowAdvancedSettingsSpeechSettingsArgsDict', 'CxFlowEventHandlerArgs', 'CxFlowEventHandlerArgsDict', 'CxFlowEventHandlerTriggerFulfillmentArgs', 'CxFlowEventHandlerTriggerFulfillmentArgsDict', ..., ..., 'CxFlowEventHandlerTriggerFulfillmentMessageArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'CxFlowKnowledgeConnectorSettingsArgs', 'CxFlowKnowledgeConnectorSettingsArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'CxFlowNluSettingsArgs', 'CxFlowNluSettingsArgsDict', 'CxFlowTransitionRouteArgs', 'CxFlowTransitionRouteArgsDict', 'CxFlowTransitionRouteTriggerFulfillmentArgs', 'CxFlowTransitionRouteTriggerFulfillmentArgsDict', ..., ..., 'CxFlowTransitionRouteTriggerFulfillmentMessageArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'CxGenerativeSettingsFallbackSettingsArgs', 'CxGenerativeSettingsFallbackSettingsArgsDict', ..., ..., 'CxGenerativeSettingsGenerativeSafetySettingsArgs', ..., ..., ..., 'CxGenerativeSettingsKnowledgeConnectorSettingsArgs', ..., 'CxGenerativeSettingsLlmModelSettingsArgs', 'CxGenerativeSettingsLlmModelSettingsArgsDict', 'CxGeneratorLlmModelSettingsArgs', 'CxGeneratorLlmModelSettingsArgsDict', 'CxGeneratorModelParameterArgs', 'CxGeneratorModelParameterArgsDict', 'CxGeneratorPlaceholderArgs', 'CxGeneratorPlaceholderArgsDict', 'CxGeneratorPromptTextArgs', 'CxGeneratorPromptTextArgsDict', 'CxIntentParameterArgs', 'CxIntentParameterArgsDict', 'CxIntentTrainingPhraseArgs', 'CxIntentTrainingPhraseArgsDict', 'CxIntentTrainingPhrasePartArgs', 'CxIntentTrainingPhrasePartArgsDict', 'CxPageAdvancedSettingsArgs', 'CxPageAdvancedSettingsArgsDict', 'CxPageAdvancedSettingsDtmfSettingsArgs', 'CxPageAdvancedSettingsDtmfSettingsArgsDict', 'CxPageEntryFulfillmentArgs', 'CxPageEntryFulfillmentArgsDict', 'CxPageEntryFulfillmentConditionalCaseArgs', 'CxPageEntryFulfillmentConditionalCaseArgsDict', 'CxPageEntryFulfillmentMessageArgs', 'CxPageEntryFulfillmentMessageArgsDict', ..., ..., 'CxPageEntryFulfillmentMessageLiveAgentHandoffArgs', ..., 'CxPageEntryFulfillmentMessageOutputAudioTextArgs', ..., 'CxPageEntryFulfillmentMessagePlayAudioArgs', 'CxPageEntryFulfillmentMessagePlayAudioArgsDict', ..., ..., 'CxPageEntryFulfillmentMessageTextArgs', 'CxPageEntryFulfillmentMessageTextArgsDict', 'CxPageEntryFulfillmentSetParameterActionArgs', 'CxPageEntryFulfillmentSetParameterActionArgsDict', 'CxPageEventHandlerArgs', 'CxPageEventHandlerArgsDict', 'CxPageEventHandlerTriggerFulfillmentArgs', 'CxPageEventHandlerTriggerFulfillmentArgsDict', ..., ..., 'CxPageEventHandlerTriggerFulfillmentMessageArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'CxPageFormArgs', 'CxPageFormArgsDict', 'CxPageFormParameterArgs', 'CxPageFormParameterArgsDict', 'CxPageFormParameterAdvancedSettingsArgs', 'CxPageFormParameterAdvancedSettingsArgsDict', ..., ..., 'CxPageFormParameterFillBehaviorArgs', 'CxPageFormParameterFillBehaviorArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'CxPageKnowledgeConnectorSettingsArgs', 'CxPageKnowledgeConnectorSettingsArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'CxPageTransitionRouteArgs', 'CxPageTransitionRouteArgsDict', 'CxPageTransitionRouteTriggerFulfillmentArgs', 'CxPageTransitionRouteTriggerFulfillmentArgsDict', ..., ..., 'CxPageTransitionRouteTriggerFulfillmentMessageArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'CxPlaybookInstructionArgs', 'CxPlaybookInstructionArgsDict', 'CxPlaybookInstructionStepArgs', 'CxPlaybookInstructionStepArgsDict', 'CxPlaybookLlmModelSettingsArgs', 'CxPlaybookLlmModelSettingsArgsDict', 'CxSecuritySettingsAudioExportSettingsArgs', 'CxSecuritySettingsAudioExportSettingsArgsDict', 'CxSecuritySettingsInsightsExportSettingsArgs', 'CxSecuritySettingsInsightsExportSettingsArgsDict', 'CxTestCaseLastTestResultArgs', 'CxTestCaseLastTestResultArgsDict', 'CxTestCaseLastTestResultConversationTurnArgs', 'CxTestCaseLastTestResultConversationTurnArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'CxTestCaseTestCaseConversationTurnArgs', 'CxTestCaseTestCaseConversationTurnArgsDict', 'CxTestCaseTestCaseConversationTurnUserInputArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'CxTestCaseTestConfigArgs', 'CxTestCaseTestConfigArgsDict', 'CxToolConnectorSpecArgs', 'CxToolConnectorSpecArgsDict', 'CxToolConnectorSpecActionArgs', 'CxToolConnectorSpecActionArgsDict', 'CxToolConnectorSpecActionEntityOperationArgs', 'CxToolConnectorSpecActionEntityOperationArgsDict', 'CxToolConnectorSpecEndUserAuthConfigArgs', 'CxToolConnectorSpecEndUserAuthConfigArgsDict', ..., ..., ..., ..., 'CxToolDataStoreSpecArgs', 'CxToolDataStoreSpecArgsDict', 'CxToolDataStoreSpecDataStoreConnectionArgs', 'CxToolDataStoreSpecDataStoreConnectionArgsDict', 'CxToolDataStoreSpecFallbackPromptArgs', 'CxToolDataStoreSpecFallbackPromptArgsDict', 'CxToolFunctionSpecArgs', 'CxToolFunctionSpecArgsDict', 'CxToolOpenApiSpecArgs', 'CxToolOpenApiSpecArgsDict', 'CxToolOpenApiSpecAuthenticationArgs', 'CxToolOpenApiSpecAuthenticationArgsDict', 'CxToolOpenApiSpecAuthenticationApiKeyConfigArgs', ..., ..., ..., 'CxToolOpenApiSpecAuthenticationOauthConfigArgs', 'CxToolOpenApiSpecAuthenticationOauthConfigArgsDict', ..., ..., 'CxToolOpenApiSpecServiceDirectoryConfigArgs', 'CxToolOpenApiSpecServiceDirectoryConfigArgsDict', 'CxToolOpenApiSpecTlsConfigArgs', 'CxToolOpenApiSpecTlsConfigArgsDict', 'CxToolOpenApiSpecTlsConfigCaCertArgs', 'CxToolOpenApiSpecTlsConfigCaCertArgsDict', 'CxToolVersionToolArgs', 'CxToolVersionToolArgsDict', 'CxToolVersionToolConnectorSpecArgs', 'CxToolVersionToolConnectorSpecArgsDict', 'CxToolVersionToolConnectorSpecActionArgs', 'CxToolVersionToolConnectorSpecActionArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., 'CxToolVersionToolDataStoreSpecArgs', 'CxToolVersionToolDataStoreSpecArgsDict', ..., ..., 'CxToolVersionToolDataStoreSpecFallbackPromptArgs', ..., 'CxToolVersionToolFunctionSpecArgs', 'CxToolVersionToolFunctionSpecArgsDict', 'CxToolVersionToolOpenApiSpecArgs', 'CxToolVersionToolOpenApiSpecArgsDict', 'CxToolVersionToolOpenApiSpecAuthenticationArgs', 'CxToolVersionToolOpenApiSpecAuthenticationArgsDict', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'CxToolVersionToolOpenApiSpecTlsConfigArgs', 'CxToolVersionToolOpenApiSpecTlsConfigArgsDict', 'CxToolVersionToolOpenApiSpecTlsConfigCaCertArgs', ..., 'CxVersionNluSettingArgs', 'CxVersionNluSettingArgsDict', 'CxWebhookGenericWebServiceArgs', 'CxWebhookGenericWebServiceArgsDict', 'CxWebhookGenericWebServiceOauthConfigArgs', 'CxWebhookGenericWebServiceOauthConfigArgsDict', ..., ..., ..., ..., 'CxWebhookServiceDirectoryArgs', 'CxWebhookServiceDirectoryArgsDict', 'CxWebhookServiceDirectoryGenericWebServiceArgs', 'CxWebhookServiceDirectoryGenericWebServiceArgsDict', ..., ..., ..., ..., ..., ..., 'EncryptionSpecEncryptionSpecArgs', 'EncryptionSpecEncryptionSpecArgsDict', 'EntityTypeEntityArgs', 'EntityTypeEntityArgsDict', 'FulfillmentFeatureArgs', 'FulfillmentFeatureArgsDict', 'FulfillmentGenericWebServiceArgs', 'FulfillmentGenericWebServiceArgsDict', 'GeneratorInferenceParameterArgs', 'GeneratorInferenceParameterArgsDict', 'GeneratorSummarizationContextArgs', 'GeneratorSummarizationContextArgsDict', 'GeneratorSummarizationContextFewShotExampleArgs', ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., ..., 'IntentFollowupIntentInfoArgs', 'IntentFollowupIntentInfoArgsDict']
class ConversationProfileAutomatedAgentConfigArgsDict(TypedDict):
    agent: pulumi.Input[_builtins.str]
    session_ttl: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConversationProfileAutomatedAgentConfigArgs:
    def __init__(__self__, *, agent: pulumi.Input[_builtins.str], session_ttl: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def agent(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @agent.setter
    def agent(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionTtl")
    def session_ttl(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_ttl.setter
    def session_ttl(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigArgsDict(TypedDict):
    end_user_suggestion_config: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigArgsDict]]
    human_agent_suggestion_config: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigArgsDict]]
    message_analysis_config: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigMessageAnalysisConfigArgsDict]]
    notification_config: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigNotificationConfigArgsDict]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigArgs:
    def __init__(__self__, *, end_user_suggestion_config: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigArgs]] = ..., human_agent_suggestion_config: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigArgs]] = ..., message_analysis_config: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigMessageAnalysisConfigArgs]] = ..., notification_config: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigNotificationConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endUserSuggestionConfig")
    def end_user_suggestion_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigArgs]]:
        
        ...
    
    @end_user_suggestion_config.setter
    def end_user_suggestion_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanAgentSuggestionConfig")
    def human_agent_suggestion_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigArgs]]:
        
        ...
    
    @human_agent_suggestion_config.setter
    def human_agent_suggestion_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageAnalysisConfig")
    def message_analysis_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigMessageAnalysisConfigArgs]]:
        
        ...
    
    @message_analysis_config.setter
    def message_analysis_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigMessageAnalysisConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigNotificationConfigArgs]]:
        
        ...
    
    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigNotificationConfigArgs]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigArgsDict(TypedDict):
    disable_high_latency_features_sync_delivery: NotRequired[pulumi.Input[_builtins.bool]]
    feature_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigArgsDict]]]]
    generators: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    group_suggestion_responses: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigArgs:
    def __init__(__self__, *, disable_high_latency_features_sync_delivery: Optional[pulumi.Input[_builtins.bool]] = ..., feature_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigArgs]]]] = ..., generators: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., group_suggestion_responses: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableHighLatencyFeaturesSyncDelivery")
    def disable_high_latency_features_sync_delivery(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_high_latency_features_sync_delivery.setter
    def disable_high_latency_features_sync_delivery(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureConfigs")
    def feature_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigArgs]]]]:
        
        ...
    
    @feature_configs.setter
    def feature_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def generators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @generators.setter
    def generators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupSuggestionResponses")
    def group_suggestion_responses(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @group_suggestion_responses.setter
    def group_suggestion_responses(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigArgsDict(TypedDict):
    conversation_model_config: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationModelConfigArgsDict]]
    conversation_process_config: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationProcessConfigArgsDict]]
    disable_agent_query_logging: NotRequired[pulumi.Input[_builtins.bool]]
    enable_conversation_augmented_query: NotRequired[pulumi.Input[_builtins.bool]]
    enable_event_based_suggestion: NotRequired[pulumi.Input[_builtins.bool]]
    enable_query_suggestion_only: NotRequired[pulumi.Input[_builtins.bool]]
    enable_query_suggestion_when_no_answer: NotRequired[pulumi.Input[_builtins.bool]]
    query_config: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigArgsDict]]
    suggestion_feature: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionFeatureArgsDict]]
    suggestion_trigger_settings: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionTriggerSettingsArgsDict]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigArgs:
    def __init__(__self__, *, conversation_model_config: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationModelConfigArgs]] = ..., conversation_process_config: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationProcessConfigArgs]] = ..., disable_agent_query_logging: Optional[pulumi.Input[_builtins.bool]] = ..., enable_conversation_augmented_query: Optional[pulumi.Input[_builtins.bool]] = ..., enable_event_based_suggestion: Optional[pulumi.Input[_builtins.bool]] = ..., enable_query_suggestion_only: Optional[pulumi.Input[_builtins.bool]] = ..., enable_query_suggestion_when_no_answer: Optional[pulumi.Input[_builtins.bool]] = ..., query_config: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigArgs]] = ..., suggestion_feature: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionFeatureArgs]] = ..., suggestion_trigger_settings: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionTriggerSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationModelConfig")
    def conversation_model_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationModelConfigArgs]]:
        
        ...
    
    @conversation_model_config.setter
    def conversation_model_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationModelConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationProcessConfig")
    def conversation_process_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationProcessConfigArgs]]:
        
        ...
    
    @conversation_process_config.setter
    def conversation_process_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationProcessConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableAgentQueryLogging")
    def disable_agent_query_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_agent_query_logging.setter
    def disable_agent_query_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableConversationAugmentedQuery")
    def enable_conversation_augmented_query(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_conversation_augmented_query.setter
    def enable_conversation_augmented_query(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEventBasedSuggestion")
    def enable_event_based_suggestion(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_event_based_suggestion.setter
    def enable_event_based_suggestion(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableQuerySuggestionOnly")
    def enable_query_suggestion_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_query_suggestion_only.setter
    def enable_query_suggestion_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableQuerySuggestionWhenNoAnswer")
    def enable_query_suggestion_when_no_answer(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_query_suggestion_when_no_answer.setter
    def enable_query_suggestion_when_no_answer(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryConfig")
    def query_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigArgs]]:
        
        ...
    
    @query_config.setter
    def query_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="suggestionFeature")
    def suggestion_feature(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionFeatureArgs]]:
        
        ...
    
    @suggestion_feature.setter
    def suggestion_feature(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionFeatureArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="suggestionTriggerSettings")
    def suggestion_trigger_settings(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionTriggerSettingsArgs]]:
        
        ...
    
    @suggestion_trigger_settings.setter
    def suggestion_trigger_settings(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionTriggerSettingsArgs]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationModelConfigArgsDict(TypedDict):
    baseline_model_version: NotRequired[pulumi.Input[_builtins.str]]
    model: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationModelConfigArgs:
    def __init__(__self__, *, baseline_model_version: Optional[pulumi.Input[_builtins.str]] = ..., model: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineModelVersion")
    def baseline_model_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @baseline_model_version.setter
    def baseline_model_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationProcessConfigArgsDict(TypedDict):
    recent_sentences_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigConversationProcessConfigArgs:
    def __init__(__self__, *, recent_sentences_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recentSentencesCount")
    def recent_sentences_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @recent_sentences_count.setter
    def recent_sentences_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigArgsDict(TypedDict):
    confidence_threshold: NotRequired[pulumi.Input[_builtins.float]]
    context_filter_settings: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigContextFilterSettingsArgsDict]]
    dialogflow_query_source: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceArgsDict]]
    document_query_source: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDocumentQuerySourceArgsDict]]
    knowledge_base_query_source: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigKnowledgeBaseQuerySourceArgsDict]]
    max_results: NotRequired[pulumi.Input[_builtins.int]]
    sections: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigSectionsArgsDict]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigArgs:
    def __init__(__self__, *, confidence_threshold: Optional[pulumi.Input[_builtins.float]] = ..., context_filter_settings: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigContextFilterSettingsArgs]] = ..., dialogflow_query_source: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceArgs]] = ..., document_query_source: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDocumentQuerySourceArgs]] = ..., knowledge_base_query_source: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigKnowledgeBaseQuerySourceArgs]] = ..., max_results: Optional[pulumi.Input[_builtins.int]] = ..., sections: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigSectionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidenceThreshold")
    def confidence_threshold(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @confidence_threshold.setter
    def confidence_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contextFilterSettings")
    def context_filter_settings(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigContextFilterSettingsArgs]]:
        
        ...
    
    @context_filter_settings.setter
    def context_filter_settings(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigContextFilterSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogflowQuerySource")
    def dialogflow_query_source(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceArgs]]:
        
        ...
    
    @dialogflow_query_source.setter
    def dialogflow_query_source(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentQuerySource")
    def document_query_source(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDocumentQuerySourceArgs]]:
        
        ...
    
    @document_query_source.setter
    def document_query_source(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDocumentQuerySourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeBaseQuerySource")
    def knowledge_base_query_source(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigKnowledgeBaseQuerySourceArgs]]:
        
        ...
    
    @knowledge_base_query_source.setter
    def knowledge_base_query_source(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigKnowledgeBaseQuerySourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxResults")
    def max_results(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_results.setter
    def max_results(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sections(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigSectionsArgs]]:
        
        ...
    
    @sections.setter
    def sections(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigSectionsArgs]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigContextFilterSettingsArgsDict(TypedDict):
    drop_handoff_messages: NotRequired[pulumi.Input[_builtins.bool]]
    drop_ivr_messages: NotRequired[pulumi.Input[_builtins.bool]]
    drop_virtual_agent_messages: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigContextFilterSettingsArgs:
    def __init__(__self__, *, drop_handoff_messages: Optional[pulumi.Input[_builtins.bool]] = ..., drop_ivr_messages: Optional[pulumi.Input[_builtins.bool]] = ..., drop_virtual_agent_messages: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dropHandoffMessages")
    def drop_handoff_messages(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @drop_handoff_messages.setter
    def drop_handoff_messages(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dropIvrMessages")
    def drop_ivr_messages(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @drop_ivr_messages.setter
    def drop_ivr_messages(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dropVirtualAgentMessages")
    def drop_virtual_agent_messages(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @drop_virtual_agent_messages.setter
    def drop_virtual_agent_messages(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceArgsDict(TypedDict):
    agent: pulumi.Input[_builtins.str]
    human_agent_side_config: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfigArgsDict]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceArgs:
    def __init__(__self__, *, agent: pulumi.Input[_builtins.str], human_agent_side_config: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def agent(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @agent.setter
    def agent(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanAgentSideConfig")
    def human_agent_side_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfigArgs]]:
        
        ...
    
    @human_agent_side_config.setter
    def human_agent_side_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfigArgs]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfigArgsDict(TypedDict):
    agent: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfigArgs:
    def __init__(__self__, *, agent: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def agent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent.setter
    def agent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDocumentQuerySourceArgsDict(TypedDict):
    documents: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigDocumentQuerySourceArgs:
    def __init__(__self__, *, documents: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def documents(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @documents.setter
    def documents(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigKnowledgeBaseQuerySourceArgsDict(TypedDict):
    knowledge_bases: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigKnowledgeBaseQuerySourceArgs:
    def __init__(__self__, *, knowledge_bases: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeBases")
    def knowledge_bases(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @knowledge_bases.setter
    def knowledge_bases(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigSectionsArgsDict(TypedDict):
    section_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigQueryConfigSectionsArgs:
    def __init__(__self__, *, section_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sectionTypes")
    def section_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @section_types.setter
    def section_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionFeatureArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionFeatureArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionTriggerSettingsArgsDict(TypedDict):
    no_small_talk: NotRequired[pulumi.Input[_builtins.bool]]
    only_end_user: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigEndUserSuggestionConfigFeatureConfigSuggestionTriggerSettingsArgs:
    def __init__(__self__, *, no_small_talk: Optional[pulumi.Input[_builtins.bool]] = ..., only_end_user: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noSmallTalk")
    def no_small_talk(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @no_small_talk.setter
    def no_small_talk(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onlyEndUser")
    def only_end_user(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @only_end_user.setter
    def only_end_user(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigArgsDict(TypedDict):
    disable_high_latency_features_sync_delivery: NotRequired[pulumi.Input[_builtins.bool]]
    feature_configs: NotRequired[pulumi.Input[Sequence[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigArgsDict]]]]
    generators: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    group_suggestion_responses: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigArgs:
    def __init__(__self__, *, disable_high_latency_features_sync_delivery: Optional[pulumi.Input[_builtins.bool]] = ..., feature_configs: Optional[pulumi.Input[Sequence[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigArgs]]]] = ..., generators: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., group_suggestion_responses: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableHighLatencyFeaturesSyncDelivery")
    def disable_high_latency_features_sync_delivery(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_high_latency_features_sync_delivery.setter
    def disable_high_latency_features_sync_delivery(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="featureConfigs")
    def feature_configs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigArgs]]]]:
        
        ...
    
    @feature_configs.setter
    def feature_configs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def generators(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @generators.setter
    def generators(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="groupSuggestionResponses")
    def group_suggestion_responses(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @group_suggestion_responses.setter
    def group_suggestion_responses(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigArgsDict(TypedDict):
    conversation_model_config: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationModelConfigArgsDict]]
    conversation_process_config: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationProcessConfigArgsDict]]
    disable_agent_query_logging: NotRequired[pulumi.Input[_builtins.bool]]
    enable_conversation_augmented_query: NotRequired[pulumi.Input[_builtins.bool]]
    enable_event_based_suggestion: NotRequired[pulumi.Input[_builtins.bool]]
    enable_query_suggestion_only: NotRequired[pulumi.Input[_builtins.bool]]
    enable_query_suggestion_when_no_answer: NotRequired[pulumi.Input[_builtins.bool]]
    query_config: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigArgsDict]]
    suggestion_feature: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionFeatureArgsDict]]
    suggestion_trigger_settings: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionTriggerSettingsArgsDict]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigArgs:
    def __init__(__self__, *, conversation_model_config: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationModelConfigArgs]] = ..., conversation_process_config: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationProcessConfigArgs]] = ..., disable_agent_query_logging: Optional[pulumi.Input[_builtins.bool]] = ..., enable_conversation_augmented_query: Optional[pulumi.Input[_builtins.bool]] = ..., enable_event_based_suggestion: Optional[pulumi.Input[_builtins.bool]] = ..., enable_query_suggestion_only: Optional[pulumi.Input[_builtins.bool]] = ..., enable_query_suggestion_when_no_answer: Optional[pulumi.Input[_builtins.bool]] = ..., query_config: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigArgs]] = ..., suggestion_feature: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionFeatureArgs]] = ..., suggestion_trigger_settings: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionTriggerSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationModelConfig")
    def conversation_model_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationModelConfigArgs]]:
        
        ...
    
    @conversation_model_config.setter
    def conversation_model_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationModelConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationProcessConfig")
    def conversation_process_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationProcessConfigArgs]]:
        
        ...
    
    @conversation_process_config.setter
    def conversation_process_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationProcessConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableAgentQueryLogging")
    def disable_agent_query_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_agent_query_logging.setter
    def disable_agent_query_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableConversationAugmentedQuery")
    def enable_conversation_augmented_query(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_conversation_augmented_query.setter
    def enable_conversation_augmented_query(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEventBasedSuggestion")
    def enable_event_based_suggestion(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_event_based_suggestion.setter
    def enable_event_based_suggestion(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableQuerySuggestionOnly")
    def enable_query_suggestion_only(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_query_suggestion_only.setter
    def enable_query_suggestion_only(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableQuerySuggestionWhenNoAnswer")
    def enable_query_suggestion_when_no_answer(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_query_suggestion_when_no_answer.setter
    def enable_query_suggestion_when_no_answer(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="queryConfig")
    def query_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigArgs]]:
        
        ...
    
    @query_config.setter
    def query_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="suggestionFeature")
    def suggestion_feature(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionFeatureArgs]]:
        
        ...
    
    @suggestion_feature.setter
    def suggestion_feature(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionFeatureArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="suggestionTriggerSettings")
    def suggestion_trigger_settings(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionTriggerSettingsArgs]]:
        
        ...
    
    @suggestion_trigger_settings.setter
    def suggestion_trigger_settings(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionTriggerSettingsArgs]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationModelConfigArgsDict(TypedDict):
    baseline_model_version: NotRequired[pulumi.Input[_builtins.str]]
    model: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationModelConfigArgs:
    def __init__(__self__, *, baseline_model_version: Optional[pulumi.Input[_builtins.str]] = ..., model: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="baselineModelVersion")
    def baseline_model_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @baseline_model_version.setter
    def baseline_model_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationProcessConfigArgsDict(TypedDict):
    recent_sentences_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigConversationProcessConfigArgs:
    def __init__(__self__, *, recent_sentences_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="recentSentencesCount")
    def recent_sentences_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @recent_sentences_count.setter
    def recent_sentences_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigArgsDict(TypedDict):
    confidence_threshold: NotRequired[pulumi.Input[_builtins.float]]
    context_filter_settings: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigContextFilterSettingsArgsDict]]
    dialogflow_query_source: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceArgsDict]]
    max_results: NotRequired[pulumi.Input[_builtins.int]]
    sections: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigSectionsArgsDict]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigArgs:
    def __init__(__self__, *, confidence_threshold: Optional[pulumi.Input[_builtins.float]] = ..., context_filter_settings: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigContextFilterSettingsArgs]] = ..., dialogflow_query_source: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceArgs]] = ..., max_results: Optional[pulumi.Input[_builtins.int]] = ..., sections: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigSectionsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="confidenceThreshold")
    def confidence_threshold(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @confidence_threshold.setter
    def confidence_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contextFilterSettings")
    def context_filter_settings(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigContextFilterSettingsArgs]]:
        
        ...
    
    @context_filter_settings.setter
    def context_filter_settings(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigContextFilterSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dialogflowQuerySource")
    def dialogflow_query_source(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceArgs]]:
        
        ...
    
    @dialogflow_query_source.setter
    def dialogflow_query_source(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxResults")
    def max_results(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_results.setter
    def max_results(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def sections(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigSectionsArgs]]:
        
        ...
    
    @sections.setter
    def sections(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigSectionsArgs]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigContextFilterSettingsArgsDict(TypedDict):
    drop_handoff_messages: NotRequired[pulumi.Input[_builtins.bool]]
    drop_ivr_messages: NotRequired[pulumi.Input[_builtins.bool]]
    drop_virtual_agent_messages: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigContextFilterSettingsArgs:
    def __init__(__self__, *, drop_handoff_messages: Optional[pulumi.Input[_builtins.bool]] = ..., drop_ivr_messages: Optional[pulumi.Input[_builtins.bool]] = ..., drop_virtual_agent_messages: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dropHandoffMessages")
    def drop_handoff_messages(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @drop_handoff_messages.setter
    def drop_handoff_messages(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dropIvrMessages")
    def drop_ivr_messages(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @drop_ivr_messages.setter
    def drop_ivr_messages(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dropVirtualAgentMessages")
    def drop_virtual_agent_messages(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @drop_virtual_agent_messages.setter
    def drop_virtual_agent_messages(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceArgsDict(TypedDict):
    agent: pulumi.Input[_builtins.str]
    human_agent_side_config: NotRequired[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfigArgsDict]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceArgs:
    def __init__(__self__, *, agent: pulumi.Input[_builtins.str], human_agent_side_config: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def agent(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @agent.setter
    def agent(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanAgentSideConfig")
    def human_agent_side_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfigArgs]]:
        
        ...
    
    @human_agent_side_config.setter
    def human_agent_side_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfigArgs]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfigArgsDict(TypedDict):
    agent: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigDialogflowQuerySourceHumanAgentSideConfigArgs:
    def __init__(__self__, *, agent: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def agent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent.setter
    def agent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigSectionsArgsDict(TypedDict):
    section_types: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigQueryConfigSectionsArgs:
    def __init__(__self__, *, section_types: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sectionTypes")
    def section_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @section_types.setter
    def section_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionFeatureArgsDict(TypedDict):
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionFeatureArgs:
    def __init__(__self__, *, type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionTriggerSettingsArgsDict(TypedDict):
    no_small_talk: NotRequired[pulumi.Input[_builtins.bool]]
    only_end_user: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigHumanAgentSuggestionConfigFeatureConfigSuggestionTriggerSettingsArgs:
    def __init__(__self__, *, no_small_talk: Optional[pulumi.Input[_builtins.bool]] = ..., only_end_user: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="noSmallTalk")
    def no_small_talk(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @no_small_talk.setter
    def no_small_talk(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="onlyEndUser")
    def only_end_user(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @only_end_user.setter
    def only_end_user(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigMessageAnalysisConfigArgsDict(TypedDict):
    enable_entity_extraction: NotRequired[pulumi.Input[_builtins.bool]]
    enable_sentiment_analysis: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigMessageAnalysisConfigArgs:
    def __init__(__self__, *, enable_entity_extraction: Optional[pulumi.Input[_builtins.bool]] = ..., enable_sentiment_analysis: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableEntityExtraction")
    def enable_entity_extraction(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_entity_extraction.setter
    def enable_entity_extraction(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSentimentAnalysis")
    def enable_sentiment_analysis(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_sentiment_analysis.setter
    def enable_sentiment_analysis(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConversationProfileHumanAgentAssistantConfigNotificationConfigArgsDict(TypedDict):
    message_format: NotRequired[pulumi.Input[_builtins.str]]
    topic: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConversationProfileHumanAgentAssistantConfigNotificationConfigArgs:
    def __init__(__self__, *, message_format: Optional[pulumi.Input[_builtins.str]] = ..., topic: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_format.setter
    def message_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConversationProfileHumanAgentHandoffConfigArgsDict(TypedDict):
    live_person_config: NotRequired[pulumi.Input[ConversationProfileHumanAgentHandoffConfigLivePersonConfigArgsDict]]


@pulumi.input_type
class ConversationProfileHumanAgentHandoffConfigArgs:
    def __init__(__self__, *, live_person_config: Optional[pulumi.Input[ConversationProfileHumanAgentHandoffConfigLivePersonConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="livePersonConfig")
    def live_person_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentHandoffConfigLivePersonConfigArgs]]:
        
        ...
    
    @live_person_config.setter
    def live_person_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentHandoffConfigLivePersonConfigArgs]]): # -> None:
        ...
    


class ConversationProfileHumanAgentHandoffConfigLivePersonConfigArgsDict(TypedDict):
    account_number: pulumi.Input[_builtins.str]


@pulumi.input_type
class ConversationProfileHumanAgentHandoffConfigLivePersonConfigArgs:
    def __init__(__self__, *, account_number: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accountNumber")
    def account_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @account_number.setter
    def account_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class ConversationProfileLoggingConfigArgsDict(TypedDict):
    enable_stackdriver_logging: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConversationProfileLoggingConfigArgs:
    def __init__(__self__, *, enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_stackdriver_logging.setter
    def enable_stackdriver_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConversationProfileNewMessageEventNotificationConfigArgsDict(TypedDict):
    message_format: NotRequired[pulumi.Input[_builtins.str]]
    topic: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConversationProfileNewMessageEventNotificationConfigArgs:
    def __init__(__self__, *, message_format: Optional[pulumi.Input[_builtins.str]] = ..., topic: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_format.setter
    def message_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConversationProfileNewRecognitionResultNotificationConfigArgsDict(TypedDict):
    message_format: NotRequired[pulumi.Input[_builtins.str]]
    topic: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConversationProfileNewRecognitionResultNotificationConfigArgs:
    def __init__(__self__, *, message_format: Optional[pulumi.Input[_builtins.str]] = ..., topic: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_format.setter
    def message_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConversationProfileNotificationConfigArgsDict(TypedDict):
    message_format: NotRequired[pulumi.Input[_builtins.str]]
    topic: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConversationProfileNotificationConfigArgs:
    def __init__(__self__, *, message_format: Optional[pulumi.Input[_builtins.str]] = ..., topic: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageFormat")
    def message_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message_format.setter
    def message_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def topic(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @topic.setter
    def topic(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class ConversationProfileSttConfigArgsDict(TypedDict):
    audio_encoding: NotRequired[pulumi.Input[_builtins.str]]
    enable_word_info: NotRequired[pulumi.Input[_builtins.bool]]
    language_code: NotRequired[pulumi.Input[_builtins.str]]
    model: NotRequired[pulumi.Input[_builtins.str]]
    sample_rate_hertz: NotRequired[pulumi.Input[_builtins.int]]
    speech_model_variant: NotRequired[pulumi.Input[_builtins.str]]
    use_timeout_based_endpointing: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class ConversationProfileSttConfigArgs:
    def __init__(__self__, *, audio_encoding: Optional[pulumi.Input[_builtins.str]] = ..., enable_word_info: Optional[pulumi.Input[_builtins.bool]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., model: Optional[pulumi.Input[_builtins.str]] = ..., sample_rate_hertz: Optional[pulumi.Input[_builtins.int]] = ..., speech_model_variant: Optional[pulumi.Input[_builtins.str]] = ..., use_timeout_based_endpointing: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioEncoding")
    def audio_encoding(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @audio_encoding.setter
    def audio_encoding(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableWordInfo")
    def enable_word_info(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_word_info.setter
    def enable_word_info(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sampleRateHertz")
    def sample_rate_hertz(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @sample_rate_hertz.setter
    def sample_rate_hertz(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="speechModelVariant")
    def speech_model_variant(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @speech_model_variant.setter
    def speech_model_variant(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useTimeoutBasedEndpointing")
    def use_timeout_based_endpointing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_timeout_based_endpointing.setter
    def use_timeout_based_endpointing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class ConversationProfileTtsConfigArgsDict(TypedDict):
    effects_profile_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    pitch: NotRequired[pulumi.Input[_builtins.float]]
    speaking_rate: NotRequired[pulumi.Input[_builtins.float]]
    voice: NotRequired[pulumi.Input[ConversationProfileTtsConfigVoiceArgsDict]]
    volume_gain_db: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class ConversationProfileTtsConfigArgs:
    def __init__(__self__, *, effects_profile_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., pitch: Optional[pulumi.Input[_builtins.float]] = ..., speaking_rate: Optional[pulumi.Input[_builtins.float]] = ..., voice: Optional[pulumi.Input[ConversationProfileTtsConfigVoiceArgs]] = ..., volume_gain_db: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="effectsProfileIds")
    def effects_profile_ids(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @effects_profile_ids.setter
    def effects_profile_ids(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def pitch(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @pitch.setter
    def pitch(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="speakingRate")
    def speaking_rate(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @speaking_rate.setter
    def speaking_rate(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def voice(self) -> Optional[pulumi.Input[ConversationProfileTtsConfigVoiceArgs]]:
        
        ...
    
    @voice.setter
    def voice(self, value: Optional[pulumi.Input[ConversationProfileTtsConfigVoiceArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeGainDb")
    def volume_gain_db(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @volume_gain_db.setter
    def volume_gain_db(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class ConversationProfileTtsConfigVoiceArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    ssml_gender: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class ConversationProfileTtsConfigVoiceArgs:
    def __init__(__self__, *, name: Optional[pulumi.Input[_builtins.str]] = ..., ssml_gender: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ssmlGender")
    def ssml_gender(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssml_gender.setter
    def ssml_gender(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxAgentAdvancedSettingsArgsDict(TypedDict):
    audio_export_gcs_destination: NotRequired[pulumi.Input[CxAgentAdvancedSettingsAudioExportGcsDestinationArgsDict]]
    dtmf_settings: NotRequired[pulumi.Input[CxAgentAdvancedSettingsDtmfSettingsArgsDict]]
    logging_settings: NotRequired[pulumi.Input[CxAgentAdvancedSettingsLoggingSettingsArgsDict]]
    speech_settings: NotRequired[pulumi.Input[CxAgentAdvancedSettingsSpeechSettingsArgsDict]]


@pulumi.input_type
class CxAgentAdvancedSettingsArgs:
    def __init__(__self__, *, audio_export_gcs_destination: Optional[pulumi.Input[CxAgentAdvancedSettingsAudioExportGcsDestinationArgs]] = ..., dtmf_settings: Optional[pulumi.Input[CxAgentAdvancedSettingsDtmfSettingsArgs]] = ..., logging_settings: Optional[pulumi.Input[CxAgentAdvancedSettingsLoggingSettingsArgs]] = ..., speech_settings: Optional[pulumi.Input[CxAgentAdvancedSettingsSpeechSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioExportGcsDestination")
    def audio_export_gcs_destination(self) -> Optional[pulumi.Input[CxAgentAdvancedSettingsAudioExportGcsDestinationArgs]]:
        
        ...
    
    @audio_export_gcs_destination.setter
    def audio_export_gcs_destination(self, value: Optional[pulumi.Input[CxAgentAdvancedSettingsAudioExportGcsDestinationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dtmfSettings")
    def dtmf_settings(self) -> Optional[pulumi.Input[CxAgentAdvancedSettingsDtmfSettingsArgs]]:
        
        ...
    
    @dtmf_settings.setter
    def dtmf_settings(self, value: Optional[pulumi.Input[CxAgentAdvancedSettingsDtmfSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingSettings")
    def logging_settings(self) -> Optional[pulumi.Input[CxAgentAdvancedSettingsLoggingSettingsArgs]]:
        
        ...
    
    @logging_settings.setter
    def logging_settings(self, value: Optional[pulumi.Input[CxAgentAdvancedSettingsLoggingSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="speechSettings")
    def speech_settings(self) -> Optional[pulumi.Input[CxAgentAdvancedSettingsSpeechSettingsArgs]]:
        
        ...
    
    @speech_settings.setter
    def speech_settings(self, value: Optional[pulumi.Input[CxAgentAdvancedSettingsSpeechSettingsArgs]]): # -> None:
        ...
    


class CxAgentAdvancedSettingsAudioExportGcsDestinationArgsDict(TypedDict):
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxAgentAdvancedSettingsAudioExportGcsDestinationArgs:
    def __init__(__self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxAgentAdvancedSettingsDtmfSettingsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    finish_digit: NotRequired[pulumi.Input[_builtins.str]]
    max_digits: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CxAgentAdvancedSettingsDtmfSettingsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., finish_digit: Optional[pulumi.Input[_builtins.str]] = ..., max_digits: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @finish_digit.setter
    def finish_digit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDigits")
    def max_digits(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_digits.setter
    def max_digits(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CxAgentAdvancedSettingsLoggingSettingsArgsDict(TypedDict):
    enable_consent_based_redaction: NotRequired[pulumi.Input[_builtins.bool]]
    enable_interaction_logging: NotRequired[pulumi.Input[_builtins.bool]]
    enable_stackdriver_logging: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxAgentAdvancedSettingsLoggingSettingsArgs:
    def __init__(__self__, *, enable_consent_based_redaction: Optional[pulumi.Input[_builtins.bool]] = ..., enable_interaction_logging: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableConsentBasedRedaction")
    def enable_consent_based_redaction(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_consent_based_redaction.setter
    def enable_consent_based_redaction(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInteractionLogging")
    def enable_interaction_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_interaction_logging.setter
    def enable_interaction_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_stackdriver_logging.setter
    def enable_stackdriver_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxAgentAdvancedSettingsSpeechSettingsArgsDict(TypedDict):
    endpointer_sensitivity: NotRequired[pulumi.Input[_builtins.int]]
    models: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    no_speech_timeout: NotRequired[pulumi.Input[_builtins.str]]
    use_timeout_based_endpointing: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxAgentAdvancedSettingsSpeechSettingsArgs:
    def __init__(__self__, *, endpointer_sensitivity: Optional[pulumi.Input[_builtins.int]] = ..., models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., no_speech_timeout: Optional[pulumi.Input[_builtins.str]] = ..., use_timeout_based_endpointing: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointerSensitivity")
    def endpointer_sensitivity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @endpointer_sensitivity.setter
    def endpointer_sensitivity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def models(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @models.setter
    def models(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noSpeechTimeout")
    def no_speech_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @no_speech_timeout.setter
    def no_speech_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useTimeoutBasedEndpointing")
    def use_timeout_based_endpointing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_timeout_based_endpointing.setter
    def use_timeout_based_endpointing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxAgentAnswerFeedbackSettingsArgsDict(TypedDict):
    enable_answer_feedback: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxAgentAnswerFeedbackSettingsArgs:
    def __init__(__self__, *, enable_answer_feedback: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAnswerFeedback")
    def enable_answer_feedback(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_answer_feedback.setter
    def enable_answer_feedback(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxAgentClientCertificateSettingsArgsDict(TypedDict):
    private_key: pulumi.Input[_builtins.str]
    ssl_certificate: pulumi.Input[_builtins.str]
    passphrase: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxAgentClientCertificateSettingsArgs:
    def __init__(__self__, *, private_key: pulumi.Input[_builtins.str], ssl_certificate: pulumi.Input[_builtins.str], passphrase: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @private_key.setter
    def private_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sslCertificate")
    def ssl_certificate(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @ssl_certificate.setter
    def ssl_certificate(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @passphrase.setter
    def passphrase(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxAgentGenAppBuilderSettingsArgsDict(TypedDict):
    engine: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxAgentGenAppBuilderSettingsArgs:
    def __init__(__self__, *, engine: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @engine.setter
    def engine(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxAgentGitIntegrationSettingsArgsDict(TypedDict):
    github_settings: NotRequired[pulumi.Input[CxAgentGitIntegrationSettingsGithubSettingsArgsDict]]


@pulumi.input_type
class CxAgentGitIntegrationSettingsArgs:
    def __init__(__self__, *, github_settings: Optional[pulumi.Input[CxAgentGitIntegrationSettingsGithubSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="githubSettings")
    def github_settings(self) -> Optional[pulumi.Input[CxAgentGitIntegrationSettingsGithubSettingsArgs]]:
        
        ...
    
    @github_settings.setter
    def github_settings(self, value: Optional[pulumi.Input[CxAgentGitIntegrationSettingsGithubSettingsArgs]]): # -> None:
        ...
    


class CxAgentGitIntegrationSettingsGithubSettingsArgsDict(TypedDict):
    access_token: NotRequired[pulumi.Input[_builtins.str]]
    branches: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    repository_uri: NotRequired[pulumi.Input[_builtins.str]]
    tracking_branch: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxAgentGitIntegrationSettingsGithubSettingsArgs:
    def __init__(__self__, *, access_token: Optional[pulumi.Input[_builtins.str]] = ..., branches: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., repository_uri: Optional[pulumi.Input[_builtins.str]] = ..., tracking_branch: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="accessToken")
    def access_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @access_token.setter
    def access_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def branches(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @branches.setter
    def branches(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repositoryUri")
    def repository_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @repository_uri.setter
    def repository_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingBranch")
    def tracking_branch(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tracking_branch.setter
    def tracking_branch(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxAgentPersonalizationSettingsArgsDict(TypedDict):
    default_end_user_metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxAgentPersonalizationSettingsArgs:
    def __init__(__self__, *, default_end_user_metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultEndUserMetadata")
    def default_end_user_metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_end_user_metadata.setter
    def default_end_user_metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxAgentSpeechToTextSettingsArgsDict(TypedDict):
    enable_speech_adaptation: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxAgentSpeechToTextSettingsArgs:
    def __init__(__self__, *, enable_speech_adaptation: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSpeechAdaptation")
    def enable_speech_adaptation(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_speech_adaptation.setter
    def enable_speech_adaptation(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxAgentTextToSpeechSettingsArgsDict(TypedDict):
    synthesize_speech_configs: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxAgentTextToSpeechSettingsArgs:
    def __init__(__self__, *, synthesize_speech_configs: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synthesizeSpeechConfigs")
    def synthesize_speech_configs(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @synthesize_speech_configs.setter
    def synthesize_speech_configs(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxEntityTypeEntityArgsDict(TypedDict):
    synonyms: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxEntityTypeEntityArgs:
    def __init__(__self__, *, synonyms: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def synonyms(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @synonyms.setter
    def synonyms(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxEntityTypeExcludedPhraseArgsDict(TypedDict):
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxEntityTypeExcludedPhraseArgs:
    def __init__(__self__, *, value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxEnvironmentVersionConfigArgsDict(TypedDict):
    version: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxEnvironmentVersionConfigArgs:
    def __init__(__self__, *, version: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxFlowAdvancedSettingsArgsDict(TypedDict):
    audio_export_gcs_destination: NotRequired[pulumi.Input[CxFlowAdvancedSettingsAudioExportGcsDestinationArgsDict]]
    dtmf_settings: NotRequired[pulumi.Input[CxFlowAdvancedSettingsDtmfSettingsArgsDict]]
    logging_settings: NotRequired[pulumi.Input[CxFlowAdvancedSettingsLoggingSettingsArgsDict]]
    speech_settings: NotRequired[pulumi.Input[CxFlowAdvancedSettingsSpeechSettingsArgsDict]]


@pulumi.input_type
class CxFlowAdvancedSettingsArgs:
    def __init__(__self__, *, audio_export_gcs_destination: Optional[pulumi.Input[CxFlowAdvancedSettingsAudioExportGcsDestinationArgs]] = ..., dtmf_settings: Optional[pulumi.Input[CxFlowAdvancedSettingsDtmfSettingsArgs]] = ..., logging_settings: Optional[pulumi.Input[CxFlowAdvancedSettingsLoggingSettingsArgs]] = ..., speech_settings: Optional[pulumi.Input[CxFlowAdvancedSettingsSpeechSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioExportGcsDestination")
    def audio_export_gcs_destination(self) -> Optional[pulumi.Input[CxFlowAdvancedSettingsAudioExportGcsDestinationArgs]]:
        
        ...
    
    @audio_export_gcs_destination.setter
    def audio_export_gcs_destination(self, value: Optional[pulumi.Input[CxFlowAdvancedSettingsAudioExportGcsDestinationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dtmfSettings")
    def dtmf_settings(self) -> Optional[pulumi.Input[CxFlowAdvancedSettingsDtmfSettingsArgs]]:
        
        ...
    
    @dtmf_settings.setter
    def dtmf_settings(self, value: Optional[pulumi.Input[CxFlowAdvancedSettingsDtmfSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingSettings")
    def logging_settings(self) -> Optional[pulumi.Input[CxFlowAdvancedSettingsLoggingSettingsArgs]]:
        
        ...
    
    @logging_settings.setter
    def logging_settings(self, value: Optional[pulumi.Input[CxFlowAdvancedSettingsLoggingSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="speechSettings")
    def speech_settings(self) -> Optional[pulumi.Input[CxFlowAdvancedSettingsSpeechSettingsArgs]]:
        
        ...
    
    @speech_settings.setter
    def speech_settings(self, value: Optional[pulumi.Input[CxFlowAdvancedSettingsSpeechSettingsArgs]]): # -> None:
        ...
    


class CxFlowAdvancedSettingsAudioExportGcsDestinationArgsDict(TypedDict):
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowAdvancedSettingsAudioExportGcsDestinationArgs:
    def __init__(__self__, *, uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowAdvancedSettingsDtmfSettingsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    finish_digit: NotRequired[pulumi.Input[_builtins.str]]
    max_digits: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CxFlowAdvancedSettingsDtmfSettingsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., finish_digit: Optional[pulumi.Input[_builtins.str]] = ..., max_digits: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @finish_digit.setter
    def finish_digit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDigits")
    def max_digits(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_digits.setter
    def max_digits(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CxFlowAdvancedSettingsLoggingSettingsArgsDict(TypedDict):
    enable_consent_based_redaction: NotRequired[pulumi.Input[_builtins.bool]]
    enable_interaction_logging: NotRequired[pulumi.Input[_builtins.bool]]
    enable_stackdriver_logging: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxFlowAdvancedSettingsLoggingSettingsArgs:
    def __init__(__self__, *, enable_consent_based_redaction: Optional[pulumi.Input[_builtins.bool]] = ..., enable_interaction_logging: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableConsentBasedRedaction")
    def enable_consent_based_redaction(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_consent_based_redaction.setter
    def enable_consent_based_redaction(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInteractionLogging")
    def enable_interaction_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_interaction_logging.setter
    def enable_interaction_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_stackdriver_logging.setter
    def enable_stackdriver_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxFlowAdvancedSettingsSpeechSettingsArgsDict(TypedDict):
    endpointer_sensitivity: NotRequired[pulumi.Input[_builtins.int]]
    models: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    no_speech_timeout: NotRequired[pulumi.Input[_builtins.str]]
    use_timeout_based_endpointing: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxFlowAdvancedSettingsSpeechSettingsArgs:
    def __init__(__self__, *, endpointer_sensitivity: Optional[pulumi.Input[_builtins.int]] = ..., models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., no_speech_timeout: Optional[pulumi.Input[_builtins.str]] = ..., use_timeout_based_endpointing: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointerSensitivity")
    def endpointer_sensitivity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @endpointer_sensitivity.setter
    def endpointer_sensitivity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def models(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @models.setter
    def models(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noSpeechTimeout")
    def no_speech_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @no_speech_timeout.setter
    def no_speech_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useTimeoutBasedEndpointing")
    def use_timeout_based_endpointing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_timeout_based_endpointing.setter
    def use_timeout_based_endpointing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxFlowEventHandlerArgsDict(TypedDict):
    event: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    target_flow: NotRequired[pulumi.Input[_builtins.str]]
    target_page: NotRequired[pulumi.Input[_builtins.str]]
    trigger_fulfillment: NotRequired[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentArgsDict]]


@pulumi.input_type
class CxFlowEventHandlerArgs:
    def __init__(__self__, *, event: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., target_flow: Optional[pulumi.Input[_builtins.str]] = ..., target_page: Optional[pulumi.Input[_builtins.str]] = ..., trigger_fulfillment: Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def event(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event.setter
    def event(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetFlow")
    def target_flow(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_flow.setter
    def target_flow(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPage")
    def target_page(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_page.setter
    def target_page(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerFulfillment")
    def trigger_fulfillment(self) -> Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentArgs]]:
        
        ...
    
    @trigger_fulfillment.setter
    def trigger_fulfillment(self, value: Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentArgs]]): # -> None:
        ...
    


class CxFlowEventHandlerTriggerFulfillmentArgsDict(TypedDict):
    conditional_cases: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentConditionalCaseArgsDict]]]]
    enable_generative_fallback: NotRequired[pulumi.Input[_builtins.bool]]
    messages: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageArgsDict]]]]
    return_partial_responses: NotRequired[pulumi.Input[_builtins.bool]]
    set_parameter_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentSetParameterActionArgsDict]]]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    webhook: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowEventHandlerTriggerFulfillmentArgs:
    def __init__(__self__, *, conditional_cases: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentConditionalCaseArgs]]]] = ..., enable_generative_fallback: Optional[pulumi.Input[_builtins.bool]] = ..., messages: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageArgs]]]] = ..., return_partial_responses: Optional[pulumi.Input[_builtins.bool]] = ..., set_parameter_actions: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentSetParameterActionArgs]]]] = ..., tag: Optional[pulumi.Input[_builtins.str]] = ..., webhook: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentConditionalCaseArgs]]]]:
        
        ...
    
    @conditional_cases.setter
    def conditional_cases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentConditionalCaseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableGenerativeFallback")
    def enable_generative_fallback(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_generative_fallback.setter
    def enable_generative_fallback(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageArgs]]]]:
        
        ...
    
    @messages.setter
    def messages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @return_partial_responses.setter
    def return_partial_responses(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentSetParameterActionArgs]]]]:
        
        ...
    
    @set_parameter_actions.setter
    def set_parameter_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentSetParameterActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @webhook.setter
    def webhook(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowEventHandlerTriggerFulfillmentConditionalCaseArgsDict(TypedDict):
    cases: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowEventHandlerTriggerFulfillmentConditionalCaseArgs:
    def __init__(__self__, *, cases: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cases.setter
    def cases(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowEventHandlerTriggerFulfillmentMessageArgsDict(TypedDict):
    channel: NotRequired[pulumi.Input[_builtins.str]]
    conversation_success: NotRequired[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageConversationSuccessArgsDict]]
    live_agent_handoff: NotRequired[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgsDict]]
    output_audio_text: NotRequired[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageOutputAudioTextArgsDict]]
    payload: NotRequired[pulumi.Input[_builtins.str]]
    play_audio: NotRequired[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessagePlayAudioArgsDict]]
    telephony_transfer_call: NotRequired[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgsDict]]
    text: NotRequired[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageTextArgsDict]]


@pulumi.input_type
class CxFlowEventHandlerTriggerFulfillmentMessageArgs:
    def __init__(__self__, *, channel: Optional[pulumi.Input[_builtins.str]] = ..., conversation_success: Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageConversationSuccessArgs]] = ..., live_agent_handoff: Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgs]] = ..., output_audio_text: Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageOutputAudioTextArgs]] = ..., payload: Optional[pulumi.Input[_builtins.str]] = ..., play_audio: Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessagePlayAudioArgs]] = ..., telephony_transfer_call: Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgs]] = ..., text: Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageTextArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel.setter
    def channel(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(self) -> Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageConversationSuccessArgs]]:
        
        ...
    
    @conversation_success.setter
    def conversation_success(self, value: Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageConversationSuccessArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(self) -> Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgs]]:
        
        ...
    
    @live_agent_handoff.setter
    def live_agent_handoff(self, value: Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(self) -> Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageOutputAudioTextArgs]]:
        
        ...
    
    @output_audio_text.setter
    def output_audio_text(self, value: Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageOutputAudioTextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @payload.setter
    def payload(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(self) -> Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessagePlayAudioArgs]]:
        
        ...
    
    @play_audio.setter
    def play_audio(self, value: Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessagePlayAudioArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(self) -> Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgs]]:
        
        ...
    
    @telephony_transfer_call.setter
    def telephony_transfer_call(self, value: Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageTextArgs]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[CxFlowEventHandlerTriggerFulfillmentMessageTextArgs]]): # -> None:
        ...
    


class CxFlowEventHandlerTriggerFulfillmentMessageConversationSuccessArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowEventHandlerTriggerFulfillmentMessageConversationSuccessArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowEventHandlerTriggerFulfillmentMessageOutputAudioTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    ssml: NotRequired[pulumi.Input[_builtins.str]]
    text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowEventHandlerTriggerFulfillmentMessageOutputAudioTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., ssml: Optional[pulumi.Input[_builtins.str]] = ..., text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssml.setter
    def ssml(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowEventHandlerTriggerFulfillmentMessagePlayAudioArgsDict(TypedDict):
    audio_uri: pulumi.Input[_builtins.str]
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxFlowEventHandlerTriggerFulfillmentMessagePlayAudioArgs:
    def __init__(__self__, *, audio_uri: pulumi.Input[_builtins.str], allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @audio_uri.setter
    def audio_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxFlowEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgsDict(TypedDict):
    phone_number: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxFlowEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgs:
    def __init__(__self__, *, phone_number: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxFlowEventHandlerTriggerFulfillmentMessageTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    texts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CxFlowEventHandlerTriggerFulfillmentMessageTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., texts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @texts.setter
    def texts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CxFlowEventHandlerTriggerFulfillmentSetParameterActionArgsDict(TypedDict):
    parameter: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowEventHandlerTriggerFulfillmentSetParameterActionArgs:
    def __init__(__self__, *, parameter: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parameter.setter
    def parameter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsArgsDict(TypedDict):
    data_store_connections: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsDataStoreConnectionArgsDict]]]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    target_flow: NotRequired[pulumi.Input[_builtins.str]]
    target_page: NotRequired[pulumi.Input[_builtins.str]]
    trigger_fulfillment: NotRequired[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentArgsDict]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsArgs:
    def __init__(__self__, *, data_store_connections: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsDataStoreConnectionArgs]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., target_flow: Optional[pulumi.Input[_builtins.str]] = ..., target_page: Optional[pulumi.Input[_builtins.str]] = ..., trigger_fulfillment: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreConnections")
    def data_store_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsDataStoreConnectionArgs]]]]:
        
        ...
    
    @data_store_connections.setter
    def data_store_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsDataStoreConnectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetFlow")
    def target_flow(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_flow.setter
    def target_flow(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPage")
    def target_page(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_page.setter
    def target_page(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerFulfillment")
    def trigger_fulfillment(self) -> Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentArgs]]:
        
        ...
    
    @trigger_fulfillment.setter
    def trigger_fulfillment(self, value: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentArgs]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsDataStoreConnectionArgsDict(TypedDict):
    data_store: NotRequired[pulumi.Input[_builtins.str]]
    data_store_type: NotRequired[pulumi.Input[_builtins.str]]
    document_processing_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsDataStoreConnectionArgs:
    def __init__(__self__, *, data_store: Optional[pulumi.Input[_builtins.str]] = ..., data_store_type: Optional[pulumi.Input[_builtins.str]] = ..., document_processing_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_store.setter
    def data_store(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreType")
    def data_store_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_store_type.setter
    def data_store_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentProcessingMode")
    def document_processing_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @document_processing_mode.setter
    def document_processing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentArgsDict(TypedDict):
    advanced_settings: NotRequired[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsArgsDict]]
    conditional_cases: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentConditionalCaseArgsDict]]]]
    enable_generative_fallback: NotRequired[pulumi.Input[_builtins.bool]]
    messages: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageArgsDict]]]]
    return_partial_responses: NotRequired[pulumi.Input[_builtins.bool]]
    set_parameter_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentSetParameterActionArgsDict]]]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    webhook: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentArgs:
    def __init__(__self__, *, advanced_settings: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsArgs]] = ..., conditional_cases: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentConditionalCaseArgs]]]] = ..., enable_generative_fallback: Optional[pulumi.Input[_builtins.bool]] = ..., messages: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageArgs]]]] = ..., return_partial_responses: Optional[pulumi.Input[_builtins.bool]] = ..., set_parameter_actions: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentSetParameterActionArgs]]]] = ..., tag: Optional[pulumi.Input[_builtins.str]] = ..., webhook: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(self) -> Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsArgs]]:
        
        ...
    
    @advanced_settings.setter
    def advanced_settings(self, value: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentConditionalCaseArgs]]]]:
        
        ...
    
    @conditional_cases.setter
    def conditional_cases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentConditionalCaseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableGenerativeFallback")
    def enable_generative_fallback(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_generative_fallback.setter
    def enable_generative_fallback(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageArgs]]]]:
        
        ...
    
    @messages.setter
    def messages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @return_partial_responses.setter
    def return_partial_responses(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentSetParameterActionArgs]]]]:
        
        ...
    
    @set_parameter_actions.setter
    def set_parameter_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentSetParameterActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @webhook.setter
    def webhook(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsArgsDict(TypedDict):
    dtmf_settings: NotRequired[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettingsArgsDict]]
    logging_settings: NotRequired[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettingsArgsDict]]
    speech_settings: NotRequired[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettingsArgsDict]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsArgs:
    def __init__(__self__, *, dtmf_settings: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettingsArgs]] = ..., logging_settings: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettingsArgs]] = ..., speech_settings: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dtmfSettings")
    def dtmf_settings(self) -> Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettingsArgs]]:
        
        ...
    
    @dtmf_settings.setter
    def dtmf_settings(self, value: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingSettings")
    def logging_settings(self) -> Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettingsArgs]]:
        
        ...
    
    @logging_settings.setter
    def logging_settings(self, value: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="speechSettings")
    def speech_settings(self) -> Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettingsArgs]]:
        
        ...
    
    @speech_settings.setter
    def speech_settings(self, value: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettingsArgs]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettingsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    endpointing_timeout_duration: NotRequired[pulumi.Input[_builtins.str]]
    finish_digit: NotRequired[pulumi.Input[_builtins.str]]
    interdigit_timeout_duration: NotRequired[pulumi.Input[_builtins.str]]
    max_digits: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettingsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., endpointing_timeout_duration: Optional[pulumi.Input[_builtins.str]] = ..., finish_digit: Optional[pulumi.Input[_builtins.str]] = ..., interdigit_timeout_duration: Optional[pulumi.Input[_builtins.str]] = ..., max_digits: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointingTimeoutDuration")
    def endpointing_timeout_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpointing_timeout_duration.setter
    def endpointing_timeout_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @finish_digit.setter
    def finish_digit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interdigitTimeoutDuration")
    def interdigit_timeout_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interdigit_timeout_duration.setter
    def interdigit_timeout_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDigits")
    def max_digits(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_digits.setter
    def max_digits(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettingsArgsDict(TypedDict):
    enable_consent_based_redaction: NotRequired[pulumi.Input[_builtins.bool]]
    enable_interaction_logging: NotRequired[pulumi.Input[_builtins.bool]]
    enable_stackdriver_logging: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettingsArgs:
    def __init__(__self__, *, enable_consent_based_redaction: Optional[pulumi.Input[_builtins.bool]] = ..., enable_interaction_logging: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableConsentBasedRedaction")
    def enable_consent_based_redaction(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_consent_based_redaction.setter
    def enable_consent_based_redaction(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInteractionLogging")
    def enable_interaction_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_interaction_logging.setter
    def enable_interaction_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_stackdriver_logging.setter
    def enable_stackdriver_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettingsArgsDict(TypedDict):
    endpointer_sensitivity: NotRequired[pulumi.Input[_builtins.int]]
    models: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    no_speech_timeout: NotRequired[pulumi.Input[_builtins.str]]
    use_timeout_based_endpointing: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettingsArgs:
    def __init__(__self__, *, endpointer_sensitivity: Optional[pulumi.Input[_builtins.int]] = ..., models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., no_speech_timeout: Optional[pulumi.Input[_builtins.str]] = ..., use_timeout_based_endpointing: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointerSensitivity")
    def endpointer_sensitivity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @endpointer_sensitivity.setter
    def endpointer_sensitivity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def models(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @models.setter
    def models(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noSpeechTimeout")
    def no_speech_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @no_speech_timeout.setter
    def no_speech_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useTimeoutBasedEndpointing")
    def use_timeout_based_endpointing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_timeout_based_endpointing.setter
    def use_timeout_based_endpointing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentConditionalCaseArgsDict(TypedDict):
    cases: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentConditionalCaseArgs:
    def __init__(__self__, *, cases: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cases.setter
    def cases(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageArgsDict(TypedDict):
    channel: NotRequired[pulumi.Input[_builtins.str]]
    conversation_success: NotRequired[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccessArgsDict]]
    end_interactions: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteractionArgsDict]]]]
    knowledge_info_card: NotRequired[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCardArgsDict]]
    live_agent_handoff: NotRequired[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoffArgsDict]]
    mixed_audios: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioArgsDict]]]]
    output_audio_text: NotRequired[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioTextArgsDict]]
    payload: NotRequired[pulumi.Input[_builtins.str]]
    play_audio: NotRequired[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudioArgsDict]]
    telephony_transfer_call: NotRequired[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCallArgsDict]]
    text: NotRequired[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageTextArgsDict]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageArgs:
    def __init__(__self__, *, channel: Optional[pulumi.Input[_builtins.str]] = ..., conversation_success: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccessArgs]] = ..., end_interactions: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteractionArgs]]]] = ..., knowledge_info_card: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCardArgs]] = ..., live_agent_handoff: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoffArgs]] = ..., mixed_audios: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioArgs]]]] = ..., output_audio_text: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioTextArgs]] = ..., payload: Optional[pulumi.Input[_builtins.str]] = ..., play_audio: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudioArgs]] = ..., telephony_transfer_call: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCallArgs]] = ..., text: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageTextArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel.setter
    def channel(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(self) -> Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccessArgs]]:
        
        ...
    
    @conversation_success.setter
    def conversation_success(self, value: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccessArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endInteractions")
    def end_interactions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteractionArgs]]]]:
        
        ...
    
    @end_interactions.setter
    def end_interactions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteractionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeInfoCard")
    def knowledge_info_card(self) -> Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCardArgs]]:
        
        ...
    
    @knowledge_info_card.setter
    def knowledge_info_card(self, value: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCardArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(self) -> Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoffArgs]]:
        
        ...
    
    @live_agent_handoff.setter
    def live_agent_handoff(self, value: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoffArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mixedAudios")
    def mixed_audios(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioArgs]]]]:
        
        ...
    
    @mixed_audios.setter
    def mixed_audios(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(self) -> Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioTextArgs]]:
        
        ...
    
    @output_audio_text.setter
    def output_audio_text(self, value: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioTextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @payload.setter
    def payload(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(self) -> Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudioArgs]]:
        
        ...
    
    @play_audio.setter
    def play_audio(self, value: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudioArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(self) -> Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCallArgs]]:
        
        ...
    
    @telephony_transfer_call.setter
    def telephony_transfer_call(self, value: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCallArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageTextArgs]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageTextArgs]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccessArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccessArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteractionArgsDict(TypedDict):
    ...


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteractionArgs:
    def __init__(__self__) -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCardArgsDict(TypedDict):
    ...


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCardArgs:
    def __init__(__self__) -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoffArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoffArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioArgsDict(TypedDict):
    segments: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegmentArgsDict]]]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioArgs:
    def __init__(__self__, *, segments: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegmentArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def segments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegmentArgs]]]]:
        
        ...
    
    @segments.setter
    def segments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegmentArgs]]]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegmentArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    audio: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegmentArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., audio: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def audio(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @audio.setter
    def audio(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    ssml: NotRequired[pulumi.Input[_builtins.str]]
    text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., ssml: Optional[pulumi.Input[_builtins.str]] = ..., text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssml.setter
    def ssml(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudioArgsDict(TypedDict):
    audio_uri: pulumi.Input[_builtins.str]
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudioArgs:
    def __init__(__self__, *, audio_uri: pulumi.Input[_builtins.str], allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @audio_uri.setter
    def audio_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCallArgsDict(TypedDict):
    phone_number: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCallArgs:
    def __init__(__self__, *, phone_number: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    texts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentMessageTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., texts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @texts.setter
    def texts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentSetParameterActionArgsDict(TypedDict):
    parameter: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowKnowledgeConnectorSettingsTriggerFulfillmentSetParameterActionArgs:
    def __init__(__self__, *, parameter: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parameter.setter
    def parameter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowNluSettingsArgsDict(TypedDict):
    classification_threshold: NotRequired[pulumi.Input[_builtins.float]]
    model_training_mode: NotRequired[pulumi.Input[_builtins.str]]
    model_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowNluSettingsArgs:
    def __init__(__self__, *, classification_threshold: Optional[pulumi.Input[_builtins.float]] = ..., model_training_mode: Optional[pulumi.Input[_builtins.str]] = ..., model_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationThreshold")
    def classification_threshold(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @classification_threshold.setter
    def classification_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelTrainingMode")
    def model_training_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_training_mode.setter
    def model_training_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelType")
    def model_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_type.setter
    def model_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowTransitionRouteArgsDict(TypedDict):
    condition: NotRequired[pulumi.Input[_builtins.str]]
    intent: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    target_flow: NotRequired[pulumi.Input[_builtins.str]]
    target_page: NotRequired[pulumi.Input[_builtins.str]]
    trigger_fulfillment: NotRequired[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentArgsDict]]


@pulumi.input_type
class CxFlowTransitionRouteArgs:
    def __init__(__self__, *, condition: Optional[pulumi.Input[_builtins.str]] = ..., intent: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., target_flow: Optional[pulumi.Input[_builtins.str]] = ..., target_page: Optional[pulumi.Input[_builtins.str]] = ..., trigger_fulfillment: Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @intent.setter
    def intent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetFlow")
    def target_flow(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_flow.setter
    def target_flow(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPage")
    def target_page(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_page.setter
    def target_page(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerFulfillment")
    def trigger_fulfillment(self) -> Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentArgs]]:
        
        ...
    
    @trigger_fulfillment.setter
    def trigger_fulfillment(self, value: Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentArgs]]): # -> None:
        ...
    


class CxFlowTransitionRouteTriggerFulfillmentArgsDict(TypedDict):
    conditional_cases: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentConditionalCaseArgsDict]]]]
    messages: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageArgsDict]]]]
    return_partial_responses: NotRequired[pulumi.Input[_builtins.bool]]
    set_parameter_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentSetParameterActionArgsDict]]]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    webhook: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowTransitionRouteTriggerFulfillmentArgs:
    def __init__(__self__, *, conditional_cases: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentConditionalCaseArgs]]]] = ..., messages: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageArgs]]]] = ..., return_partial_responses: Optional[pulumi.Input[_builtins.bool]] = ..., set_parameter_actions: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentSetParameterActionArgs]]]] = ..., tag: Optional[pulumi.Input[_builtins.str]] = ..., webhook: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentConditionalCaseArgs]]]]:
        
        ...
    
    @conditional_cases.setter
    def conditional_cases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentConditionalCaseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageArgs]]]]:
        
        ...
    
    @messages.setter
    def messages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @return_partial_responses.setter
    def return_partial_responses(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentSetParameterActionArgs]]]]:
        
        ...
    
    @set_parameter_actions.setter
    def set_parameter_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentSetParameterActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @webhook.setter
    def webhook(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowTransitionRouteTriggerFulfillmentConditionalCaseArgsDict(TypedDict):
    cases: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowTransitionRouteTriggerFulfillmentConditionalCaseArgs:
    def __init__(__self__, *, cases: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cases.setter
    def cases(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowTransitionRouteTriggerFulfillmentMessageArgsDict(TypedDict):
    channel: NotRequired[pulumi.Input[_builtins.str]]
    conversation_success: NotRequired[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageConversationSuccessArgsDict]]
    live_agent_handoff: NotRequired[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageLiveAgentHandoffArgsDict]]
    output_audio_text: NotRequired[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageOutputAudioTextArgsDict]]
    payload: NotRequired[pulumi.Input[_builtins.str]]
    play_audio: NotRequired[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessagePlayAudioArgsDict]]
    telephony_transfer_call: NotRequired[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageTelephonyTransferCallArgsDict]]
    text: NotRequired[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageTextArgsDict]]


@pulumi.input_type
class CxFlowTransitionRouteTriggerFulfillmentMessageArgs:
    def __init__(__self__, *, channel: Optional[pulumi.Input[_builtins.str]] = ..., conversation_success: Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageConversationSuccessArgs]] = ..., live_agent_handoff: Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageLiveAgentHandoffArgs]] = ..., output_audio_text: Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageOutputAudioTextArgs]] = ..., payload: Optional[pulumi.Input[_builtins.str]] = ..., play_audio: Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessagePlayAudioArgs]] = ..., telephony_transfer_call: Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageTelephonyTransferCallArgs]] = ..., text: Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageTextArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel.setter
    def channel(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(self) -> Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageConversationSuccessArgs]]:
        
        ...
    
    @conversation_success.setter
    def conversation_success(self, value: Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageConversationSuccessArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(self) -> Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageLiveAgentHandoffArgs]]:
        
        ...
    
    @live_agent_handoff.setter
    def live_agent_handoff(self, value: Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageLiveAgentHandoffArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(self) -> Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageOutputAudioTextArgs]]:
        
        ...
    
    @output_audio_text.setter
    def output_audio_text(self, value: Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageOutputAudioTextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @payload.setter
    def payload(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(self) -> Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessagePlayAudioArgs]]:
        
        ...
    
    @play_audio.setter
    def play_audio(self, value: Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessagePlayAudioArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(self) -> Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageTelephonyTransferCallArgs]]:
        
        ...
    
    @telephony_transfer_call.setter
    def telephony_transfer_call(self, value: Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageTelephonyTransferCallArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageTextArgs]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[CxFlowTransitionRouteTriggerFulfillmentMessageTextArgs]]): # -> None:
        ...
    


class CxFlowTransitionRouteTriggerFulfillmentMessageConversationSuccessArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowTransitionRouteTriggerFulfillmentMessageConversationSuccessArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowTransitionRouteTriggerFulfillmentMessageLiveAgentHandoffArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowTransitionRouteTriggerFulfillmentMessageLiveAgentHandoffArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowTransitionRouteTriggerFulfillmentMessageOutputAudioTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    ssml: NotRequired[pulumi.Input[_builtins.str]]
    text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowTransitionRouteTriggerFulfillmentMessageOutputAudioTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., ssml: Optional[pulumi.Input[_builtins.str]] = ..., text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssml.setter
    def ssml(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxFlowTransitionRouteTriggerFulfillmentMessagePlayAudioArgsDict(TypedDict):
    audio_uri: pulumi.Input[_builtins.str]
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxFlowTransitionRouteTriggerFulfillmentMessagePlayAudioArgs:
    def __init__(__self__, *, audio_uri: pulumi.Input[_builtins.str], allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @audio_uri.setter
    def audio_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxFlowTransitionRouteTriggerFulfillmentMessageTelephonyTransferCallArgsDict(TypedDict):
    phone_number: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxFlowTransitionRouteTriggerFulfillmentMessageTelephonyTransferCallArgs:
    def __init__(__self__, *, phone_number: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxFlowTransitionRouteTriggerFulfillmentMessageTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    texts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CxFlowTransitionRouteTriggerFulfillmentMessageTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., texts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @texts.setter
    def texts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CxFlowTransitionRouteTriggerFulfillmentSetParameterActionArgsDict(TypedDict):
    parameter: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxFlowTransitionRouteTriggerFulfillmentSetParameterActionArgs:
    def __init__(__self__, *, parameter: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parameter.setter
    def parameter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxGenerativeSettingsFallbackSettingsArgsDict(TypedDict):
    prompt_templates: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxGenerativeSettingsFallbackSettingsPromptTemplateArgsDict]]]]
    selected_prompt: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxGenerativeSettingsFallbackSettingsArgs:
    def __init__(__self__, *, prompt_templates: Optional[pulumi.Input[Sequence[pulumi.Input[CxGenerativeSettingsFallbackSettingsPromptTemplateArgs]]]] = ..., selected_prompt: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="promptTemplates")
    def prompt_templates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxGenerativeSettingsFallbackSettingsPromptTemplateArgs]]]]:
        
        ...
    
    @prompt_templates.setter
    def prompt_templates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxGenerativeSettingsFallbackSettingsPromptTemplateArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="selectedPrompt")
    def selected_prompt(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @selected_prompt.setter
    def selected_prompt(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxGenerativeSettingsFallbackSettingsPromptTemplateArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    frozen: NotRequired[pulumi.Input[_builtins.bool]]
    prompt_text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxGenerativeSettingsFallbackSettingsPromptTemplateArgs:
    def __init__(__self__, *, display_name: Optional[pulumi.Input[_builtins.str]] = ..., frozen: Optional[pulumi.Input[_builtins.bool]] = ..., prompt_text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def frozen(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @frozen.setter
    def frozen(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="promptText")
    def prompt_text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prompt_text.setter
    def prompt_text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxGenerativeSettingsGenerativeSafetySettingsArgsDict(TypedDict):
    banned_phrases: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxGenerativeSettingsGenerativeSafetySettingsBannedPhraseArgsDict]]]]
    default_banned_phrase_match_strategy: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxGenerativeSettingsGenerativeSafetySettingsArgs:
    def __init__(__self__, *, banned_phrases: Optional[pulumi.Input[Sequence[pulumi.Input[CxGenerativeSettingsGenerativeSafetySettingsBannedPhraseArgs]]]] = ..., default_banned_phrase_match_strategy: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bannedPhrases")
    def banned_phrases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxGenerativeSettingsGenerativeSafetySettingsBannedPhraseArgs]]]]:
        
        ...
    
    @banned_phrases.setter
    def banned_phrases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxGenerativeSettingsGenerativeSafetySettingsBannedPhraseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultBannedPhraseMatchStrategy")
    def default_banned_phrase_match_strategy(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_banned_phrase_match_strategy.setter
    def default_banned_phrase_match_strategy(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxGenerativeSettingsGenerativeSafetySettingsBannedPhraseArgsDict(TypedDict):
    language_code: pulumi.Input[_builtins.str]
    text: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxGenerativeSettingsGenerativeSafetySettingsBannedPhraseArgs:
    def __init__(__self__, *, language_code: pulumi.Input[_builtins.str], text: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @language_code.setter
    def language_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @text.setter
    def text(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxGenerativeSettingsKnowledgeConnectorSettingsArgsDict(TypedDict):
    agent: NotRequired[pulumi.Input[_builtins.str]]
    agent_identity: NotRequired[pulumi.Input[_builtins.str]]
    agent_scope: NotRequired[pulumi.Input[_builtins.str]]
    business: NotRequired[pulumi.Input[_builtins.str]]
    business_description: NotRequired[pulumi.Input[_builtins.str]]
    disable_data_store_fallback: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxGenerativeSettingsKnowledgeConnectorSettingsArgs:
    def __init__(__self__, *, agent: Optional[pulumi.Input[_builtins.str]] = ..., agent_identity: Optional[pulumi.Input[_builtins.str]] = ..., agent_scope: Optional[pulumi.Input[_builtins.str]] = ..., business: Optional[pulumi.Input[_builtins.str]] = ..., business_description: Optional[pulumi.Input[_builtins.str]] = ..., disable_data_store_fallback: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def agent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent.setter
    def agent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentIdentity")
    def agent_identity(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_identity.setter
    def agent_identity(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentScope")
    def agent_scope(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_scope.setter
    def agent_scope(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def business(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @business.setter
    def business(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="businessDescription")
    def business_description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @business_description.setter
    def business_description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableDataStoreFallback")
    def disable_data_store_fallback(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @disable_data_store_fallback.setter
    def disable_data_store_fallback(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxGenerativeSettingsLlmModelSettingsArgsDict(TypedDict):
    model: NotRequired[pulumi.Input[_builtins.str]]
    prompt_text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxGenerativeSettingsLlmModelSettingsArgs:
    def __init__(__self__, *, model: Optional[pulumi.Input[_builtins.str]] = ..., prompt_text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="promptText")
    def prompt_text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prompt_text.setter
    def prompt_text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxGeneratorLlmModelSettingsArgsDict(TypedDict):
    model: NotRequired[pulumi.Input[_builtins.str]]
    prompt_text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxGeneratorLlmModelSettingsArgs:
    def __init__(__self__, *, model: Optional[pulumi.Input[_builtins.str]] = ..., prompt_text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="promptText")
    def prompt_text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prompt_text.setter
    def prompt_text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxGeneratorModelParameterArgsDict(TypedDict):
    max_decode_steps: NotRequired[pulumi.Input[_builtins.int]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    top_k: NotRequired[pulumi.Input[_builtins.int]]
    top_p: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class CxGeneratorModelParameterArgs:
    def __init__(__self__, *, max_decode_steps: Optional[pulumi.Input[_builtins.int]] = ..., temperature: Optional[pulumi.Input[_builtins.float]] = ..., top_k: Optional[pulumi.Input[_builtins.int]] = ..., top_p: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDecodeSteps")
    def max_decode_steps(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_decode_steps.setter
    def max_decode_steps(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topK")
    def top_k(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @top_k.setter
    def top_k(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topP")
    def top_p(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @top_p.setter
    def top_p(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class CxGeneratorPlaceholderArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxGeneratorPlaceholderArgs:
    def __init__(__self__, *, id: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxGeneratorPromptTextArgsDict(TypedDict):
    text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxGeneratorPromptTextArgs:
    def __init__(__self__, *, text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxIntentParameterArgsDict(TypedDict):
    entity_type: pulumi.Input[_builtins.str]
    id: pulumi.Input[_builtins.str]
    is_list: NotRequired[pulumi.Input[_builtins.bool]]
    redact: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxIntentParameterArgs:
    def __init__(__self__, *, entity_type: pulumi.Input[_builtins.str], id: pulumi.Input[_builtins.str], is_list: Optional[pulumi.Input[_builtins.bool]] = ..., redact: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @entity_type.setter
    def entity_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @id.setter
    def id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isList")
    def is_list(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_list.setter
    def is_list(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def redact(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @redact.setter
    def redact(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxIntentTrainingPhraseArgsDict(TypedDict):
    parts: pulumi.Input[Sequence[pulumi.Input[CxIntentTrainingPhrasePartArgsDict]]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    repeat_count: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CxIntentTrainingPhraseArgs:
    def __init__(__self__, *, parts: pulumi.Input[Sequence[pulumi.Input[CxIntentTrainingPhrasePartArgs]]], id: Optional[pulumi.Input[_builtins.str]] = ..., repeat_count: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parts(self) -> pulumi.Input[Sequence[pulumi.Input[CxIntentTrainingPhrasePartArgs]]]:
        
        ...
    
    @parts.setter
    def parts(self, value: pulumi.Input[Sequence[pulumi.Input[CxIntentTrainingPhrasePartArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repeatCount")
    def repeat_count(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @repeat_count.setter
    def repeat_count(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CxIntentTrainingPhrasePartArgsDict(TypedDict):
    text: pulumi.Input[_builtins.str]
    parameter_id: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxIntentTrainingPhrasePartArgs:
    def __init__(__self__, *, text: pulumi.Input[_builtins.str], parameter_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @text.setter
    def text(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterId")
    def parameter_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parameter_id.setter
    def parameter_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageAdvancedSettingsArgsDict(TypedDict):
    dtmf_settings: NotRequired[pulumi.Input[CxPageAdvancedSettingsDtmfSettingsArgsDict]]


@pulumi.input_type
class CxPageAdvancedSettingsArgs:
    def __init__(__self__, *, dtmf_settings: Optional[pulumi.Input[CxPageAdvancedSettingsDtmfSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dtmfSettings")
    def dtmf_settings(self) -> Optional[pulumi.Input[CxPageAdvancedSettingsDtmfSettingsArgs]]:
        
        ...
    
    @dtmf_settings.setter
    def dtmf_settings(self, value: Optional[pulumi.Input[CxPageAdvancedSettingsDtmfSettingsArgs]]): # -> None:
        ...
    


class CxPageAdvancedSettingsDtmfSettingsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    finish_digit: NotRequired[pulumi.Input[_builtins.str]]
    max_digits: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CxPageAdvancedSettingsDtmfSettingsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., finish_digit: Optional[pulumi.Input[_builtins.str]] = ..., max_digits: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @finish_digit.setter
    def finish_digit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDigits")
    def max_digits(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_digits.setter
    def max_digits(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CxPageEntryFulfillmentArgsDict(TypedDict):
    conditional_cases: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageEntryFulfillmentConditionalCaseArgsDict]]]]
    messages: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageEntryFulfillmentMessageArgsDict]]]]
    return_partial_responses: NotRequired[pulumi.Input[_builtins.bool]]
    set_parameter_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageEntryFulfillmentSetParameterActionArgsDict]]]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    webhook: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageEntryFulfillmentArgs:
    def __init__(__self__, *, conditional_cases: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEntryFulfillmentConditionalCaseArgs]]]] = ..., messages: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEntryFulfillmentMessageArgs]]]] = ..., return_partial_responses: Optional[pulumi.Input[_builtins.bool]] = ..., set_parameter_actions: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEntryFulfillmentSetParameterActionArgs]]]] = ..., tag: Optional[pulumi.Input[_builtins.str]] = ..., webhook: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEntryFulfillmentConditionalCaseArgs]]]]:
        
        ...
    
    @conditional_cases.setter
    def conditional_cases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEntryFulfillmentConditionalCaseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEntryFulfillmentMessageArgs]]]]:
        
        ...
    
    @messages.setter
    def messages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEntryFulfillmentMessageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @return_partial_responses.setter
    def return_partial_responses(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEntryFulfillmentSetParameterActionArgs]]]]:
        
        ...
    
    @set_parameter_actions.setter
    def set_parameter_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEntryFulfillmentSetParameterActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @webhook.setter
    def webhook(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageEntryFulfillmentConditionalCaseArgsDict(TypedDict):
    cases: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageEntryFulfillmentConditionalCaseArgs:
    def __init__(__self__, *, cases: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cases.setter
    def cases(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageEntryFulfillmentMessageArgsDict(TypedDict):
    channel: NotRequired[pulumi.Input[_builtins.str]]
    conversation_success: NotRequired[pulumi.Input[CxPageEntryFulfillmentMessageConversationSuccessArgsDict]]
    live_agent_handoff: NotRequired[pulumi.Input[CxPageEntryFulfillmentMessageLiveAgentHandoffArgsDict]]
    output_audio_text: NotRequired[pulumi.Input[CxPageEntryFulfillmentMessageOutputAudioTextArgsDict]]
    payload: NotRequired[pulumi.Input[_builtins.str]]
    play_audio: NotRequired[pulumi.Input[CxPageEntryFulfillmentMessagePlayAudioArgsDict]]
    telephony_transfer_call: NotRequired[pulumi.Input[CxPageEntryFulfillmentMessageTelephonyTransferCallArgsDict]]
    text: NotRequired[pulumi.Input[CxPageEntryFulfillmentMessageTextArgsDict]]


@pulumi.input_type
class CxPageEntryFulfillmentMessageArgs:
    def __init__(__self__, *, channel: Optional[pulumi.Input[_builtins.str]] = ..., conversation_success: Optional[pulumi.Input[CxPageEntryFulfillmentMessageConversationSuccessArgs]] = ..., live_agent_handoff: Optional[pulumi.Input[CxPageEntryFulfillmentMessageLiveAgentHandoffArgs]] = ..., output_audio_text: Optional[pulumi.Input[CxPageEntryFulfillmentMessageOutputAudioTextArgs]] = ..., payload: Optional[pulumi.Input[_builtins.str]] = ..., play_audio: Optional[pulumi.Input[CxPageEntryFulfillmentMessagePlayAudioArgs]] = ..., telephony_transfer_call: Optional[pulumi.Input[CxPageEntryFulfillmentMessageTelephonyTransferCallArgs]] = ..., text: Optional[pulumi.Input[CxPageEntryFulfillmentMessageTextArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel.setter
    def channel(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(self) -> Optional[pulumi.Input[CxPageEntryFulfillmentMessageConversationSuccessArgs]]:
        
        ...
    
    @conversation_success.setter
    def conversation_success(self, value: Optional[pulumi.Input[CxPageEntryFulfillmentMessageConversationSuccessArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(self) -> Optional[pulumi.Input[CxPageEntryFulfillmentMessageLiveAgentHandoffArgs]]:
        
        ...
    
    @live_agent_handoff.setter
    def live_agent_handoff(self, value: Optional[pulumi.Input[CxPageEntryFulfillmentMessageLiveAgentHandoffArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(self) -> Optional[pulumi.Input[CxPageEntryFulfillmentMessageOutputAudioTextArgs]]:
        
        ...
    
    @output_audio_text.setter
    def output_audio_text(self, value: Optional[pulumi.Input[CxPageEntryFulfillmentMessageOutputAudioTextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @payload.setter
    def payload(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(self) -> Optional[pulumi.Input[CxPageEntryFulfillmentMessagePlayAudioArgs]]:
        
        ...
    
    @play_audio.setter
    def play_audio(self, value: Optional[pulumi.Input[CxPageEntryFulfillmentMessagePlayAudioArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(self) -> Optional[pulumi.Input[CxPageEntryFulfillmentMessageTelephonyTransferCallArgs]]:
        
        ...
    
    @telephony_transfer_call.setter
    def telephony_transfer_call(self, value: Optional[pulumi.Input[CxPageEntryFulfillmentMessageTelephonyTransferCallArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[CxPageEntryFulfillmentMessageTextArgs]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[CxPageEntryFulfillmentMessageTextArgs]]): # -> None:
        ...
    


class CxPageEntryFulfillmentMessageConversationSuccessArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageEntryFulfillmentMessageConversationSuccessArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageEntryFulfillmentMessageLiveAgentHandoffArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageEntryFulfillmentMessageLiveAgentHandoffArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageEntryFulfillmentMessageOutputAudioTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    ssml: NotRequired[pulumi.Input[_builtins.str]]
    text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageEntryFulfillmentMessageOutputAudioTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., ssml: Optional[pulumi.Input[_builtins.str]] = ..., text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssml.setter
    def ssml(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageEntryFulfillmentMessagePlayAudioArgsDict(TypedDict):
    audio_uri: pulumi.Input[_builtins.str]
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxPageEntryFulfillmentMessagePlayAudioArgs:
    def __init__(__self__, *, audio_uri: pulumi.Input[_builtins.str], allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @audio_uri.setter
    def audio_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxPageEntryFulfillmentMessageTelephonyTransferCallArgsDict(TypedDict):
    phone_number: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxPageEntryFulfillmentMessageTelephonyTransferCallArgs:
    def __init__(__self__, *, phone_number: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxPageEntryFulfillmentMessageTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    texts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CxPageEntryFulfillmentMessageTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., texts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @texts.setter
    def texts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CxPageEntryFulfillmentSetParameterActionArgsDict(TypedDict):
    parameter: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageEntryFulfillmentSetParameterActionArgs:
    def __init__(__self__, *, parameter: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parameter.setter
    def parameter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageEventHandlerArgsDict(TypedDict):
    event: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    target_flow: NotRequired[pulumi.Input[_builtins.str]]
    target_page: NotRequired[pulumi.Input[_builtins.str]]
    trigger_fulfillment: NotRequired[pulumi.Input[CxPageEventHandlerTriggerFulfillmentArgsDict]]


@pulumi.input_type
class CxPageEventHandlerArgs:
    def __init__(__self__, *, event: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., target_flow: Optional[pulumi.Input[_builtins.str]] = ..., target_page: Optional[pulumi.Input[_builtins.str]] = ..., trigger_fulfillment: Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def event(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event.setter
    def event(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetFlow")
    def target_flow(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_flow.setter
    def target_flow(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPage")
    def target_page(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_page.setter
    def target_page(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerFulfillment")
    def trigger_fulfillment(self) -> Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentArgs]]:
        
        ...
    
    @trigger_fulfillment.setter
    def trigger_fulfillment(self, value: Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentArgs]]): # -> None:
        ...
    


class CxPageEventHandlerTriggerFulfillmentArgsDict(TypedDict):
    conditional_cases: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerTriggerFulfillmentConditionalCaseArgsDict]]]]
    messages: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageArgsDict]]]]
    return_partial_responses: NotRequired[pulumi.Input[_builtins.bool]]
    set_parameter_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerTriggerFulfillmentSetParameterActionArgsDict]]]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    webhook: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageEventHandlerTriggerFulfillmentArgs:
    def __init__(__self__, *, conditional_cases: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerTriggerFulfillmentConditionalCaseArgs]]]] = ..., messages: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageArgs]]]] = ..., return_partial_responses: Optional[pulumi.Input[_builtins.bool]] = ..., set_parameter_actions: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerTriggerFulfillmentSetParameterActionArgs]]]] = ..., tag: Optional[pulumi.Input[_builtins.str]] = ..., webhook: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerTriggerFulfillmentConditionalCaseArgs]]]]:
        
        ...
    
    @conditional_cases.setter
    def conditional_cases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerTriggerFulfillmentConditionalCaseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageArgs]]]]:
        
        ...
    
    @messages.setter
    def messages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @return_partial_responses.setter
    def return_partial_responses(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerTriggerFulfillmentSetParameterActionArgs]]]]:
        
        ...
    
    @set_parameter_actions.setter
    def set_parameter_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageEventHandlerTriggerFulfillmentSetParameterActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @webhook.setter
    def webhook(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageEventHandlerTriggerFulfillmentConditionalCaseArgsDict(TypedDict):
    cases: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageEventHandlerTriggerFulfillmentConditionalCaseArgs:
    def __init__(__self__, *, cases: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cases.setter
    def cases(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageEventHandlerTriggerFulfillmentMessageArgsDict(TypedDict):
    channel: NotRequired[pulumi.Input[_builtins.str]]
    conversation_success: NotRequired[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageConversationSuccessArgsDict]]
    live_agent_handoff: NotRequired[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgsDict]]
    output_audio_text: NotRequired[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageOutputAudioTextArgsDict]]
    payload: NotRequired[pulumi.Input[_builtins.str]]
    play_audio: NotRequired[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessagePlayAudioArgsDict]]
    telephony_transfer_call: NotRequired[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgsDict]]
    text: NotRequired[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageTextArgsDict]]


@pulumi.input_type
class CxPageEventHandlerTriggerFulfillmentMessageArgs:
    def __init__(__self__, *, channel: Optional[pulumi.Input[_builtins.str]] = ..., conversation_success: Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageConversationSuccessArgs]] = ..., live_agent_handoff: Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgs]] = ..., output_audio_text: Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageOutputAudioTextArgs]] = ..., payload: Optional[pulumi.Input[_builtins.str]] = ..., play_audio: Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessagePlayAudioArgs]] = ..., telephony_transfer_call: Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgs]] = ..., text: Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageTextArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel.setter
    def channel(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(self) -> Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageConversationSuccessArgs]]:
        
        ...
    
    @conversation_success.setter
    def conversation_success(self, value: Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageConversationSuccessArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(self) -> Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgs]]:
        
        ...
    
    @live_agent_handoff.setter
    def live_agent_handoff(self, value: Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(self) -> Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageOutputAudioTextArgs]]:
        
        ...
    
    @output_audio_text.setter
    def output_audio_text(self, value: Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageOutputAudioTextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @payload.setter
    def payload(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(self) -> Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessagePlayAudioArgs]]:
        
        ...
    
    @play_audio.setter
    def play_audio(self, value: Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessagePlayAudioArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(self) -> Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgs]]:
        
        ...
    
    @telephony_transfer_call.setter
    def telephony_transfer_call(self, value: Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageTextArgs]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[CxPageEventHandlerTriggerFulfillmentMessageTextArgs]]): # -> None:
        ...
    


class CxPageEventHandlerTriggerFulfillmentMessageConversationSuccessArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageEventHandlerTriggerFulfillmentMessageConversationSuccessArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageEventHandlerTriggerFulfillmentMessageOutputAudioTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    ssml: NotRequired[pulumi.Input[_builtins.str]]
    text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageEventHandlerTriggerFulfillmentMessageOutputAudioTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., ssml: Optional[pulumi.Input[_builtins.str]] = ..., text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssml.setter
    def ssml(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageEventHandlerTriggerFulfillmentMessagePlayAudioArgsDict(TypedDict):
    audio_uri: pulumi.Input[_builtins.str]
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxPageEventHandlerTriggerFulfillmentMessagePlayAudioArgs:
    def __init__(__self__, *, audio_uri: pulumi.Input[_builtins.str], allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @audio_uri.setter
    def audio_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxPageEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgsDict(TypedDict):
    phone_number: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxPageEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgs:
    def __init__(__self__, *, phone_number: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxPageEventHandlerTriggerFulfillmentMessageTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    texts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CxPageEventHandlerTriggerFulfillmentMessageTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., texts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @texts.setter
    def texts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CxPageEventHandlerTriggerFulfillmentSetParameterActionArgsDict(TypedDict):
    parameter: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageEventHandlerTriggerFulfillmentSetParameterActionArgs:
    def __init__(__self__, *, parameter: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parameter.setter
    def parameter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageFormArgsDict(TypedDict):
    parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterArgsDict]]]]


@pulumi.input_type
class CxPageFormArgs:
    def __init__(__self__, *, parameters: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterArgs]]]]:
        
        ...
    
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterArgs]]]]): # -> None:
        ...
    


class CxPageFormParameterArgsDict(TypedDict):
    advanced_settings: NotRequired[pulumi.Input[CxPageFormParameterAdvancedSettingsArgsDict]]
    default_value: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    entity_type: NotRequired[pulumi.Input[_builtins.str]]
    fill_behavior: NotRequired[pulumi.Input[CxPageFormParameterFillBehaviorArgsDict]]
    is_list: NotRequired[pulumi.Input[_builtins.bool]]
    redact: NotRequired[pulumi.Input[_builtins.bool]]
    required: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxPageFormParameterArgs:
    def __init__(__self__, *, advanced_settings: Optional[pulumi.Input[CxPageFormParameterAdvancedSettingsArgs]] = ..., default_value: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., entity_type: Optional[pulumi.Input[_builtins.str]] = ..., fill_behavior: Optional[pulumi.Input[CxPageFormParameterFillBehaviorArgs]] = ..., is_list: Optional[pulumi.Input[_builtins.bool]] = ..., redact: Optional[pulumi.Input[_builtins.bool]] = ..., required: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(self) -> Optional[pulumi.Input[CxPageFormParameterAdvancedSettingsArgs]]:
        
        ...
    
    @advanced_settings.setter
    def advanced_settings(self, value: Optional[pulumi.Input[CxPageFormParameterAdvancedSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultValue")
    def default_value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_value.setter
    def default_value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityType")
    def entity_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @entity_type.setter
    def entity_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fillBehavior")
    def fill_behavior(self) -> Optional[pulumi.Input[CxPageFormParameterFillBehaviorArgs]]:
        
        ...
    
    @fill_behavior.setter
    def fill_behavior(self, value: Optional[pulumi.Input[CxPageFormParameterFillBehaviorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isList")
    def is_list(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_list.setter
    def is_list(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def redact(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @redact.setter
    def redact(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def required(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @required.setter
    def required(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxPageFormParameterAdvancedSettingsArgsDict(TypedDict):
    dtmf_settings: NotRequired[pulumi.Input[CxPageFormParameterAdvancedSettingsDtmfSettingsArgsDict]]


@pulumi.input_type
class CxPageFormParameterAdvancedSettingsArgs:
    def __init__(__self__, *, dtmf_settings: Optional[pulumi.Input[CxPageFormParameterAdvancedSettingsDtmfSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dtmfSettings")
    def dtmf_settings(self) -> Optional[pulumi.Input[CxPageFormParameterAdvancedSettingsDtmfSettingsArgs]]:
        
        ...
    
    @dtmf_settings.setter
    def dtmf_settings(self, value: Optional[pulumi.Input[CxPageFormParameterAdvancedSettingsDtmfSettingsArgs]]): # -> None:
        ...
    


class CxPageFormParameterAdvancedSettingsDtmfSettingsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    finish_digit: NotRequired[pulumi.Input[_builtins.str]]
    max_digits: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CxPageFormParameterAdvancedSettingsDtmfSettingsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., finish_digit: Optional[pulumi.Input[_builtins.str]] = ..., max_digits: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @finish_digit.setter
    def finish_digit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDigits")
    def max_digits(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_digits.setter
    def max_digits(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorArgsDict(TypedDict):
    initial_prompt_fulfillment: NotRequired[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentArgsDict]]
    reprompt_event_handlers: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerArgsDict]]]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorArgs:
    def __init__(__self__, *, initial_prompt_fulfillment: Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentArgs]] = ..., reprompt_event_handlers: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="initialPromptFulfillment")
    def initial_prompt_fulfillment(self) -> Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentArgs]]:
        
        ...
    
    @initial_prompt_fulfillment.setter
    def initial_prompt_fulfillment(self, value: Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="repromptEventHandlers")
    def reprompt_event_handlers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerArgs]]]]:
        
        ...
    
    @reprompt_event_handlers.setter
    def reprompt_event_handlers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerArgs]]]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorInitialPromptFulfillmentArgsDict(TypedDict):
    conditional_cases: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentConditionalCaseArgsDict]]]]
    messages: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageArgsDict]]]]
    return_partial_responses: NotRequired[pulumi.Input[_builtins.bool]]
    set_parameter_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentSetParameterActionArgsDict]]]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    webhook: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentArgs:
    def __init__(__self__, *, conditional_cases: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentConditionalCaseArgs]]]] = ..., messages: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageArgs]]]] = ..., return_partial_responses: Optional[pulumi.Input[_builtins.bool]] = ..., set_parameter_actions: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentSetParameterActionArgs]]]] = ..., tag: Optional[pulumi.Input[_builtins.str]] = ..., webhook: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentConditionalCaseArgs]]]]:
        
        ...
    
    @conditional_cases.setter
    def conditional_cases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentConditionalCaseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageArgs]]]]:
        
        ...
    
    @messages.setter
    def messages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @return_partial_responses.setter
    def return_partial_responses(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentSetParameterActionArgs]]]]:
        
        ...
    
    @set_parameter_actions.setter
    def set_parameter_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentSetParameterActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @webhook.setter
    def webhook(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorInitialPromptFulfillmentConditionalCaseArgsDict(TypedDict):
    cases: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentConditionalCaseArgs:
    def __init__(__self__, *, cases: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cases.setter
    def cases(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageArgsDict(TypedDict):
    channel: NotRequired[pulumi.Input[_builtins.str]]
    conversation_success: NotRequired[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageConversationSuccessArgsDict]]
    live_agent_handoff: NotRequired[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageLiveAgentHandoffArgsDict]]
    output_audio_text: NotRequired[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageOutputAudioTextArgsDict]]
    payload: NotRequired[pulumi.Input[_builtins.str]]
    play_audio: NotRequired[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessagePlayAudioArgsDict]]
    telephony_transfer_call: NotRequired[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageTelephonyTransferCallArgsDict]]
    text: NotRequired[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageTextArgsDict]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageArgs:
    def __init__(__self__, *, channel: Optional[pulumi.Input[_builtins.str]] = ..., conversation_success: Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageConversationSuccessArgs]] = ..., live_agent_handoff: Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageLiveAgentHandoffArgs]] = ..., output_audio_text: Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageOutputAudioTextArgs]] = ..., payload: Optional[pulumi.Input[_builtins.str]] = ..., play_audio: Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessagePlayAudioArgs]] = ..., telephony_transfer_call: Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageTelephonyTransferCallArgs]] = ..., text: Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageTextArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel.setter
    def channel(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(self) -> Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageConversationSuccessArgs]]:
        
        ...
    
    @conversation_success.setter
    def conversation_success(self, value: Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageConversationSuccessArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(self) -> Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageLiveAgentHandoffArgs]]:
        
        ...
    
    @live_agent_handoff.setter
    def live_agent_handoff(self, value: Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageLiveAgentHandoffArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(self) -> Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageOutputAudioTextArgs]]:
        
        ...
    
    @output_audio_text.setter
    def output_audio_text(self, value: Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageOutputAudioTextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @payload.setter
    def payload(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(self) -> Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessagePlayAudioArgs]]:
        
        ...
    
    @play_audio.setter
    def play_audio(self, value: Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessagePlayAudioArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(self) -> Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageTelephonyTransferCallArgs]]:
        
        ...
    
    @telephony_transfer_call.setter
    def telephony_transfer_call(self, value: Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageTelephonyTransferCallArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageTextArgs]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageTextArgs]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageConversationSuccessArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageConversationSuccessArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageLiveAgentHandoffArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageLiveAgentHandoffArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageOutputAudioTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    ssml: NotRequired[pulumi.Input[_builtins.str]]
    text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageOutputAudioTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., ssml: Optional[pulumi.Input[_builtins.str]] = ..., text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssml.setter
    def ssml(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessagePlayAudioArgsDict(TypedDict):
    audio_uri: pulumi.Input[_builtins.str]
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessagePlayAudioArgs:
    def __init__(__self__, *, audio_uri: pulumi.Input[_builtins.str], allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @audio_uri.setter
    def audio_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageTelephonyTransferCallArgsDict(TypedDict):
    phone_number: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageTelephonyTransferCallArgs:
    def __init__(__self__, *, phone_number: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    texts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentMessageTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., texts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @texts.setter
    def texts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorInitialPromptFulfillmentSetParameterActionArgsDict(TypedDict):
    parameter: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorInitialPromptFulfillmentSetParameterActionArgs:
    def __init__(__self__, *, parameter: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parameter.setter
    def parameter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorRepromptEventHandlerArgsDict(TypedDict):
    event: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    target_flow: NotRequired[pulumi.Input[_builtins.str]]
    target_page: NotRequired[pulumi.Input[_builtins.str]]
    trigger_fulfillment: NotRequired[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentArgsDict]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerArgs:
    def __init__(__self__, *, event: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., target_flow: Optional[pulumi.Input[_builtins.str]] = ..., target_page: Optional[pulumi.Input[_builtins.str]] = ..., trigger_fulfillment: Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def event(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @event.setter
    def event(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetFlow")
    def target_flow(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_flow.setter
    def target_flow(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPage")
    def target_page(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_page.setter
    def target_page(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerFulfillment")
    def trigger_fulfillment(self) -> Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentArgs]]:
        
        ...
    
    @trigger_fulfillment.setter
    def trigger_fulfillment(self, value: Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentArgs]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentArgsDict(TypedDict):
    conditional_cases: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentConditionalCaseArgsDict]]]]
    messages: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageArgsDict]]]]
    return_partial_responses: NotRequired[pulumi.Input[_builtins.bool]]
    set_parameter_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentSetParameterActionArgsDict]]]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    webhook: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentArgs:
    def __init__(__self__, *, conditional_cases: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentConditionalCaseArgs]]]] = ..., messages: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageArgs]]]] = ..., return_partial_responses: Optional[pulumi.Input[_builtins.bool]] = ..., set_parameter_actions: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentSetParameterActionArgs]]]] = ..., tag: Optional[pulumi.Input[_builtins.str]] = ..., webhook: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentConditionalCaseArgs]]]]:
        
        ...
    
    @conditional_cases.setter
    def conditional_cases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentConditionalCaseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageArgs]]]]:
        
        ...
    
    @messages.setter
    def messages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @return_partial_responses.setter
    def return_partial_responses(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentSetParameterActionArgs]]]]:
        
        ...
    
    @set_parameter_actions.setter
    def set_parameter_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentSetParameterActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @webhook.setter
    def webhook(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentConditionalCaseArgsDict(TypedDict):
    cases: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentConditionalCaseArgs:
    def __init__(__self__, *, cases: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cases.setter
    def cases(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageArgsDict(TypedDict):
    channel: NotRequired[pulumi.Input[_builtins.str]]
    conversation_success: NotRequired[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageConversationSuccessArgsDict]]
    live_agent_handoff: NotRequired[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgsDict]]
    output_audio_text: NotRequired[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageOutputAudioTextArgsDict]]
    payload: NotRequired[pulumi.Input[_builtins.str]]
    play_audio: NotRequired[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessagePlayAudioArgsDict]]
    telephony_transfer_call: NotRequired[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgsDict]]
    text: NotRequired[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageTextArgsDict]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageArgs:
    def __init__(__self__, *, channel: Optional[pulumi.Input[_builtins.str]] = ..., conversation_success: Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageConversationSuccessArgs]] = ..., live_agent_handoff: Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgs]] = ..., output_audio_text: Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageOutputAudioTextArgs]] = ..., payload: Optional[pulumi.Input[_builtins.str]] = ..., play_audio: Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessagePlayAudioArgs]] = ..., telephony_transfer_call: Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgs]] = ..., text: Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageTextArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel.setter
    def channel(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(self) -> Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageConversationSuccessArgs]]:
        
        ...
    
    @conversation_success.setter
    def conversation_success(self, value: Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageConversationSuccessArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(self) -> Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgs]]:
        
        ...
    
    @live_agent_handoff.setter
    def live_agent_handoff(self, value: Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(self) -> Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageOutputAudioTextArgs]]:
        
        ...
    
    @output_audio_text.setter
    def output_audio_text(self, value: Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageOutputAudioTextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @payload.setter
    def payload(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(self) -> Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessagePlayAudioArgs]]:
        
        ...
    
    @play_audio.setter
    def play_audio(self, value: Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessagePlayAudioArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(self) -> Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgs]]:
        
        ...
    
    @telephony_transfer_call.setter
    def telephony_transfer_call(self, value: Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageTextArgs]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageTextArgs]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageConversationSuccessArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageConversationSuccessArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageLiveAgentHandoffArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageOutputAudioTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    ssml: NotRequired[pulumi.Input[_builtins.str]]
    text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageOutputAudioTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., ssml: Optional[pulumi.Input[_builtins.str]] = ..., text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssml.setter
    def ssml(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessagePlayAudioArgsDict(TypedDict):
    audio_uri: pulumi.Input[_builtins.str]
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessagePlayAudioArgs:
    def __init__(__self__, *, audio_uri: pulumi.Input[_builtins.str], allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @audio_uri.setter
    def audio_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgsDict(TypedDict):
    phone_number: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageTelephonyTransferCallArgs:
    def __init__(__self__, *, phone_number: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    texts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentMessageTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., texts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @texts.setter
    def texts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentSetParameterActionArgsDict(TypedDict):
    parameter: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageFormParameterFillBehaviorRepromptEventHandlerTriggerFulfillmentSetParameterActionArgs:
    def __init__(__self__, *, parameter: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parameter.setter
    def parameter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsArgsDict(TypedDict):
    data_store_connections: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsDataStoreConnectionArgsDict]]]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    target_flow: NotRequired[pulumi.Input[_builtins.str]]
    target_page: NotRequired[pulumi.Input[_builtins.str]]
    trigger_fulfillment: NotRequired[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentArgsDict]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsArgs:
    def __init__(__self__, *, data_store_connections: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsDataStoreConnectionArgs]]]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., target_flow: Optional[pulumi.Input[_builtins.str]] = ..., target_page: Optional[pulumi.Input[_builtins.str]] = ..., trigger_fulfillment: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreConnections")
    def data_store_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsDataStoreConnectionArgs]]]]:
        
        ...
    
    @data_store_connections.setter
    def data_store_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsDataStoreConnectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetFlow")
    def target_flow(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_flow.setter
    def target_flow(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPage")
    def target_page(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_page.setter
    def target_page(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerFulfillment")
    def trigger_fulfillment(self) -> Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentArgs]]:
        
        ...
    
    @trigger_fulfillment.setter
    def trigger_fulfillment(self, value: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentArgs]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsDataStoreConnectionArgsDict(TypedDict):
    data_store: NotRequired[pulumi.Input[_builtins.str]]
    data_store_type: NotRequired[pulumi.Input[_builtins.str]]
    document_processing_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsDataStoreConnectionArgs:
    def __init__(__self__, *, data_store: Optional[pulumi.Input[_builtins.str]] = ..., data_store_type: Optional[pulumi.Input[_builtins.str]] = ..., document_processing_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_store.setter
    def data_store(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreType")
    def data_store_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_store_type.setter
    def data_store_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentProcessingMode")
    def document_processing_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @document_processing_mode.setter
    def document_processing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentArgsDict(TypedDict):
    advanced_settings: NotRequired[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsArgsDict]]
    conditional_cases: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentConditionalCaseArgsDict]]]]
    enable_generative_fallback: NotRequired[pulumi.Input[_builtins.bool]]
    messages: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageArgsDict]]]]
    return_partial_responses: NotRequired[pulumi.Input[_builtins.bool]]
    set_parameter_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentSetParameterActionArgsDict]]]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    webhook: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentArgs:
    def __init__(__self__, *, advanced_settings: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsArgs]] = ..., conditional_cases: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentConditionalCaseArgs]]]] = ..., enable_generative_fallback: Optional[pulumi.Input[_builtins.bool]] = ..., messages: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageArgs]]]] = ..., return_partial_responses: Optional[pulumi.Input[_builtins.bool]] = ..., set_parameter_actions: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentSetParameterActionArgs]]]] = ..., tag: Optional[pulumi.Input[_builtins.str]] = ..., webhook: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(self) -> Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsArgs]]:
        
        ...
    
    @advanced_settings.setter
    def advanced_settings(self, value: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentConditionalCaseArgs]]]]:
        
        ...
    
    @conditional_cases.setter
    def conditional_cases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentConditionalCaseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableGenerativeFallback")
    def enable_generative_fallback(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_generative_fallback.setter
    def enable_generative_fallback(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageArgs]]]]:
        
        ...
    
    @messages.setter
    def messages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @return_partial_responses.setter
    def return_partial_responses(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentSetParameterActionArgs]]]]:
        
        ...
    
    @set_parameter_actions.setter
    def set_parameter_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentSetParameterActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @webhook.setter
    def webhook(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsArgsDict(TypedDict):
    dtmf_settings: NotRequired[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettingsArgsDict]]
    logging_settings: NotRequired[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettingsArgsDict]]
    speech_settings: NotRequired[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettingsArgsDict]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsArgs:
    def __init__(__self__, *, dtmf_settings: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettingsArgs]] = ..., logging_settings: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettingsArgs]] = ..., speech_settings: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dtmfSettings")
    def dtmf_settings(self) -> Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettingsArgs]]:
        
        ...
    
    @dtmf_settings.setter
    def dtmf_settings(self, value: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingSettings")
    def logging_settings(self) -> Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettingsArgs]]:
        
        ...
    
    @logging_settings.setter
    def logging_settings(self, value: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="speechSettings")
    def speech_settings(self) -> Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettingsArgs]]:
        
        ...
    
    @speech_settings.setter
    def speech_settings(self, value: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettingsArgs]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettingsArgsDict(TypedDict):
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    endpointing_timeout_duration: NotRequired[pulumi.Input[_builtins.str]]
    finish_digit: NotRequired[pulumi.Input[_builtins.str]]
    interdigit_timeout_duration: NotRequired[pulumi.Input[_builtins.str]]
    max_digits: NotRequired[pulumi.Input[_builtins.int]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsDtmfSettingsArgs:
    def __init__(__self__, *, enabled: Optional[pulumi.Input[_builtins.bool]] = ..., endpointing_timeout_duration: Optional[pulumi.Input[_builtins.str]] = ..., finish_digit: Optional[pulumi.Input[_builtins.str]] = ..., interdigit_timeout_duration: Optional[pulumi.Input[_builtins.str]] = ..., max_digits: Optional[pulumi.Input[_builtins.int]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointingTimeoutDuration")
    def endpointing_timeout_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @endpointing_timeout_duration.setter
    def endpointing_timeout_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @finish_digit.setter
    def finish_digit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="interdigitTimeoutDuration")
    def interdigit_timeout_duration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @interdigit_timeout_duration.setter
    def interdigit_timeout_duration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxDigits")
    def max_digits(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_digits.setter
    def max_digits(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettingsArgsDict(TypedDict):
    enable_consent_based_redaction: NotRequired[pulumi.Input[_builtins.bool]]
    enable_interaction_logging: NotRequired[pulumi.Input[_builtins.bool]]
    enable_stackdriver_logging: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsLoggingSettingsArgs:
    def __init__(__self__, *, enable_consent_based_redaction: Optional[pulumi.Input[_builtins.bool]] = ..., enable_interaction_logging: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableConsentBasedRedaction")
    def enable_consent_based_redaction(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_consent_based_redaction.setter
    def enable_consent_based_redaction(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInteractionLogging")
    def enable_interaction_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_interaction_logging.setter
    def enable_interaction_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    def enable_stackdriver_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_stackdriver_logging.setter
    def enable_stackdriver_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettingsArgsDict(TypedDict):
    endpointer_sensitivity: NotRequired[pulumi.Input[_builtins.int]]
    models: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    no_speech_timeout: NotRequired[pulumi.Input[_builtins.str]]
    use_timeout_based_endpointing: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentAdvancedSettingsSpeechSettingsArgs:
    def __init__(__self__, *, endpointer_sensitivity: Optional[pulumi.Input[_builtins.int]] = ..., models: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., no_speech_timeout: Optional[pulumi.Input[_builtins.str]] = ..., use_timeout_based_endpointing: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="endpointerSensitivity")
    def endpointer_sensitivity(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @endpointer_sensitivity.setter
    def endpointer_sensitivity(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def models(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @models.setter
    def models(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="noSpeechTimeout")
    def no_speech_timeout(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @no_speech_timeout.setter
    def no_speech_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="useTimeoutBasedEndpointing")
    def use_timeout_based_endpointing(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @use_timeout_based_endpointing.setter
    def use_timeout_based_endpointing(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentConditionalCaseArgsDict(TypedDict):
    cases: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentConditionalCaseArgs:
    def __init__(__self__, *, cases: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cases.setter
    def cases(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageArgsDict(TypedDict):
    channel: NotRequired[pulumi.Input[_builtins.str]]
    conversation_success: NotRequired[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccessArgsDict]]
    end_interactions: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteractionArgsDict]]]]
    knowledge_info_card: NotRequired[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCardArgsDict]]
    live_agent_handoff: NotRequired[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoffArgsDict]]
    mixed_audios: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioArgsDict]]]]
    output_audio_text: NotRequired[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioTextArgsDict]]
    payload: NotRequired[pulumi.Input[_builtins.str]]
    play_audio: NotRequired[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudioArgsDict]]
    telephony_transfer_call: NotRequired[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCallArgsDict]]
    text: NotRequired[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageTextArgsDict]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageArgs:
    def __init__(__self__, *, channel: Optional[pulumi.Input[_builtins.str]] = ..., conversation_success: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccessArgs]] = ..., end_interactions: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteractionArgs]]]] = ..., knowledge_info_card: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCardArgs]] = ..., live_agent_handoff: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoffArgs]] = ..., mixed_audios: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioArgs]]]] = ..., output_audio_text: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioTextArgs]] = ..., payload: Optional[pulumi.Input[_builtins.str]] = ..., play_audio: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudioArgs]] = ..., telephony_transfer_call: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCallArgs]] = ..., text: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageTextArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel.setter
    def channel(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(self) -> Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccessArgs]]:
        
        ...
    
    @conversation_success.setter
    def conversation_success(self, value: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccessArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endInteractions")
    def end_interactions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteractionArgs]]]]:
        
        ...
    
    @end_interactions.setter
    def end_interactions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteractionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeInfoCard")
    def knowledge_info_card(self) -> Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCardArgs]]:
        
        ...
    
    @knowledge_info_card.setter
    def knowledge_info_card(self, value: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCardArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(self) -> Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoffArgs]]:
        
        ...
    
    @live_agent_handoff.setter
    def live_agent_handoff(self, value: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoffArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="mixedAudios")
    def mixed_audios(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioArgs]]]]:
        
        ...
    
    @mixed_audios.setter
    def mixed_audios(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(self) -> Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioTextArgs]]:
        
        ...
    
    @output_audio_text.setter
    def output_audio_text(self, value: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioTextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @payload.setter
    def payload(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(self) -> Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudioArgs]]:
        
        ...
    
    @play_audio.setter
    def play_audio(self, value: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudioArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(self) -> Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCallArgs]]:
        
        ...
    
    @telephony_transfer_call.setter
    def telephony_transfer_call(self, value: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCallArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageTextArgs]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageTextArgs]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccessArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageConversationSuccessArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteractionArgsDict(TypedDict):
    ...


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageEndInteractionArgs:
    def __init__(__self__) -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCardArgsDict(TypedDict):
    ...


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageKnowledgeInfoCardArgs:
    def __init__(__self__) -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoffArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageLiveAgentHandoffArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioArgsDict(TypedDict):
    segments: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegmentArgsDict]]]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioArgs:
    def __init__(__self__, *, segments: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegmentArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def segments(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegmentArgs]]]]:
        
        ...
    
    @segments.setter
    def segments(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegmentArgs]]]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegmentArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    audio: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageMixedAudioSegmentArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., audio: Optional[pulumi.Input[_builtins.str]] = ..., uri: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def audio(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @audio.setter
    def audio(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    ssml: NotRequired[pulumi.Input[_builtins.str]]
    text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageOutputAudioTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., ssml: Optional[pulumi.Input[_builtins.str]] = ..., text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssml.setter
    def ssml(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudioArgsDict(TypedDict):
    audio_uri: pulumi.Input[_builtins.str]
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessagePlayAudioArgs:
    def __init__(__self__, *, audio_uri: pulumi.Input[_builtins.str], allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @audio_uri.setter
    def audio_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCallArgsDict(TypedDict):
    phone_number: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageTelephonyTransferCallArgs:
    def __init__(__self__, *, phone_number: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    texts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentMessageTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., texts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @texts.setter
    def texts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CxPageKnowledgeConnectorSettingsTriggerFulfillmentSetParameterActionArgsDict(TypedDict):
    parameter: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageKnowledgeConnectorSettingsTriggerFulfillmentSetParameterActionArgs:
    def __init__(__self__, *, parameter: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parameter.setter
    def parameter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageTransitionRouteArgsDict(TypedDict):
    condition: NotRequired[pulumi.Input[_builtins.str]]
    intent: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    target_flow: NotRequired[pulumi.Input[_builtins.str]]
    target_page: NotRequired[pulumi.Input[_builtins.str]]
    trigger_fulfillment: NotRequired[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentArgsDict]]


@pulumi.input_type
class CxPageTransitionRouteArgs:
    def __init__(__self__, *, condition: Optional[pulumi.Input[_builtins.str]] = ..., intent: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., target_flow: Optional[pulumi.Input[_builtins.str]] = ..., target_page: Optional[pulumi.Input[_builtins.str]] = ..., trigger_fulfillment: Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def intent(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @intent.setter
    def intent(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetFlow")
    def target_flow(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_flow.setter
    def target_flow(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetPage")
    def target_page(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @target_page.setter
    def target_page(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggerFulfillment")
    def trigger_fulfillment(self) -> Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentArgs]]:
        
        ...
    
    @trigger_fulfillment.setter
    def trigger_fulfillment(self, value: Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentArgs]]): # -> None:
        ...
    


class CxPageTransitionRouteTriggerFulfillmentArgsDict(TypedDict):
    conditional_cases: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentConditionalCaseArgsDict]]]]
    messages: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageArgsDict]]]]
    return_partial_responses: NotRequired[pulumi.Input[_builtins.bool]]
    set_parameter_actions: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentSetParameterActionArgsDict]]]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    webhook: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageTransitionRouteTriggerFulfillmentArgs:
    def __init__(__self__, *, conditional_cases: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentConditionalCaseArgs]]]] = ..., messages: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageArgs]]]] = ..., return_partial_responses: Optional[pulumi.Input[_builtins.bool]] = ..., set_parameter_actions: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentSetParameterActionArgs]]]] = ..., tag: Optional[pulumi.Input[_builtins.str]] = ..., webhook: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionalCases")
    def conditional_cases(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentConditionalCaseArgs]]]]:
        
        ...
    
    @conditional_cases.setter
    def conditional_cases(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentConditionalCaseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageArgs]]]]:
        
        ...
    
    @messages.setter
    def messages(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="returnPartialResponses")
    def return_partial_responses(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @return_partial_responses.setter
    def return_partial_responses(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="setParameterActions")
    def set_parameter_actions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentSetParameterActionArgs]]]]:
        
        ...
    
    @set_parameter_actions.setter
    def set_parameter_actions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentSetParameterActionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def webhook(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @webhook.setter
    def webhook(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageTransitionRouteTriggerFulfillmentConditionalCaseArgsDict(TypedDict):
    cases: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageTransitionRouteTriggerFulfillmentConditionalCaseArgs:
    def __init__(__self__, *, cases: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cases(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @cases.setter
    def cases(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageTransitionRouteTriggerFulfillmentMessageArgsDict(TypedDict):
    channel: NotRequired[pulumi.Input[_builtins.str]]
    conversation_success: NotRequired[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageConversationSuccessArgsDict]]
    live_agent_handoff: NotRequired[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageLiveAgentHandoffArgsDict]]
    output_audio_text: NotRequired[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageOutputAudioTextArgsDict]]
    payload: NotRequired[pulumi.Input[_builtins.str]]
    play_audio: NotRequired[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessagePlayAudioArgsDict]]
    telephony_transfer_call: NotRequired[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageTelephonyTransferCallArgsDict]]
    text: NotRequired[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageTextArgsDict]]


@pulumi.input_type
class CxPageTransitionRouteTriggerFulfillmentMessageArgs:
    def __init__(__self__, *, channel: Optional[pulumi.Input[_builtins.str]] = ..., conversation_success: Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageConversationSuccessArgs]] = ..., live_agent_handoff: Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageLiveAgentHandoffArgs]] = ..., output_audio_text: Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageOutputAudioTextArgs]] = ..., payload: Optional[pulumi.Input[_builtins.str]] = ..., play_audio: Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessagePlayAudioArgs]] = ..., telephony_transfer_call: Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageTelephonyTransferCallArgs]] = ..., text: Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageTextArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def channel(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @channel.setter
    def channel(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationSuccess")
    def conversation_success(self) -> Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageConversationSuccessArgs]]:
        
        ...
    
    @conversation_success.setter
    def conversation_success(self, value: Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageConversationSuccessArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="liveAgentHandoff")
    def live_agent_handoff(self) -> Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageLiveAgentHandoffArgs]]:
        
        ...
    
    @live_agent_handoff.setter
    def live_agent_handoff(self, value: Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageLiveAgentHandoffArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputAudioText")
    def output_audio_text(self) -> Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageOutputAudioTextArgs]]:
        
        ...
    
    @output_audio_text.setter
    def output_audio_text(self, value: Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageOutputAudioTextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def payload(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @payload.setter
    def payload(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="playAudio")
    def play_audio(self) -> Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessagePlayAudioArgs]]:
        
        ...
    
    @play_audio.setter
    def play_audio(self, value: Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessagePlayAudioArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="telephonyTransferCall")
    def telephony_transfer_call(self) -> Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageTelephonyTransferCallArgs]]:
        
        ...
    
    @telephony_transfer_call.setter
    def telephony_transfer_call(self, value: Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageTelephonyTransferCallArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageTextArgs]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[CxPageTransitionRouteTriggerFulfillmentMessageTextArgs]]): # -> None:
        ...
    


class CxPageTransitionRouteTriggerFulfillmentMessageConversationSuccessArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageTransitionRouteTriggerFulfillmentMessageConversationSuccessArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageTransitionRouteTriggerFulfillmentMessageLiveAgentHandoffArgsDict(TypedDict):
    metadata: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageTransitionRouteTriggerFulfillmentMessageLiveAgentHandoffArgs:
    def __init__(__self__, *, metadata: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageTransitionRouteTriggerFulfillmentMessageOutputAudioTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    ssml: NotRequired[pulumi.Input[_builtins.str]]
    text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageTransitionRouteTriggerFulfillmentMessageOutputAudioTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., ssml: Optional[pulumi.Input[_builtins.str]] = ..., text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def ssml(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @ssml.setter
    def ssml(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPageTransitionRouteTriggerFulfillmentMessagePlayAudioArgsDict(TypedDict):
    audio_uri: pulumi.Input[_builtins.str]
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxPageTransitionRouteTriggerFulfillmentMessagePlayAudioArgs:
    def __init__(__self__, *, audio_uri: pulumi.Input[_builtins.str], allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioUri")
    def audio_uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @audio_uri.setter
    def audio_uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxPageTransitionRouteTriggerFulfillmentMessageTelephonyTransferCallArgsDict(TypedDict):
    phone_number: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxPageTransitionRouteTriggerFulfillmentMessageTelephonyTransferCallArgs:
    def __init__(__self__, *, phone_number: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="phoneNumber")
    def phone_number(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @phone_number.setter
    def phone_number(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxPageTransitionRouteTriggerFulfillmentMessageTextArgsDict(TypedDict):
    allow_playback_interruption: NotRequired[pulumi.Input[_builtins.bool]]
    texts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CxPageTransitionRouteTriggerFulfillmentMessageTextArgs:
    def __init__(__self__, *, allow_playback_interruption: Optional[pulumi.Input[_builtins.bool]] = ..., texts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowPlaybackInterruption")
    def allow_playback_interruption(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @allow_playback_interruption.setter
    def allow_playback_interruption(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @texts.setter
    def texts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CxPageTransitionRouteTriggerFulfillmentSetParameterActionArgsDict(TypedDict):
    parameter: NotRequired[pulumi.Input[_builtins.str]]
    value: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPageTransitionRouteTriggerFulfillmentSetParameterActionArgs:
    def __init__(__self__, *, parameter: Optional[pulumi.Input[_builtins.str]] = ..., value: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameter(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parameter.setter
    def parameter(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPlaybookInstructionArgsDict(TypedDict):
    guidelines: NotRequired[pulumi.Input[_builtins.str]]
    steps: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxPlaybookInstructionStepArgsDict]]]]


@pulumi.input_type
class CxPlaybookInstructionArgs:
    def __init__(__self__, *, guidelines: Optional[pulumi.Input[_builtins.str]] = ..., steps: Optional[pulumi.Input[Sequence[pulumi.Input[CxPlaybookInstructionStepArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def guidelines(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @guidelines.setter
    def guidelines(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def steps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxPlaybookInstructionStepArgs]]]]:
        
        ...
    
    @steps.setter
    def steps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxPlaybookInstructionStepArgs]]]]): # -> None:
        ...
    


class CxPlaybookInstructionStepArgsDict(TypedDict):
    steps: NotRequired[pulumi.Input[_builtins.str]]
    text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPlaybookInstructionStepArgs:
    def __init__(__self__, *, steps: Optional[pulumi.Input[_builtins.str]] = ..., text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def steps(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @steps.setter
    def steps(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxPlaybookLlmModelSettingsArgsDict(TypedDict):
    model: NotRequired[pulumi.Input[_builtins.str]]
    prompt_text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxPlaybookLlmModelSettingsArgs:
    def __init__(__self__, *, model: Optional[pulumi.Input[_builtins.str]] = ..., prompt_text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="promptText")
    def prompt_text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prompt_text.setter
    def prompt_text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxSecuritySettingsAudioExportSettingsArgsDict(TypedDict):
    audio_export_pattern: NotRequired[pulumi.Input[_builtins.str]]
    audio_format: NotRequired[pulumi.Input[_builtins.str]]
    enable_audio_redaction: NotRequired[pulumi.Input[_builtins.bool]]
    gcs_bucket: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxSecuritySettingsAudioExportSettingsArgs:
    def __init__(__self__, *, audio_export_pattern: Optional[pulumi.Input[_builtins.str]] = ..., audio_format: Optional[pulumi.Input[_builtins.str]] = ..., enable_audio_redaction: Optional[pulumi.Input[_builtins.bool]] = ..., gcs_bucket: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioExportPattern")
    def audio_export_pattern(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @audio_export_pattern.setter
    def audio_export_pattern(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioFormat")
    def audio_format(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @audio_format.setter
    def audio_format(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableAudioRedaction")
    def enable_audio_redaction(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_audio_redaction.setter
    def enable_audio_redaction(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsBucket")
    def gcs_bucket(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @gcs_bucket.setter
    def gcs_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxSecuritySettingsInsightsExportSettingsArgsDict(TypedDict):
    enable_insights_export: pulumi.Input[_builtins.bool]


@pulumi.input_type
class CxSecuritySettingsInsightsExportSettingsArgs:
    def __init__(__self__, *, enable_insights_export: pulumi.Input[_builtins.bool]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableInsightsExport")
    def enable_insights_export(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @enable_insights_export.setter
    def enable_insights_export(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    


class CxTestCaseLastTestResultArgsDict(TypedDict):
    conversation_turns: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxTestCaseLastTestResultConversationTurnArgsDict]]]]
    environment: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    test_result: NotRequired[pulumi.Input[_builtins.str]]
    test_time: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxTestCaseLastTestResultArgs:
    def __init__(__self__, *, conversation_turns: Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseLastTestResultConversationTurnArgs]]]] = ..., environment: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., test_result: Optional[pulumi.Input[_builtins.str]] = ..., test_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationTurns")
    def conversation_turns(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseLastTestResultConversationTurnArgs]]]]:
        
        ...
    
    @conversation_turns.setter
    def conversation_turns(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseLastTestResultConversationTurnArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def environment(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @environment.setter
    def environment(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testResult")
    def test_result(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @test_result.setter
    def test_result(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="testTime")
    def test_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @test_time.setter
    def test_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxTestCaseLastTestResultConversationTurnArgsDict(TypedDict):
    user_input: NotRequired[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputArgsDict]]
    virtual_agent_output: NotRequired[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputArgsDict]]


@pulumi.input_type
class CxTestCaseLastTestResultConversationTurnArgs:
    def __init__(__self__, *, user_input: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputArgs]] = ..., virtual_agent_output: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInput")
    def user_input(self) -> Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputArgs]]:
        
        ...
    
    @user_input.setter
    def user_input(self, value: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualAgentOutput")
    def virtual_agent_output(self) -> Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputArgs]]:
        
        ...
    
    @virtual_agent_output.setter
    def virtual_agent_output(self, value: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputArgs]]): # -> None:
        ...
    


class CxTestCaseLastTestResultConversationTurnUserInputArgsDict(TypedDict):
    enable_sentiment_analysis: NotRequired[pulumi.Input[_builtins.bool]]
    injected_parameters: NotRequired[pulumi.Input[_builtins.str]]
    input: NotRequired[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputArgsDict]]
    is_webhook_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxTestCaseLastTestResultConversationTurnUserInputArgs:
    def __init__(__self__, *, enable_sentiment_analysis: Optional[pulumi.Input[_builtins.bool]] = ..., injected_parameters: Optional[pulumi.Input[_builtins.str]] = ..., input: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputArgs]] = ..., is_webhook_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSentimentAnalysis")
    def enable_sentiment_analysis(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_sentiment_analysis.setter
    def enable_sentiment_analysis(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="injectedParameters")
    def injected_parameters(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @injected_parameters.setter
    def injected_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isWebhookEnabled")
    def is_webhook_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_webhook_enabled.setter
    def is_webhook_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxTestCaseLastTestResultConversationTurnUserInputInputArgsDict(TypedDict):
    dtmf: NotRequired[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputDtmfArgsDict]]
    event: NotRequired[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputEventArgsDict]]
    language_code: NotRequired[pulumi.Input[_builtins.str]]
    text: NotRequired[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputTextArgsDict]]


@pulumi.input_type
class CxTestCaseLastTestResultConversationTurnUserInputInputArgs:
    def __init__(__self__, *, dtmf: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputDtmfArgs]] = ..., event: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputEventArgs]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., text: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputTextArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dtmf(self) -> Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputDtmfArgs]]:
        
        ...
    
    @dtmf.setter
    def dtmf(self, value: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputDtmfArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def event(self) -> Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputEventArgs]]:
        
        ...
    
    @event.setter
    def event(self, value: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputEventArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputTextArgs]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnUserInputInputTextArgs]]): # -> None:
        ...
    


class CxTestCaseLastTestResultConversationTurnUserInputInputDtmfArgsDict(TypedDict):
    digits: NotRequired[pulumi.Input[_builtins.str]]
    finish_digit: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxTestCaseLastTestResultConversationTurnUserInputInputDtmfArgs:
    def __init__(__self__, *, digits: Optional[pulumi.Input[_builtins.str]] = ..., finish_digit: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def digits(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @digits.setter
    def digits(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @finish_digit.setter
    def finish_digit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxTestCaseLastTestResultConversationTurnUserInputInputEventArgsDict(TypedDict):
    event: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxTestCaseLastTestResultConversationTurnUserInputInputEventArgs:
    def __init__(__self__, *, event: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def event(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event.setter
    def event(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxTestCaseLastTestResultConversationTurnUserInputInputTextArgsDict(TypedDict):
    text: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxTestCaseLastTestResultConversationTurnUserInputInputTextArgs:
    def __init__(__self__, *, text: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @text.setter
    def text(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputArgsDict(TypedDict):
    current_page: NotRequired[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputCurrentPageArgsDict]]
    differences: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputDifferenceArgsDict]]]]
    session_parameters: NotRequired[pulumi.Input[_builtins.str]]
    status: NotRequired[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputStatusArgsDict]]
    text_responses: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTextResponseArgsDict]]]]
    triggered_intent: NotRequired[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTriggeredIntentArgsDict]]


@pulumi.input_type
class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputArgs:
    def __init__(__self__, *, current_page: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputCurrentPageArgs]] = ..., differences: Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputDifferenceArgs]]]] = ..., session_parameters: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputStatusArgs]] = ..., text_responses: Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTextResponseArgs]]]] = ..., triggered_intent: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTriggeredIntentArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentPage")
    def current_page(self) -> Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputCurrentPageArgs]]:
        
        ...
    
    @current_page.setter
    def current_page(self, value: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputCurrentPageArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def differences(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputDifferenceArgs]]]]:
        
        ...
    
    @differences.setter
    def differences(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputDifferenceArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionParameters")
    def session_parameters(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_parameters.setter
    def session_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputStatusArgs]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputStatusArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="textResponses")
    def text_responses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTextResponseArgs]]]]:
        
        ...
    
    @text_responses.setter
    def text_responses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTextResponseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggeredIntent")
    def triggered_intent(self) -> Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTriggeredIntentArgs]]:
        
        ...
    
    @triggered_intent.setter
    def triggered_intent(self, value: Optional[pulumi.Input[CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTriggeredIntentArgs]]): # -> None:
        ...
    


class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputCurrentPageArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputCurrentPageArgs:
    def __init__(__self__, *, display_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputDifferenceArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputDifferenceArgs:
    def __init__(__self__, *, description: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputStatusArgsDict(TypedDict):
    code: NotRequired[pulumi.Input[_builtins.int]]
    details: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputStatusArgs:
    def __init__(__self__, *, code: Optional[pulumi.Input[_builtins.int]] = ..., details: Optional[pulumi.Input[_builtins.str]] = ..., message: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @code.setter
    def code(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @details.setter
    def details(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTextResponseArgsDict(TypedDict):
    texts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTextResponseArgs:
    def __init__(__self__, *, texts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @texts.setter
    def texts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTriggeredIntentArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxTestCaseLastTestResultConversationTurnVirtualAgentOutputTriggeredIntentArgs:
    def __init__(__self__, *, display_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxTestCaseTestCaseConversationTurnArgsDict(TypedDict):
    user_input: NotRequired[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputArgsDict]]
    virtual_agent_output: NotRequired[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputArgsDict]]


@pulumi.input_type
class CxTestCaseTestCaseConversationTurnArgs:
    def __init__(__self__, *, user_input: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputArgs]] = ..., virtual_agent_output: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="userInput")
    def user_input(self) -> Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputArgs]]:
        
        ...
    
    @user_input.setter
    def user_input(self, value: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="virtualAgentOutput")
    def virtual_agent_output(self) -> Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputArgs]]:
        
        ...
    
    @virtual_agent_output.setter
    def virtual_agent_output(self, value: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputArgs]]): # -> None:
        ...
    


class CxTestCaseTestCaseConversationTurnUserInputArgsDict(TypedDict):
    enable_sentiment_analysis: NotRequired[pulumi.Input[_builtins.bool]]
    injected_parameters: NotRequired[pulumi.Input[_builtins.str]]
    input: NotRequired[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputArgsDict]]
    is_webhook_enabled: NotRequired[pulumi.Input[_builtins.bool]]


@pulumi.input_type
class CxTestCaseTestCaseConversationTurnUserInputArgs:
    def __init__(__self__, *, enable_sentiment_analysis: Optional[pulumi.Input[_builtins.bool]] = ..., injected_parameters: Optional[pulumi.Input[_builtins.str]] = ..., input: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputArgs]] = ..., is_webhook_enabled: Optional[pulumi.Input[_builtins.bool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSentimentAnalysis")
    def enable_sentiment_analysis(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_sentiment_analysis.setter
    def enable_sentiment_analysis(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="injectedParameters")
    def injected_parameters(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @injected_parameters.setter
    def injected_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def input(self) -> Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputArgs]]:
        
        ...
    
    @input.setter
    def input(self, value: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="isWebhookEnabled")
    def is_webhook_enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @is_webhook_enabled.setter
    def is_webhook_enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    


class CxTestCaseTestCaseConversationTurnUserInputInputArgsDict(TypedDict):
    dtmf: NotRequired[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputDtmfArgsDict]]
    event: NotRequired[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputEventArgsDict]]
    language_code: NotRequired[pulumi.Input[_builtins.str]]
    text: NotRequired[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputTextArgsDict]]


@pulumi.input_type
class CxTestCaseTestCaseConversationTurnUserInputInputArgs:
    def __init__(__self__, *, dtmf: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputDtmfArgs]] = ..., event: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputEventArgs]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., text: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputTextArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dtmf(self) -> Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputDtmfArgs]]:
        
        ...
    
    @dtmf.setter
    def dtmf(self, value: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputDtmfArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def event(self) -> Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputEventArgs]]:
        
        ...
    
    @event.setter
    def event(self, value: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputEventArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputTextArgs]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnUserInputInputTextArgs]]): # -> None:
        ...
    


class CxTestCaseTestCaseConversationTurnUserInputInputDtmfArgsDict(TypedDict):
    digits: NotRequired[pulumi.Input[_builtins.str]]
    finish_digit: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxTestCaseTestCaseConversationTurnUserInputInputDtmfArgs:
    def __init__(__self__, *, digits: Optional[pulumi.Input[_builtins.str]] = ..., finish_digit: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def digits(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @digits.setter
    def digits(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="finishDigit")
    def finish_digit(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @finish_digit.setter
    def finish_digit(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxTestCaseTestCaseConversationTurnUserInputInputEventArgsDict(TypedDict):
    event: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxTestCaseTestCaseConversationTurnUserInputInputEventArgs:
    def __init__(__self__, *, event: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def event(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @event.setter
    def event(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxTestCaseTestCaseConversationTurnUserInputInputTextArgsDict(TypedDict):
    text: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxTestCaseTestCaseConversationTurnUserInputInputTextArgs:
    def __init__(__self__, *, text: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @text.setter
    def text(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxTestCaseTestCaseConversationTurnVirtualAgentOutputArgsDict(TypedDict):
    current_page: NotRequired[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputCurrentPageArgsDict]]
    session_parameters: NotRequired[pulumi.Input[_builtins.str]]
    text_responses: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputTextResponseArgsDict]]]]
    triggered_intent: NotRequired[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputTriggeredIntentArgsDict]]


@pulumi.input_type
class CxTestCaseTestCaseConversationTurnVirtualAgentOutputArgs:
    def __init__(__self__, *, current_page: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputCurrentPageArgs]] = ..., session_parameters: Optional[pulumi.Input[_builtins.str]] = ..., text_responses: Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputTextResponseArgs]]]] = ..., triggered_intent: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputTriggeredIntentArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="currentPage")
    def current_page(self) -> Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputCurrentPageArgs]]:
        
        ...
    
    @current_page.setter
    def current_page(self, value: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputCurrentPageArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="sessionParameters")
    def session_parameters(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @session_parameters.setter
    def session_parameters(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="textResponses")
    def text_responses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputTextResponseArgs]]]]:
        
        ...
    
    @text_responses.setter
    def text_responses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputTextResponseArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="triggeredIntent")
    def triggered_intent(self) -> Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputTriggeredIntentArgs]]:
        
        ...
    
    @triggered_intent.setter
    def triggered_intent(self, value: Optional[pulumi.Input[CxTestCaseTestCaseConversationTurnVirtualAgentOutputTriggeredIntentArgs]]): # -> None:
        ...
    


class CxTestCaseTestCaseConversationTurnVirtualAgentOutputCurrentPageArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxTestCaseTestCaseConversationTurnVirtualAgentOutputCurrentPageArgs:
    def __init__(__self__, *, display_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxTestCaseTestCaseConversationTurnVirtualAgentOutputTextResponseArgsDict(TypedDict):
    texts: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CxTestCaseTestCaseConversationTurnVirtualAgentOutputTextResponseArgs:
    def __init__(__self__, *, texts: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def texts(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @texts.setter
    def texts(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CxTestCaseTestCaseConversationTurnVirtualAgentOutputTriggeredIntentArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxTestCaseTestCaseConversationTurnVirtualAgentOutputTriggeredIntentArgs:
    def __init__(__self__, *, display_name: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxTestCaseTestConfigArgsDict(TypedDict):
    flow: NotRequired[pulumi.Input[_builtins.str]]
    page: NotRequired[pulumi.Input[_builtins.str]]
    tracking_parameters: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CxTestCaseTestConfigArgs:
    def __init__(__self__, *, flow: Optional[pulumi.Input[_builtins.str]] = ..., page: Optional[pulumi.Input[_builtins.str]] = ..., tracking_parameters: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def flow(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @flow.setter
    def flow(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def page(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @page.setter
    def page(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="trackingParameters")
    def tracking_parameters(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tracking_parameters.setter
    def tracking_parameters(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CxToolConnectorSpecArgsDict(TypedDict):
    actions: pulumi.Input[Sequence[pulumi.Input[CxToolConnectorSpecActionArgsDict]]]
    name: pulumi.Input[_builtins.str]
    end_user_auth_config: NotRequired[pulumi.Input[CxToolConnectorSpecEndUserAuthConfigArgsDict]]


@pulumi.input_type
class CxToolConnectorSpecArgs:
    def __init__(__self__, *, actions: pulumi.Input[Sequence[pulumi.Input[CxToolConnectorSpecActionArgs]]], name: pulumi.Input[_builtins.str], end_user_auth_config: Optional[pulumi.Input[CxToolConnectorSpecEndUserAuthConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[CxToolConnectorSpecActionArgs]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[CxToolConnectorSpecActionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endUserAuthConfig")
    def end_user_auth_config(self) -> Optional[pulumi.Input[CxToolConnectorSpecEndUserAuthConfigArgs]]:
        
        ...
    
    @end_user_auth_config.setter
    def end_user_auth_config(self, value: Optional[pulumi.Input[CxToolConnectorSpecEndUserAuthConfigArgs]]): # -> None:
        ...
    


class CxToolConnectorSpecActionArgsDict(TypedDict):
    connection_action_id: NotRequired[pulumi.Input[_builtins.str]]
    entity_operation: NotRequired[pulumi.Input[CxToolConnectorSpecActionEntityOperationArgsDict]]
    input_fields: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    output_fields: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CxToolConnectorSpecActionArgs:
    def __init__(__self__, *, connection_action_id: Optional[pulumi.Input[_builtins.str]] = ..., entity_operation: Optional[pulumi.Input[CxToolConnectorSpecActionEntityOperationArgs]] = ..., input_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., output_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionActionId")
    def connection_action_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_action_id.setter
    def connection_action_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityOperation")
    def entity_operation(self) -> Optional[pulumi.Input[CxToolConnectorSpecActionEntityOperationArgs]]:
        
        ...
    
    @entity_operation.setter
    def entity_operation(self, value: Optional[pulumi.Input[CxToolConnectorSpecActionEntityOperationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputFields")
    def input_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @input_fields.setter
    def input_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputFields")
    def output_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @output_fields.setter
    def output_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CxToolConnectorSpecActionEntityOperationArgsDict(TypedDict):
    entity_id: pulumi.Input[_builtins.str]
    operation: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxToolConnectorSpecActionEntityOperationArgs:
    def __init__(__self__, *, entity_id: pulumi.Input[_builtins.str], operation: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @entity_id.setter
    def entity_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operation(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @operation.setter
    def operation(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxToolConnectorSpecEndUserAuthConfigArgsDict(TypedDict):
    oauth2_auth_code_config: NotRequired[pulumi.Input[CxToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfigArgsDict]]
    oauth2_jwt_bearer_config: NotRequired[pulumi.Input[CxToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfigArgsDict]]


@pulumi.input_type
class CxToolConnectorSpecEndUserAuthConfigArgs:
    def __init__(__self__, *, oauth2_auth_code_config: Optional[pulumi.Input[CxToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfigArgs]] = ..., oauth2_jwt_bearer_config: Optional[pulumi.Input[CxToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2AuthCodeConfig")
    def oauth2_auth_code_config(self) -> Optional[pulumi.Input[CxToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfigArgs]]:
        
        ...
    
    @oauth2_auth_code_config.setter
    def oauth2_auth_code_config(self, value: Optional[pulumi.Input[CxToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2JwtBearerConfig")
    def oauth2_jwt_bearer_config(self) -> Optional[pulumi.Input[CxToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfigArgs]]:
        
        ...
    
    @oauth2_jwt_bearer_config.setter
    def oauth2_jwt_bearer_config(self, value: Optional[pulumi.Input[CxToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfigArgs]]): # -> None:
        ...
    


class CxToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfigArgsDict(TypedDict):
    oauth_token: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfigArgs:
    def __init__(__self__, *, oauth_token: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthToken")
    def oauth_token(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @oauth_token.setter
    def oauth_token(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfigArgsDict(TypedDict):
    client_key: pulumi.Input[_builtins.str]
    issuer: pulumi.Input[_builtins.str]
    subject: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfigArgs:
    def __init__(__self__, *, client_key: pulumi.Input[_builtins.str], issuer: pulumi.Input[_builtins.str], subject: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_key.setter
    def client_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @subject.setter
    def subject(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxToolDataStoreSpecArgsDict(TypedDict):
    data_store_connections: pulumi.Input[Sequence[pulumi.Input[CxToolDataStoreSpecDataStoreConnectionArgsDict]]]
    fallback_prompt: pulumi.Input[CxToolDataStoreSpecFallbackPromptArgsDict]


@pulumi.input_type
class CxToolDataStoreSpecArgs:
    def __init__(__self__, *, data_store_connections: pulumi.Input[Sequence[pulumi.Input[CxToolDataStoreSpecDataStoreConnectionArgs]]], fallback_prompt: pulumi.Input[CxToolDataStoreSpecFallbackPromptArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreConnections")
    def data_store_connections(self) -> pulumi.Input[Sequence[pulumi.Input[CxToolDataStoreSpecDataStoreConnectionArgs]]]:
        
        ...
    
    @data_store_connections.setter
    def data_store_connections(self, value: pulumi.Input[Sequence[pulumi.Input[CxToolDataStoreSpecDataStoreConnectionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackPrompt")
    def fallback_prompt(self) -> pulumi.Input[CxToolDataStoreSpecFallbackPromptArgs]:
        
        ...
    
    @fallback_prompt.setter
    def fallback_prompt(self, value: pulumi.Input[CxToolDataStoreSpecFallbackPromptArgs]): # -> None:
        ...
    


class CxToolDataStoreSpecDataStoreConnectionArgsDict(TypedDict):
    data_store: NotRequired[pulumi.Input[_builtins.str]]
    data_store_type: NotRequired[pulumi.Input[_builtins.str]]
    document_processing_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxToolDataStoreSpecDataStoreConnectionArgs:
    def __init__(__self__, *, data_store: Optional[pulumi.Input[_builtins.str]] = ..., data_store_type: Optional[pulumi.Input[_builtins.str]] = ..., document_processing_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_store.setter
    def data_store(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreType")
    def data_store_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_store_type.setter
    def data_store_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentProcessingMode")
    def document_processing_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @document_processing_mode.setter
    def document_processing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxToolDataStoreSpecFallbackPromptArgsDict(TypedDict):
    ...


@pulumi.input_type
class CxToolDataStoreSpecFallbackPromptArgs:
    def __init__(__self__) -> None:
        ...
    


class CxToolFunctionSpecArgsDict(TypedDict):
    input_schema: NotRequired[pulumi.Input[_builtins.str]]
    output_schema: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxToolFunctionSpecArgs:
    def __init__(__self__, *, input_schema: Optional[pulumi.Input[_builtins.str]] = ..., output_schema: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputSchema")
    def input_schema(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @input_schema.setter
    def input_schema(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputSchema")
    def output_schema(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @output_schema.setter
    def output_schema(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxToolOpenApiSpecArgsDict(TypedDict):
    text_schema: pulumi.Input[_builtins.str]
    authentication: NotRequired[pulumi.Input[CxToolOpenApiSpecAuthenticationArgsDict]]
    service_directory_config: NotRequired[pulumi.Input[CxToolOpenApiSpecServiceDirectoryConfigArgsDict]]
    tls_config: NotRequired[pulumi.Input[CxToolOpenApiSpecTlsConfigArgsDict]]


@pulumi.input_type
class CxToolOpenApiSpecArgs:
    def __init__(__self__, *, text_schema: pulumi.Input[_builtins.str], authentication: Optional[pulumi.Input[CxToolOpenApiSpecAuthenticationArgs]] = ..., service_directory_config: Optional[pulumi.Input[CxToolOpenApiSpecServiceDirectoryConfigArgs]] = ..., tls_config: Optional[pulumi.Input[CxToolOpenApiSpecTlsConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textSchema")
    def text_schema(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @text_schema.setter
    def text_schema(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[CxToolOpenApiSpecAuthenticationArgs]]:
        
        ...
    
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[CxToolOpenApiSpecAuthenticationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(self) -> Optional[pulumi.Input[CxToolOpenApiSpecServiceDirectoryConfigArgs]]:
        
        ...
    
    @service_directory_config.setter
    def service_directory_config(self, value: Optional[pulumi.Input[CxToolOpenApiSpecServiceDirectoryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[pulumi.Input[CxToolOpenApiSpecTlsConfigArgs]]:
        
        ...
    
    @tls_config.setter
    def tls_config(self, value: Optional[pulumi.Input[CxToolOpenApiSpecTlsConfigArgs]]): # -> None:
        ...
    


class CxToolOpenApiSpecAuthenticationArgsDict(TypedDict):
    api_key_config: NotRequired[pulumi.Input[CxToolOpenApiSpecAuthenticationApiKeyConfigArgsDict]]
    bearer_token_config: NotRequired[pulumi.Input[CxToolOpenApiSpecAuthenticationBearerTokenConfigArgsDict]]
    oauth_config: NotRequired[pulumi.Input[CxToolOpenApiSpecAuthenticationOauthConfigArgsDict]]
    service_agent_auth_config: NotRequired[pulumi.Input[CxToolOpenApiSpecAuthenticationServiceAgentAuthConfigArgsDict]]


@pulumi.input_type
class CxToolOpenApiSpecAuthenticationArgs:
    def __init__(__self__, *, api_key_config: Optional[pulumi.Input[CxToolOpenApiSpecAuthenticationApiKeyConfigArgs]] = ..., bearer_token_config: Optional[pulumi.Input[CxToolOpenApiSpecAuthenticationBearerTokenConfigArgs]] = ..., oauth_config: Optional[pulumi.Input[CxToolOpenApiSpecAuthenticationOauthConfigArgs]] = ..., service_agent_auth_config: Optional[pulumi.Input[CxToolOpenApiSpecAuthenticationServiceAgentAuthConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyConfig")
    def api_key_config(self) -> Optional[pulumi.Input[CxToolOpenApiSpecAuthenticationApiKeyConfigArgs]]:
        
        ...
    
    @api_key_config.setter
    def api_key_config(self, value: Optional[pulumi.Input[CxToolOpenApiSpecAuthenticationApiKeyConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bearerTokenConfig")
    def bearer_token_config(self) -> Optional[pulumi.Input[CxToolOpenApiSpecAuthenticationBearerTokenConfigArgs]]:
        
        ...
    
    @bearer_token_config.setter
    def bearer_token_config(self, value: Optional[pulumi.Input[CxToolOpenApiSpecAuthenticationBearerTokenConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthConfig")
    def oauth_config(self) -> Optional[pulumi.Input[CxToolOpenApiSpecAuthenticationOauthConfigArgs]]:
        
        ...
    
    @oauth_config.setter
    def oauth_config(self, value: Optional[pulumi.Input[CxToolOpenApiSpecAuthenticationOauthConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAgentAuthConfig")
    def service_agent_auth_config(self) -> Optional[pulumi.Input[CxToolOpenApiSpecAuthenticationServiceAgentAuthConfigArgs]]:
        
        ...
    
    @service_agent_auth_config.setter
    def service_agent_auth_config(self, value: Optional[pulumi.Input[CxToolOpenApiSpecAuthenticationServiceAgentAuthConfigArgs]]): # -> None:
        ...
    


class CxToolOpenApiSpecAuthenticationApiKeyConfigArgsDict(TypedDict):
    key_name: pulumi.Input[_builtins.str]
    request_location: pulumi.Input[_builtins.str]
    api_key: NotRequired[pulumi.Input[_builtins.str]]
    secret_version_for_api_key: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxToolOpenApiSpecAuthenticationApiKeyConfigArgs:
    def __init__(__self__, *, key_name: pulumi.Input[_builtins.str], request_location: pulumi.Input[_builtins.str], api_key: Optional[pulumi.Input[_builtins.str]] = ..., secret_version_for_api_key: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestLocation")
    def request_location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @request_location.setter
    def request_location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersionForApiKey")
    def secret_version_for_api_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_version_for_api_key.setter
    def secret_version_for_api_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxToolOpenApiSpecAuthenticationBearerTokenConfigArgsDict(TypedDict):
    secret_version_for_token: NotRequired[pulumi.Input[_builtins.str]]
    token: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxToolOpenApiSpecAuthenticationBearerTokenConfigArgs:
    def __init__(__self__, *, secret_version_for_token: Optional[pulumi.Input[_builtins.str]] = ..., token: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersionForToken")
    def secret_version_for_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_version_for_token.setter
    def secret_version_for_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @token.setter
    def token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxToolOpenApiSpecAuthenticationOauthConfigArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    oauth_grant_type: pulumi.Input[_builtins.str]
    token_endpoint: pulumi.Input[_builtins.str]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    secret_version_for_client_secret: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxToolOpenApiSpecAuthenticationOauthConfigArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], oauth_grant_type: pulumi.Input[_builtins.str], token_endpoint: pulumi.Input[_builtins.str], client_secret: Optional[pulumi.Input[_builtins.str]] = ..., scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., secret_version_for_client_secret: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthGrantType")
    def oauth_grant_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @oauth_grant_type.setter
    def oauth_grant_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersionForClientSecret")
    def secret_version_for_client_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_version_for_client_secret.setter
    def secret_version_for_client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxToolOpenApiSpecAuthenticationServiceAgentAuthConfigArgsDict(TypedDict):
    service_agent_auth: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxToolOpenApiSpecAuthenticationServiceAgentAuthConfigArgs:
    def __init__(__self__, *, service_agent_auth: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAgentAuth")
    def service_agent_auth(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_agent_auth.setter
    def service_agent_auth(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxToolOpenApiSpecServiceDirectoryConfigArgsDict(TypedDict):
    service: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxToolOpenApiSpecServiceDirectoryConfigArgs:
    def __init__(__self__, *, service: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxToolOpenApiSpecTlsConfigArgsDict(TypedDict):
    ca_certs: pulumi.Input[Sequence[pulumi.Input[CxToolOpenApiSpecTlsConfigCaCertArgsDict]]]


@pulumi.input_type
class CxToolOpenApiSpecTlsConfigArgs:
    def __init__(__self__, *, ca_certs: pulumi.Input[Sequence[pulumi.Input[CxToolOpenApiSpecTlsConfigCaCertArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(self) -> pulumi.Input[Sequence[pulumi.Input[CxToolOpenApiSpecTlsConfigCaCertArgs]]]:
        
        ...
    
    @ca_certs.setter
    def ca_certs(self, value: pulumi.Input[Sequence[pulumi.Input[CxToolOpenApiSpecTlsConfigCaCertArgs]]]): # -> None:
        ...
    


class CxToolOpenApiSpecTlsConfigCaCertArgsDict(TypedDict):
    cert: pulumi.Input[_builtins.str]
    display_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxToolOpenApiSpecTlsConfigCaCertArgs:
    def __init__(__self__, *, cert: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cert(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cert.setter
    def cert(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxToolVersionToolArgsDict(TypedDict):
    description: pulumi.Input[_builtins.str]
    display_name: pulumi.Input[_builtins.str]
    connector_spec: NotRequired[pulumi.Input[CxToolVersionToolConnectorSpecArgsDict]]
    data_store_spec: NotRequired[pulumi.Input[CxToolVersionToolDataStoreSpecArgsDict]]
    function_spec: NotRequired[pulumi.Input[CxToolVersionToolFunctionSpecArgsDict]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    open_api_spec: NotRequired[pulumi.Input[CxToolVersionToolOpenApiSpecArgsDict]]
    tool_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxToolVersionToolArgs:
    def __init__(__self__, *, description: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], connector_spec: Optional[pulumi.Input[CxToolVersionToolConnectorSpecArgs]] = ..., data_store_spec: Optional[pulumi.Input[CxToolVersionToolDataStoreSpecArgs]] = ..., function_spec: Optional[pulumi.Input[CxToolVersionToolFunctionSpecArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., open_api_spec: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecArgs]] = ..., tool_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorSpec")
    def connector_spec(self) -> Optional[pulumi.Input[CxToolVersionToolConnectorSpecArgs]]:
        
        ...
    
    @connector_spec.setter
    def connector_spec(self, value: Optional[pulumi.Input[CxToolVersionToolConnectorSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreSpec")
    def data_store_spec(self) -> Optional[pulumi.Input[CxToolVersionToolDataStoreSpecArgs]]:
        
        ...
    
    @data_store_spec.setter
    def data_store_spec(self, value: Optional[pulumi.Input[CxToolVersionToolDataStoreSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionSpec")
    def function_spec(self) -> Optional[pulumi.Input[CxToolVersionToolFunctionSpecArgs]]:
        
        ...
    
    @function_spec.setter
    def function_spec(self, value: Optional[pulumi.Input[CxToolVersionToolFunctionSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="openApiSpec")
    def open_api_spec(self) -> Optional[pulumi.Input[CxToolVersionToolOpenApiSpecArgs]]:
        
        ...
    
    @open_api_spec.setter
    def open_api_spec(self, value: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolType")
    def tool_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @tool_type.setter
    def tool_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxToolVersionToolConnectorSpecArgsDict(TypedDict):
    actions: pulumi.Input[Sequence[pulumi.Input[CxToolVersionToolConnectorSpecActionArgsDict]]]
    name: pulumi.Input[_builtins.str]
    end_user_auth_config: NotRequired[pulumi.Input[CxToolVersionToolConnectorSpecEndUserAuthConfigArgsDict]]


@pulumi.input_type
class CxToolVersionToolConnectorSpecArgs:
    def __init__(__self__, *, actions: pulumi.Input[Sequence[pulumi.Input[CxToolVersionToolConnectorSpecActionArgs]]], name: pulumi.Input[_builtins.str], end_user_auth_config: Optional[pulumi.Input[CxToolVersionToolConnectorSpecEndUserAuthConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[CxToolVersionToolConnectorSpecActionArgs]]]:
        
        ...
    
    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[CxToolVersionToolConnectorSpecActionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="endUserAuthConfig")
    def end_user_auth_config(self) -> Optional[pulumi.Input[CxToolVersionToolConnectorSpecEndUserAuthConfigArgs]]:
        
        ...
    
    @end_user_auth_config.setter
    def end_user_auth_config(self, value: Optional[pulumi.Input[CxToolVersionToolConnectorSpecEndUserAuthConfigArgs]]): # -> None:
        ...
    


class CxToolVersionToolConnectorSpecActionArgsDict(TypedDict):
    connection_action_id: NotRequired[pulumi.Input[_builtins.str]]
    entity_operation: NotRequired[pulumi.Input[CxToolVersionToolConnectorSpecActionEntityOperationArgsDict]]
    input_fields: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    output_fields: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]


@pulumi.input_type
class CxToolVersionToolConnectorSpecActionArgs:
    def __init__(__self__, *, connection_action_id: Optional[pulumi.Input[_builtins.str]] = ..., entity_operation: Optional[pulumi.Input[CxToolVersionToolConnectorSpecActionEntityOperationArgs]] = ..., input_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., output_fields: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectionActionId")
    def connection_action_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @connection_action_id.setter
    def connection_action_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityOperation")
    def entity_operation(self) -> Optional[pulumi.Input[CxToolVersionToolConnectorSpecActionEntityOperationArgs]]:
        
        ...
    
    @entity_operation.setter
    def entity_operation(self, value: Optional[pulumi.Input[CxToolVersionToolConnectorSpecActionEntityOperationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputFields")
    def input_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @input_fields.setter
    def input_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputFields")
    def output_fields(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @output_fields.setter
    def output_fields(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    


class CxToolVersionToolConnectorSpecActionEntityOperationArgsDict(TypedDict):
    entity_id: pulumi.Input[_builtins.str]
    operation: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxToolVersionToolConnectorSpecActionEntityOperationArgs:
    def __init__(__self__, *, entity_id: pulumi.Input[_builtins.str], operation: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entityId")
    def entity_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @entity_id.setter
    def entity_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def operation(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @operation.setter
    def operation(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxToolVersionToolConnectorSpecEndUserAuthConfigArgsDict(TypedDict):
    oauth2_auth_code_config: NotRequired[pulumi.Input[CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfigArgsDict]]
    oauth2_jwt_bearer_config: NotRequired[pulumi.Input[CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfigArgsDict]]


@pulumi.input_type
class CxToolVersionToolConnectorSpecEndUserAuthConfigArgs:
    def __init__(__self__, *, oauth2_auth_code_config: Optional[pulumi.Input[CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfigArgs]] = ..., oauth2_jwt_bearer_config: Optional[pulumi.Input[CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2AuthCodeConfig")
    def oauth2_auth_code_config(self) -> Optional[pulumi.Input[CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfigArgs]]:
        
        ...
    
    @oauth2_auth_code_config.setter
    def oauth2_auth_code_config(self, value: Optional[pulumi.Input[CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauth2JwtBearerConfig")
    def oauth2_jwt_bearer_config(self) -> Optional[pulumi.Input[CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfigArgs]]:
        
        ...
    
    @oauth2_jwt_bearer_config.setter
    def oauth2_jwt_bearer_config(self, value: Optional[pulumi.Input[CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfigArgs]]): # -> None:
        ...
    


class CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfigArgsDict(TypedDict):
    oauth_token: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2AuthCodeConfigArgs:
    def __init__(__self__, *, oauth_token: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthToken")
    def oauth_token(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @oauth_token.setter
    def oauth_token(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfigArgsDict(TypedDict):
    client_key: pulumi.Input[_builtins.str]
    issuer: pulumi.Input[_builtins.str]
    subject: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxToolVersionToolConnectorSpecEndUserAuthConfigOauth2JwtBearerConfigArgs:
    def __init__(__self__, *, client_key: pulumi.Input[_builtins.str], issuer: pulumi.Input[_builtins.str], subject: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientKey")
    def client_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_key.setter
    def client_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def issuer(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @issuer.setter
    def issuer(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def subject(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @subject.setter
    def subject(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxToolVersionToolDataStoreSpecArgsDict(TypedDict):
    data_store_connections: pulumi.Input[Sequence[pulumi.Input[CxToolVersionToolDataStoreSpecDataStoreConnectionArgsDict]]]
    fallback_prompt: pulumi.Input[CxToolVersionToolDataStoreSpecFallbackPromptArgsDict]


@pulumi.input_type
class CxToolVersionToolDataStoreSpecArgs:
    def __init__(__self__, *, data_store_connections: pulumi.Input[Sequence[pulumi.Input[CxToolVersionToolDataStoreSpecDataStoreConnectionArgs]]], fallback_prompt: pulumi.Input[CxToolVersionToolDataStoreSpecFallbackPromptArgs]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreConnections")
    def data_store_connections(self) -> pulumi.Input[Sequence[pulumi.Input[CxToolVersionToolDataStoreSpecDataStoreConnectionArgs]]]:
        
        ...
    
    @data_store_connections.setter
    def data_store_connections(self, value: pulumi.Input[Sequence[pulumi.Input[CxToolVersionToolDataStoreSpecDataStoreConnectionArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackPrompt")
    def fallback_prompt(self) -> pulumi.Input[CxToolVersionToolDataStoreSpecFallbackPromptArgs]:
        
        ...
    
    @fallback_prompt.setter
    def fallback_prompt(self, value: pulumi.Input[CxToolVersionToolDataStoreSpecFallbackPromptArgs]): # -> None:
        ...
    


class CxToolVersionToolDataStoreSpecDataStoreConnectionArgsDict(TypedDict):
    data_store: NotRequired[pulumi.Input[_builtins.str]]
    data_store_type: NotRequired[pulumi.Input[_builtins.str]]
    document_processing_mode: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxToolVersionToolDataStoreSpecDataStoreConnectionArgs:
    def __init__(__self__, *, data_store: Optional[pulumi.Input[_builtins.str]] = ..., data_store_type: Optional[pulumi.Input[_builtins.str]] = ..., document_processing_mode: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_store.setter
    def data_store(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreType")
    def data_store_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @data_store_type.setter
    def data_store_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentProcessingMode")
    def document_processing_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @document_processing_mode.setter
    def document_processing_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxToolVersionToolDataStoreSpecFallbackPromptArgsDict(TypedDict):
    ...


@pulumi.input_type
class CxToolVersionToolDataStoreSpecFallbackPromptArgs:
    def __init__(__self__) -> None:
        ...
    


class CxToolVersionToolFunctionSpecArgsDict(TypedDict):
    input_schema: NotRequired[pulumi.Input[_builtins.str]]
    output_schema: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxToolVersionToolFunctionSpecArgs:
    def __init__(__self__, *, input_schema: Optional[pulumi.Input[_builtins.str]] = ..., output_schema: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputSchema")
    def input_schema(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @input_schema.setter
    def input_schema(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputSchema")
    def output_schema(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @output_schema.setter
    def output_schema(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxToolVersionToolOpenApiSpecArgsDict(TypedDict):
    text_schema: pulumi.Input[_builtins.str]
    authentication: NotRequired[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationArgsDict]]
    service_directory_config: NotRequired[pulumi.Input[CxToolVersionToolOpenApiSpecServiceDirectoryConfigArgsDict]]
    tls_config: NotRequired[pulumi.Input[CxToolVersionToolOpenApiSpecTlsConfigArgsDict]]


@pulumi.input_type
class CxToolVersionToolOpenApiSpecArgs:
    def __init__(__self__, *, text_schema: pulumi.Input[_builtins.str], authentication: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationArgs]] = ..., service_directory_config: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecServiceDirectoryConfigArgs]] = ..., tls_config: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecTlsConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textSchema")
    def text_schema(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @text_schema.setter
    def text_schema(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def authentication(self) -> Optional[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationArgs]]:
        
        ...
    
    @authentication.setter
    def authentication(self, value: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(self) -> Optional[pulumi.Input[CxToolVersionToolOpenApiSpecServiceDirectoryConfigArgs]]:
        
        ...
    
    @service_directory_config.setter
    def service_directory_config(self, value: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecServiceDirectoryConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[pulumi.Input[CxToolVersionToolOpenApiSpecTlsConfigArgs]]:
        
        ...
    
    @tls_config.setter
    def tls_config(self, value: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecTlsConfigArgs]]): # -> None:
        ...
    


class CxToolVersionToolOpenApiSpecAuthenticationArgsDict(TypedDict):
    api_key_config: NotRequired[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationApiKeyConfigArgsDict]]
    bearer_token_config: NotRequired[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationBearerTokenConfigArgsDict]]
    oauth_config: NotRequired[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationOauthConfigArgsDict]]
    service_agent_auth_config: NotRequired[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationServiceAgentAuthConfigArgsDict]]


@pulumi.input_type
class CxToolVersionToolOpenApiSpecAuthenticationArgs:
    def __init__(__self__, *, api_key_config: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationApiKeyConfigArgs]] = ..., bearer_token_config: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationBearerTokenConfigArgs]] = ..., oauth_config: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationOauthConfigArgs]] = ..., service_agent_auth_config: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationServiceAgentAuthConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyConfig")
    def api_key_config(self) -> Optional[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationApiKeyConfigArgs]]:
        
        ...
    
    @api_key_config.setter
    def api_key_config(self, value: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationApiKeyConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="bearerTokenConfig")
    def bearer_token_config(self) -> Optional[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationBearerTokenConfigArgs]]:
        
        ...
    
    @bearer_token_config.setter
    def bearer_token_config(self, value: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationBearerTokenConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthConfig")
    def oauth_config(self) -> Optional[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationOauthConfigArgs]]:
        
        ...
    
    @oauth_config.setter
    def oauth_config(self, value: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationOauthConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAgentAuthConfig")
    def service_agent_auth_config(self) -> Optional[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationServiceAgentAuthConfigArgs]]:
        
        ...
    
    @service_agent_auth_config.setter
    def service_agent_auth_config(self, value: Optional[pulumi.Input[CxToolVersionToolOpenApiSpecAuthenticationServiceAgentAuthConfigArgs]]): # -> None:
        ...
    


class CxToolVersionToolOpenApiSpecAuthenticationApiKeyConfigArgsDict(TypedDict):
    key_name: pulumi.Input[_builtins.str]
    request_location: pulumi.Input[_builtins.str]
    api_key: NotRequired[pulumi.Input[_builtins.str]]
    secret_version_for_api_key: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxToolVersionToolOpenApiSpecAuthenticationApiKeyConfigArgs:
    def __init__(__self__, *, key_name: pulumi.Input[_builtins.str], request_location: pulumi.Input[_builtins.str], api_key: Optional[pulumi.Input[_builtins.str]] = ..., secret_version_for_api_key: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key_name.setter
    def key_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestLocation")
    def request_location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @request_location.setter
    def request_location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKey")
    def api_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @api_key.setter
    def api_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersionForApiKey")
    def secret_version_for_api_key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_version_for_api_key.setter
    def secret_version_for_api_key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxToolVersionToolOpenApiSpecAuthenticationBearerTokenConfigArgsDict(TypedDict):
    secret_version_for_token: NotRequired[pulumi.Input[_builtins.str]]
    token: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxToolVersionToolOpenApiSpecAuthenticationBearerTokenConfigArgs:
    def __init__(__self__, *, secret_version_for_token: Optional[pulumi.Input[_builtins.str]] = ..., token: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersionForToken")
    def secret_version_for_token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_version_for_token.setter
    def secret_version_for_token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @token.setter
    def token(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxToolVersionToolOpenApiSpecAuthenticationOauthConfigArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    oauth_grant_type: pulumi.Input[_builtins.str]
    token_endpoint: pulumi.Input[_builtins.str]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    secret_version_for_client_secret: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxToolVersionToolOpenApiSpecAuthenticationOauthConfigArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], oauth_grant_type: pulumi.Input[_builtins.str], token_endpoint: pulumi.Input[_builtins.str], client_secret: Optional[pulumi.Input[_builtins.str]] = ..., scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., secret_version_for_client_secret: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthGrantType")
    def oauth_grant_type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @oauth_grant_type.setter
    def oauth_grant_type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersionForClientSecret")
    def secret_version_for_client_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_version_for_client_secret.setter
    def secret_version_for_client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxToolVersionToolOpenApiSpecAuthenticationServiceAgentAuthConfigArgsDict(TypedDict):
    service_agent_auth: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxToolVersionToolOpenApiSpecAuthenticationServiceAgentAuthConfigArgs:
    def __init__(__self__, *, service_agent_auth: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAgentAuth")
    def service_agent_auth(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_agent_auth.setter
    def service_agent_auth(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxToolVersionToolOpenApiSpecServiceDirectoryConfigArgsDict(TypedDict):
    service: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxToolVersionToolOpenApiSpecServiceDirectoryConfigArgs:
    def __init__(__self__, *, service: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxToolVersionToolOpenApiSpecTlsConfigArgsDict(TypedDict):
    ca_certs: pulumi.Input[Sequence[pulumi.Input[CxToolVersionToolOpenApiSpecTlsConfigCaCertArgsDict]]]


@pulumi.input_type
class CxToolVersionToolOpenApiSpecTlsConfigArgs:
    def __init__(__self__, *, ca_certs: pulumi.Input[Sequence[pulumi.Input[CxToolVersionToolOpenApiSpecTlsConfigCaCertArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(self) -> pulumi.Input[Sequence[pulumi.Input[CxToolVersionToolOpenApiSpecTlsConfigCaCertArgs]]]:
        
        ...
    
    @ca_certs.setter
    def ca_certs(self, value: pulumi.Input[Sequence[pulumi.Input[CxToolVersionToolOpenApiSpecTlsConfigCaCertArgs]]]): # -> None:
        ...
    


class CxToolVersionToolOpenApiSpecTlsConfigCaCertArgsDict(TypedDict):
    cert: pulumi.Input[_builtins.str]
    display_name: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxToolVersionToolOpenApiSpecTlsConfigCaCertArgs:
    def __init__(__self__, *, cert: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cert(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @cert.setter
    def cert(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxVersionNluSettingArgsDict(TypedDict):
    classification_threshold: NotRequired[pulumi.Input[_builtins.float]]
    model_training_mode: NotRequired[pulumi.Input[_builtins.str]]
    model_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxVersionNluSettingArgs:
    def __init__(__self__, *, classification_threshold: Optional[pulumi.Input[_builtins.float]] = ..., model_training_mode: Optional[pulumi.Input[_builtins.str]] = ..., model_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="classificationThreshold")
    def classification_threshold(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @classification_threshold.setter
    def classification_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelTrainingMode")
    def model_training_mode(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_training_mode.setter
    def model_training_mode(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelType")
    def model_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @model_type.setter
    def model_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxWebhookGenericWebServiceArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    allowed_ca_certs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    http_method: NotRequired[pulumi.Input[_builtins.str]]
    oauth_config: NotRequired[pulumi.Input[CxWebhookGenericWebServiceOauthConfigArgsDict]]
    parameter_mapping: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    request_body: NotRequired[pulumi.Input[_builtins.str]]
    request_headers: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    secret_version_for_username_password: NotRequired[pulumi.Input[_builtins.str]]
    secret_versions_for_request_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxWebhookGenericWebServiceSecretVersionsForRequestHeaderArgsDict]]]]
    service_account_auth_config: NotRequired[pulumi.Input[CxWebhookGenericWebServiceServiceAccountAuthConfigArgsDict]]
    service_agent_auth: NotRequired[pulumi.Input[_builtins.str]]
    webhook_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxWebhookGenericWebServiceArgs:
    def __init__(__self__, *, uri: pulumi.Input[_builtins.str], allowed_ca_certs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., http_method: Optional[pulumi.Input[_builtins.str]] = ..., oauth_config: Optional[pulumi.Input[CxWebhookGenericWebServiceOauthConfigArgs]] = ..., parameter_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., request_body: Optional[pulumi.Input[_builtins.str]] = ..., request_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., secret_version_for_username_password: Optional[pulumi.Input[_builtins.str]] = ..., secret_versions_for_request_headers: Optional[pulumi.Input[Sequence[pulumi.Input[CxWebhookGenericWebServiceSecretVersionsForRequestHeaderArgs]]]] = ..., service_account_auth_config: Optional[pulumi.Input[CxWebhookGenericWebServiceServiceAccountAuthConfigArgs]] = ..., service_agent_auth: Optional[pulumi.Input[_builtins.str]] = ..., webhook_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedCaCerts")
    def allowed_ca_certs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_ca_certs.setter
    def allowed_ca_certs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_method.setter
    def http_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthConfig")
    def oauth_config(self) -> Optional[pulumi.Input[CxWebhookGenericWebServiceOauthConfigArgs]]:
        
        ...
    
    @oauth_config.setter
    def oauth_config(self, value: Optional[pulumi.Input[CxWebhookGenericWebServiceOauthConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterMapping")
    def parameter_mapping(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameter_mapping.setter
    def parameter_mapping(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestBody")
    def request_body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_body.setter
    def request_body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestHeaders")
    def request_headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @request_headers.setter
    def request_headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersionForUsernamePassword")
    def secret_version_for_username_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_version_for_username_password.setter
    def secret_version_for_username_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersionsForRequestHeaders")
    def secret_versions_for_request_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxWebhookGenericWebServiceSecretVersionsForRequestHeaderArgs]]]]:
        
        ...
    
    @secret_versions_for_request_headers.setter
    def secret_versions_for_request_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxWebhookGenericWebServiceSecretVersionsForRequestHeaderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountAuthConfig")
    def service_account_auth_config(self) -> Optional[pulumi.Input[CxWebhookGenericWebServiceServiceAccountAuthConfigArgs]]:
        
        ...
    
    @service_account_auth_config.setter
    def service_account_auth_config(self, value: Optional[pulumi.Input[CxWebhookGenericWebServiceServiceAccountAuthConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAgentAuth")
    def service_agent_auth(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_agent_auth.setter
    def service_agent_auth(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookType")
    def webhook_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @webhook_type.setter
    def webhook_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxWebhookGenericWebServiceOauthConfigArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    token_endpoint: pulumi.Input[_builtins.str]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    secret_version_for_client_secret: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxWebhookGenericWebServiceOauthConfigArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], token_endpoint: pulumi.Input[_builtins.str], client_secret: Optional[pulumi.Input[_builtins.str]] = ..., scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., secret_version_for_client_secret: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersionForClientSecret")
    def secret_version_for_client_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_version_for_client_secret.setter
    def secret_version_for_client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxWebhookGenericWebServiceSecretVersionsForRequestHeaderArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    secret_version: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxWebhookGenericWebServiceSecretVersionsForRequestHeaderArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], secret_version: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxWebhookGenericWebServiceServiceAccountAuthConfigArgsDict(TypedDict):
    service_account: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxWebhookGenericWebServiceServiceAccountAuthConfigArgs:
    def __init__(__self__, *, service_account: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_account.setter
    def service_account(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxWebhookServiceDirectoryArgsDict(TypedDict):
    service: pulumi.Input[_builtins.str]
    generic_web_service: NotRequired[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceArgsDict]]


@pulumi.input_type
class CxWebhookServiceDirectoryArgs:
    def __init__(__self__, *, service: pulumi.Input[_builtins.str], generic_web_service: Optional[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="genericWebService")
    def generic_web_service(self) -> Optional[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceArgs]]:
        
        ...
    
    @generic_web_service.setter
    def generic_web_service(self, value: Optional[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceArgs]]): # -> None:
        ...
    


class CxWebhookServiceDirectoryGenericWebServiceArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    allowed_ca_certs: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    http_method: NotRequired[pulumi.Input[_builtins.str]]
    oauth_config: NotRequired[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceOauthConfigArgsDict]]
    parameter_mapping: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    request_body: NotRequired[pulumi.Input[_builtins.str]]
    request_headers: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    secret_version_for_username_password: NotRequired[pulumi.Input[_builtins.str]]
    secret_versions_for_request_headers: NotRequired[pulumi.Input[Sequence[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceSecretVersionsForRequestHeaderArgsDict]]]]
    service_account_auth_config: NotRequired[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceServiceAccountAuthConfigArgsDict]]
    service_agent_auth: NotRequired[pulumi.Input[_builtins.str]]
    webhook_type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxWebhookServiceDirectoryGenericWebServiceArgs:
    def __init__(__self__, *, uri: pulumi.Input[_builtins.str], allowed_ca_certs: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., http_method: Optional[pulumi.Input[_builtins.str]] = ..., oauth_config: Optional[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceOauthConfigArgs]] = ..., parameter_mapping: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., request_body: Optional[pulumi.Input[_builtins.str]] = ..., request_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., secret_version_for_username_password: Optional[pulumi.Input[_builtins.str]] = ..., secret_versions_for_request_headers: Optional[pulumi.Input[Sequence[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceSecretVersionsForRequestHeaderArgs]]]] = ..., service_account_auth_config: Optional[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceServiceAccountAuthConfigArgs]] = ..., service_agent_auth: Optional[pulumi.Input[_builtins.str]] = ..., webhook_type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowedCaCerts")
    def allowed_ca_certs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @allowed_ca_certs.setter
    def allowed_ca_certs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="httpMethod")
    def http_method(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @http_method.setter
    def http_method(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthConfig")
    def oauth_config(self) -> Optional[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceOauthConfigArgs]]:
        
        ...
    
    @oauth_config.setter
    def oauth_config(self, value: Optional[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceOauthConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parameterMapping")
    def parameter_mapping(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @parameter_mapping.setter
    def parameter_mapping(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestBody")
    def request_body(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @request_body.setter
    def request_body(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestHeaders")
    def request_headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @request_headers.setter
    def request_headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersionForUsernamePassword")
    def secret_version_for_username_password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_version_for_username_password.setter
    def secret_version_for_username_password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersionsForRequestHeaders")
    def secret_versions_for_request_headers(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceSecretVersionsForRequestHeaderArgs]]]]:
        
        ...
    
    @secret_versions_for_request_headers.setter
    def secret_versions_for_request_headers(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceSecretVersionsForRequestHeaderArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountAuthConfig")
    def service_account_auth_config(self) -> Optional[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceServiceAccountAuthConfigArgs]]:
        
        ...
    
    @service_account_auth_config.setter
    def service_account_auth_config(self, value: Optional[pulumi.Input[CxWebhookServiceDirectoryGenericWebServiceServiceAccountAuthConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAgentAuth")
    def service_agent_auth(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @service_agent_auth.setter
    def service_agent_auth(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="webhookType")
    def webhook_type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @webhook_type.setter
    def webhook_type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxWebhookServiceDirectoryGenericWebServiceOauthConfigArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    token_endpoint: pulumi.Input[_builtins.str]
    client_secret: NotRequired[pulumi.Input[_builtins.str]]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    secret_version_for_client_secret: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class CxWebhookServiceDirectoryGenericWebServiceOauthConfigArgs:
    def __init__(__self__, *, client_id: pulumi.Input[_builtins.str], token_endpoint: pulumi.Input[_builtins.str], client_secret: Optional[pulumi.Input[_builtins.str]] = ..., scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., secret_version_for_client_secret: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @client_secret.setter
    def client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @scopes.setter
    def scopes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersionForClientSecret")
    def secret_version_for_client_secret(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @secret_version_for_client_secret.setter
    def secret_version_for_client_secret(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class CxWebhookServiceDirectoryGenericWebServiceSecretVersionsForRequestHeaderArgsDict(TypedDict):
    key: pulumi.Input[_builtins.str]
    secret_version: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxWebhookServiceDirectoryGenericWebServiceSecretVersionsForRequestHeaderArgs:
    def __init__(__self__, *, key: pulumi.Input[_builtins.str], secret_version: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="secretVersion")
    def secret_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @secret_version.setter
    def secret_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class CxWebhookServiceDirectoryGenericWebServiceServiceAccountAuthConfigArgsDict(TypedDict):
    service_account: pulumi.Input[_builtins.str]


@pulumi.input_type
class CxWebhookServiceDirectoryGenericWebServiceServiceAccountAuthConfigArgs:
    def __init__(__self__, *, service_account: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @service_account.setter
    def service_account(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EncryptionSpecEncryptionSpecArgsDict(TypedDict):
    kms_key: pulumi.Input[_builtins.str]


@pulumi.input_type
class EncryptionSpecEncryptionSpecArgs:
    def __init__(__self__, *, kms_key: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="kmsKey")
    def kms_key(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @kms_key.setter
    def kms_key(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class EntityTypeEntityArgsDict(TypedDict):
    synonyms: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    value: pulumi.Input[_builtins.str]


@pulumi.input_type
class EntityTypeEntityArgs:
    def __init__(__self__, *, synonyms: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]], value: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def synonyms(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]:
        
        ...
    
    @synonyms.setter
    def synonyms(self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def value(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @value.setter
    def value(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FulfillmentFeatureArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]


@pulumi.input_type
class FulfillmentFeatureArgs:
    def __init__(__self__, *, type: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class FulfillmentGenericWebServiceArgsDict(TypedDict):
    uri: pulumi.Input[_builtins.str]
    password: NotRequired[pulumi.Input[_builtins.str]]
    request_headers: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    username: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class FulfillmentGenericWebServiceArgs:
    def __init__(__self__, *, uri: pulumi.Input[_builtins.str], password: Optional[pulumi.Input[_builtins.str]] = ..., request_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., username: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def uri(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @uri.setter
    def uri(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @password.setter
    def password(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestHeaders")
    def request_headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @request_headers.setter
    def request_headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def username(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @username.setter
    def username(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GeneratorInferenceParameterArgsDict(TypedDict):
    max_output_tokens: NotRequired[pulumi.Input[_builtins.int]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    top_k: NotRequired[pulumi.Input[_builtins.int]]
    top_p: NotRequired[pulumi.Input[_builtins.float]]


@pulumi.input_type
class GeneratorInferenceParameterArgs:
    def __init__(__self__, *, max_output_tokens: Optional[pulumi.Input[_builtins.int]] = ..., temperature: Optional[pulumi.Input[_builtins.float]] = ..., top_k: Optional[pulumi.Input[_builtins.int]] = ..., top_p: Optional[pulumi.Input[_builtins.float]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxOutputTokens")
    def max_output_tokens(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @max_output_tokens.setter
    def max_output_tokens(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topK")
    def top_k(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @top_k.setter
    def top_k(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="topP")
    def top_p(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @top_p.setter
    def top_p(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    


class GeneratorSummarizationContextArgsDict(TypedDict):
    few_shot_examples: NotRequired[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleArgsDict]]]]
    output_language_code: NotRequired[pulumi.Input[_builtins.str]]
    summarization_sections: NotRequired[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextSummarizationSectionArgsDict]]]]
    version: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GeneratorSummarizationContextArgs:
    def __init__(__self__, *, few_shot_examples: Optional[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleArgs]]]] = ..., output_language_code: Optional[pulumi.Input[_builtins.str]] = ..., summarization_sections: Optional[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextSummarizationSectionArgs]]]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fewShotExamples")
    def few_shot_examples(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleArgs]]]]:
        
        ...
    
    @few_shot_examples.setter
    def few_shot_examples(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputLanguageCode")
    def output_language_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @output_language_code.setter
    def output_language_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="summarizationSections")
    def summarization_sections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextSummarizationSectionArgs]]]]:
        
        ...
    
    @summarization_sections.setter
    def summarization_sections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextSummarizationSectionArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GeneratorSummarizationContextFewShotExampleArgsDict(TypedDict):
    output: pulumi.Input[GeneratorSummarizationContextFewShotExampleOutputArgsDict]
    conversation_context: NotRequired[pulumi.Input[GeneratorSummarizationContextFewShotExampleConversationContextArgsDict]]
    extra_info: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    summarization_section_list: NotRequired[pulumi.Input[GeneratorSummarizationContextFewShotExampleSummarizationSectionListArgsDict]]


@pulumi.input_type
class GeneratorSummarizationContextFewShotExampleArgs:
    def __init__(__self__, *, output: pulumi.Input[GeneratorSummarizationContextFewShotExampleOutputArgs], conversation_context: Optional[pulumi.Input[GeneratorSummarizationContextFewShotExampleConversationContextArgs]] = ..., extra_info: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., summarization_section_list: Optional[pulumi.Input[GeneratorSummarizationContextFewShotExampleSummarizationSectionListArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def output(self) -> pulumi.Input[GeneratorSummarizationContextFewShotExampleOutputArgs]:
        
        ...
    
    @output.setter
    def output(self, value: pulumi.Input[GeneratorSummarizationContextFewShotExampleOutputArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationContext")
    def conversation_context(self) -> Optional[pulumi.Input[GeneratorSummarizationContextFewShotExampleConversationContextArgs]]:
        
        ...
    
    @conversation_context.setter
    def conversation_context(self, value: Optional[pulumi.Input[GeneratorSummarizationContextFewShotExampleConversationContextArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="extraInfo")
    def extra_info(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @extra_info.setter
    def extra_info(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="summarizationSectionList")
    def summarization_section_list(self) -> Optional[pulumi.Input[GeneratorSummarizationContextFewShotExampleSummarizationSectionListArgs]]:
        
        ...
    
    @summarization_section_list.setter
    def summarization_section_list(self, value: Optional[pulumi.Input[GeneratorSummarizationContextFewShotExampleSummarizationSectionListArgs]]): # -> None:
        ...
    


class GeneratorSummarizationContextFewShotExampleConversationContextArgsDict(TypedDict):
    message_entries: NotRequired[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleConversationContextMessageEntryArgsDict]]]]


@pulumi.input_type
class GeneratorSummarizationContextFewShotExampleConversationContextArgs:
    def __init__(__self__, *, message_entries: Optional[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleConversationContextMessageEntryArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="messageEntries")
    def message_entries(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleConversationContextMessageEntryArgs]]]]:
        
        ...
    
    @message_entries.setter
    def message_entries(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleConversationContextMessageEntryArgs]]]]): # -> None:
        ...
    


class GeneratorSummarizationContextFewShotExampleConversationContextMessageEntryArgsDict(TypedDict):
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    language_code: NotRequired[pulumi.Input[_builtins.str]]
    role: NotRequired[pulumi.Input[_builtins.str]]
    text: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GeneratorSummarizationContextFewShotExampleConversationContextMessageEntryArgs:
    def __init__(__self__, *, create_time: Optional[pulumi.Input[_builtins.str]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., role: Optional[pulumi.Input[_builtins.str]] = ..., text: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GeneratorSummarizationContextFewShotExampleOutputArgsDict(TypedDict):
    summary_suggestion: NotRequired[pulumi.Input[GeneratorSummarizationContextFewShotExampleOutputSummarySuggestionArgsDict]]


@pulumi.input_type
class GeneratorSummarizationContextFewShotExampleOutputArgs:
    def __init__(__self__, *, summary_suggestion: Optional[pulumi.Input[GeneratorSummarizationContextFewShotExampleOutputSummarySuggestionArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="summarySuggestion")
    def summary_suggestion(self) -> Optional[pulumi.Input[GeneratorSummarizationContextFewShotExampleOutputSummarySuggestionArgs]]:
        
        ...
    
    @summary_suggestion.setter
    def summary_suggestion(self, value: Optional[pulumi.Input[GeneratorSummarizationContextFewShotExampleOutputSummarySuggestionArgs]]): # -> None:
        ...
    


class GeneratorSummarizationContextFewShotExampleOutputSummarySuggestionArgsDict(TypedDict):
    summary_sections: pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleOutputSummarySuggestionSummarySectionArgsDict]]]


@pulumi.input_type
class GeneratorSummarizationContextFewShotExampleOutputSummarySuggestionArgs:
    def __init__(__self__, *, summary_sections: pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleOutputSummarySuggestionSummarySectionArgs]]]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="summarySections")
    def summary_sections(self) -> pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleOutputSummarySuggestionSummarySectionArgs]]]:
        
        ...
    
    @summary_sections.setter
    def summary_sections(self, value: pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleOutputSummarySuggestionSummarySectionArgs]]]): # -> None:
        ...
    


class GeneratorSummarizationContextFewShotExampleOutputSummarySuggestionSummarySectionArgsDict(TypedDict):
    section: pulumi.Input[_builtins.str]
    summary: pulumi.Input[_builtins.str]


@pulumi.input_type
class GeneratorSummarizationContextFewShotExampleOutputSummarySuggestionSummarySectionArgs:
    def __init__(__self__, *, section: pulumi.Input[_builtins.str], summary: pulumi.Input[_builtins.str]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def section(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @section.setter
    def section(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def summary(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @summary.setter
    def summary(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    


class GeneratorSummarizationContextFewShotExampleSummarizationSectionListArgsDict(TypedDict):
    summarization_sections: NotRequired[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleSummarizationSectionListSummarizationSectionArgsDict]]]]


@pulumi.input_type
class GeneratorSummarizationContextFewShotExampleSummarizationSectionListArgs:
    def __init__(__self__, *, summarization_sections: Optional[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleSummarizationSectionListSummarizationSectionArgs]]]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="summarizationSections")
    def summarization_sections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleSummarizationSectionListSummarizationSectionArgs]]]]:
        
        ...
    
    @summarization_sections.setter
    def summarization_sections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[GeneratorSummarizationContextFewShotExampleSummarizationSectionListSummarizationSectionArgs]]]]): # -> None:
        ...
    


class GeneratorSummarizationContextFewShotExampleSummarizationSectionListSummarizationSectionArgsDict(TypedDict):
    definition: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GeneratorSummarizationContextFewShotExampleSummarizationSectionListSummarizationSectionArgs:
    def __init__(__self__, *, definition: Optional[pulumi.Input[_builtins.str]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def definition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @definition.setter
    def definition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class GeneratorSummarizationContextSummarizationSectionArgsDict(TypedDict):
    definition: NotRequired[pulumi.Input[_builtins.str]]
    key: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class GeneratorSummarizationContextSummarizationSectionArgs:
    def __init__(__self__, *, definition: Optional[pulumi.Input[_builtins.str]] = ..., key: Optional[pulumi.Input[_builtins.str]] = ..., type: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def definition(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @definition.setter
    def definition(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @key.setter
    def key(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


class IntentFollowupIntentInfoArgsDict(TypedDict):
    followup_intent_name: NotRequired[pulumi.Input[_builtins.str]]
    parent_followup_intent_name: NotRequired[pulumi.Input[_builtins.str]]


@pulumi.input_type
class IntentFollowupIntentInfoArgs:
    def __init__(__self__, *, followup_intent_name: Optional[pulumi.Input[_builtins.str]] = ..., parent_followup_intent_name: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="followupIntentName")
    def followup_intent_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @followup_intent_name.setter
    def followup_intent_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentFollowupIntentName")
    def parent_followup_intent_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent_followup_intent_name.setter
    def parent_followup_intent_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


