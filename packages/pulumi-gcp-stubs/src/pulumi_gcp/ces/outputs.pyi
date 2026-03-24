

import builtins as _builtins
import sys
import pulumi
from typing import Any, Mapping, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AgentAfterAgentCallback', 'AgentAfterModelCallback', 'AgentAfterToolCallback', 'AgentBeforeAgentCallback', 'AgentBeforeModelCallback', 'AgentBeforeToolCallback', 'AgentLlmAgent', 'AgentModelSettings', 'AgentRemoteDialogflowAgent', 'AgentToolset', 'AppAudioProcessingConfig', 'AppAudioProcessingConfigAmbientSoundConfig', 'AppAudioProcessingConfigBargeInConfig', 'AppAudioProcessingConfigSynthesizeSpeechConfig', 'AppClientCertificateSettings', 'AppDataStoreSettings', 'AppDataStoreSettingsEngine', 'AppDefaultChannelProfile', 'AppDefaultChannelProfilePersonaProperty', 'AppDefaultChannelProfileWebWidgetConfig', 'AppEvaluationMetricsThresholds', ..., ..., ..., 'AppLanguageSettings', 'AppLoggingSettings', 'AppLoggingSettingsAudioRecordingConfig', 'AppLoggingSettingsBigqueryExportSettings', 'AppLoggingSettingsCloudLoggingSettings', 'AppLoggingSettingsConversationLoggingSettings', 'AppLoggingSettingsRedactionConfig', 'AppModelSettings', 'AppTimeZoneSettings', 'AppVariableDeclaration', 'AppVariableDeclarationSchema', 'AppVersionSnapshot', 'AppVersionSnapshotAgent', 'AppVersionSnapshotAgentAfterAgentCallback', 'AppVersionSnapshotAgentAfterModelCallback', 'AppVersionSnapshotAgentAfterToolCallback', 'AppVersionSnapshotAgentBeforeAgentCallback', 'AppVersionSnapshotAgentBeforeModelCallback', 'AppVersionSnapshotAgentBeforeToolCallback', 'AppVersionSnapshotAgentLlmAgent', 'AppVersionSnapshotAgentModelSetting', 'AppVersionSnapshotAgentRemoteDialogflowAgent', 'AppVersionSnapshotAgentToolset', 'AppVersionSnapshotApp', 'AppVersionSnapshotAppAudioProcessingConfig', ..., ..., ..., 'AppVersionSnapshotAppClientCertificateSetting', 'AppVersionSnapshotAppDataStoreSetting', 'AppVersionSnapshotAppDataStoreSettingEngine', 'AppVersionSnapshotAppDefaultChannelProfile', ..., ..., 'AppVersionSnapshotAppEvaluationMetricsThreshold', ..., ..., ..., 'AppVersionSnapshotAppLanguageSetting', 'AppVersionSnapshotAppLoggingSetting', ..., ..., ..., ..., 'AppVersionSnapshotAppLoggingSettingRedactionConfig', 'AppVersionSnapshotAppModelSetting', 'AppVersionSnapshotAppTimeZoneSetting', 'AppVersionSnapshotAppVariableDeclaration', 'AppVersionSnapshotAppVariableDeclarationSchema', 'AppVersionSnapshotExample', 'AppVersionSnapshotExampleMessage', 'AppVersionSnapshotExampleMessageChunk', 'AppVersionSnapshotExampleMessageChunkAgentTransfer', 'AppVersionSnapshotExampleMessageChunkImage', 'AppVersionSnapshotExampleMessageChunkToolCall', ..., 'AppVersionSnapshotExampleMessageChunkToolResponse', ..., 'AppVersionSnapshotGuardrail', 'AppVersionSnapshotGuardrailAction', 'AppVersionSnapshotGuardrailActionGenerativeAnswer', ..., ..., 'AppVersionSnapshotGuardrailActionTransferAgent', 'AppVersionSnapshotGuardrailCodeCallback', ..., ..., ..., ..., 'AppVersionSnapshotGuardrailContentFilter', 'AppVersionSnapshotGuardrailLlmPolicy', 'AppVersionSnapshotGuardrailLlmPolicyModelSetting', 'AppVersionSnapshotGuardrailLlmPromptSecurity', ..., ..., ..., 'AppVersionSnapshotGuardrailModelSafety', ..., 'AppVersionSnapshotTool', 'AppVersionSnapshotToolClientFunction', 'AppVersionSnapshotToolClientFunctionParameter', 'AppVersionSnapshotToolClientFunctionResponse', 'AppVersionSnapshotToolDataStoreTool', 'AppVersionSnapshotToolDataStoreToolBoostSpec', 'AppVersionSnapshotToolDataStoreToolBoostSpecSpec', ..., ..., ..., 'AppVersionSnapshotToolDataStoreToolEngineSource', ..., ..., ..., 'AppVersionSnapshotToolDataStoreToolModalityConfig', ..., ..., ..., ..., ..., 'AppVersionSnapshotToolGoogleSearchTool', 'AppVersionSnapshotToolOpenApiTool', 'AppVersionSnapshotToolOpenApiToolApiAuthentication', ..., ..., ..., ..., ..., 'AppVersionSnapshotToolOpenApiToolTlsConfig', 'AppVersionSnapshotToolOpenApiToolTlsConfigCaCert', 'AppVersionSnapshotToolPythonFunction', 'AppVersionSnapshotToolSystemTool', 'AppVersionSnapshotToolset', 'AppVersionSnapshotToolsetOpenApiToolset', ..., ..., ..., ..., ..., ..., ..., 'AppVersionSnapshotToolsetOpenApiToolsetTlsConfig', ..., 'DeploymentChannelProfile', 'DeploymentChannelProfilePersonaProperty', 'DeploymentChannelProfileWebWidgetConfig', 'ExampleMessage', 'ExampleMessageChunk', 'ExampleMessageChunkAgentTransfer', 'ExampleMessageChunkImage', 'ExampleMessageChunkToolCall', 'ExampleMessageChunkToolCallToolsetTool', 'ExampleMessageChunkToolResponse', 'ExampleMessageChunkToolResponseToolsetTool', 'GuardrailAction', 'GuardrailActionGenerativeAnswer', 'GuardrailActionRespondImmediately', 'GuardrailActionRespondImmediatelyResponse', 'GuardrailActionTransferAgent', 'GuardrailCodeCallback', 'GuardrailCodeCallbackAfterAgentCallback', 'GuardrailCodeCallbackAfterModelCallback', 'GuardrailCodeCallbackBeforeAgentCallback', 'GuardrailCodeCallbackBeforeModelCallback', 'GuardrailContentFilter', 'GuardrailLlmPolicy', 'GuardrailLlmPolicyModelSettings', 'GuardrailLlmPromptSecurity', 'GuardrailLlmPromptSecurityCustomPolicy', ..., 'GuardrailLlmPromptSecurityDefaultSettings', 'GuardrailModelSafety', 'GuardrailModelSafetySafetySetting', 'ToolClientFunction', 'ToolClientFunctionParameters', 'ToolClientFunctionResponse', 'ToolDataStoreTool', 'ToolDataStoreToolBoostSpec', 'ToolDataStoreToolBoostSpecSpec', 'ToolDataStoreToolBoostSpecSpecConditionBoostSpec', ..., ..., 'ToolDataStoreToolEngineSource', 'ToolDataStoreToolEngineSourceDataStoreSource', ..., ..., 'ToolDataStoreToolModalityConfig', 'ToolDataStoreToolModalityConfigGroundingConfig', 'ToolDataStoreToolModalityConfigRewriterConfig', ..., 'ToolDataStoreToolModalityConfigSummarizationConfig', ..., 'ToolGoogleSearchTool', 'ToolOpenApiTool', 'ToolOpenApiToolApiAuthentication', 'ToolOpenApiToolApiAuthenticationApiKeyConfig', 'ToolOpenApiToolApiAuthenticationBearerTokenConfig', 'ToolOpenApiToolApiAuthenticationOauthConfig', ..., ..., 'ToolOpenApiToolServiceDirectoryConfig', 'ToolOpenApiToolTlsConfig', 'ToolOpenApiToolTlsConfigCaCert', 'ToolPythonFunction', 'ToolSystemTool', 'ToolsetMcpToolset', 'ToolsetMcpToolsetApiAuthentication', 'ToolsetMcpToolsetApiAuthenticationApiKeyConfig', ..., 'ToolsetMcpToolsetApiAuthenticationOauthConfig', ..., ..., 'ToolsetMcpToolsetServiceDirectoryConfig', 'ToolsetMcpToolsetTlsConfig', 'ToolsetMcpToolsetTlsConfigCaCert', 'ToolsetOpenApiToolset', 'ToolsetOpenApiToolsetApiAuthentication', 'ToolsetOpenApiToolsetApiAuthenticationApiKeyConfig', ..., 'ToolsetOpenApiToolsetApiAuthenticationOauthConfig', ..., ..., 'ToolsetOpenApiToolsetServiceDirectoryConfig', 'ToolsetOpenApiToolsetTlsConfig', 'ToolsetOpenApiToolsetTlsConfigCaCert']
@pulumi.output_type
class AgentAfterAgentCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, python_code: _builtins.str, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AgentAfterModelCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, python_code: _builtins.str, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AgentAfterToolCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, python_code: _builtins.str, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AgentBeforeAgentCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, python_code: _builtins.str, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AgentBeforeModelCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, python_code: _builtins.str, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AgentBeforeToolCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, python_code: _builtins.str, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AgentLlmAgent(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class AgentModelSettings(dict):
    def __init__(__self__, *, model: Optional[_builtins.str] = ..., temperature: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AgentRemoteDialogflowAgent(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent: _builtins.str, flow_id: _builtins.str, environment_id: Optional[_builtins.str] = ..., input_variable_mapping: Optional[Mapping[str, _builtins.str]] = ..., output_variable_mapping: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def agent(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowId")
    def flow_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputVariableMapping")
    def input_variable_mapping(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputVariableMapping")
    def output_variable_mapping(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class AgentToolset(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, toolset: _builtins.str, tool_ids: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def toolset(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolIds")
    def tool_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class AppAudioProcessingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ambient_sound_config: Optional[outputs.AppAudioProcessingConfigAmbientSoundConfig] = ..., barge_in_config: Optional[outputs.AppAudioProcessingConfigBargeInConfig] = ..., inactivity_timeout: Optional[_builtins.str] = ..., synthesize_speech_configs: Optional[Sequence[outputs.AppAudioProcessingConfigSynthesizeSpeechConfig]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ambientSoundConfig")
    def ambient_sound_config(self) -> Optional[outputs.AppAudioProcessingConfigAmbientSoundConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bargeInConfig")
    def barge_in_config(self) -> Optional[outputs.AppAudioProcessingConfigBargeInConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inactivityTimeout")
    def inactivity_timeout(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synthesizeSpeechConfigs")
    def synthesize_speech_configs(self) -> Optional[Sequence[outputs.AppAudioProcessingConfigSynthesizeSpeechConfig]]:
        
        ...
    


@pulumi.output_type
class AppAudioProcessingConfigAmbientSoundConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gcs_uri: Optional[_builtins.str] = ..., prebuilt_ambient_sound: Optional[_builtins.str] = ..., volume_gain_db: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsUri")
    def gcs_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prebuiltAmbientSound")
    def prebuilt_ambient_sound(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeGainDb")
    def volume_gain_db(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AppAudioProcessingConfigBargeInConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, barge_in_awareness: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bargeInAwareness")
    def barge_in_awareness(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AppAudioProcessingConfigSynthesizeSpeechConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, language_code: _builtins.str, speaking_rate: Optional[_builtins.float] = ..., voice: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="speakingRate")
    def speaking_rate(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def voice(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppClientCertificateSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, private_key: _builtins.str, tls_certificate: _builtins.str, passphrase: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsCertificate")
    def tls_certificate(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppDataStoreSettings(dict):
    def __init__(__self__, *, engines: Optional[Sequence[outputs.AppDataStoreSettingsEngine]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engines(self) -> Optional[Sequence[outputs.AppDataStoreSettingsEngine]]:
        
        ...
    


@pulumi.output_type
class AppDataStoreSettingsEngine(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppDefaultChannelProfile(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_type: Optional[_builtins.str] = ..., disable_barge_in_control: Optional[_builtins.bool] = ..., disable_dtmf: Optional[_builtins.bool] = ..., persona_property: Optional[outputs.AppDefaultChannelProfilePersonaProperty] = ..., profile_id: Optional[_builtins.str] = ..., web_widget_config: Optional[outputs.AppDefaultChannelProfileWebWidgetConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableBargeInControl")
    def disable_barge_in_control(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableDtmf")
    def disable_dtmf(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="personaProperty")
    def persona_property(self) -> Optional[outputs.AppDefaultChannelProfilePersonaProperty]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webWidgetConfig")
    def web_widget_config(self) -> Optional[outputs.AppDefaultChannelProfileWebWidgetConfig]:
        
        ...
    


@pulumi.output_type
class AppDefaultChannelProfilePersonaProperty(dict):
    def __init__(__self__, *, persona: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def persona(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppDefaultChannelProfileWebWidgetConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, modality: Optional[_builtins.str] = ..., theme: Optional[_builtins.str] = ..., web_widget_title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def modality(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def theme(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webWidgetTitle")
    def web_widget_title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppEvaluationMetricsThresholds(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, golden_evaluation_metrics_thresholds: Optional[outputs.AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholds] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="goldenEvaluationMetricsThresholds")
    def golden_evaluation_metrics_thresholds(self) -> Optional[outputs.AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholds]:
        
        ...
    


@pulumi.output_type
class AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholds(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expectation_level_metrics_thresholds: Optional[outputs.AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsExpectationLevelMetricsThresholds] = ..., turn_level_metrics_thresholds: Optional[outputs.AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsTurnLevelMetricsThresholds] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectationLevelMetricsThresholds")
    def expectation_level_metrics_thresholds(self) -> Optional[outputs.AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsExpectationLevelMetricsThresholds]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="turnLevelMetricsThresholds")
    def turn_level_metrics_thresholds(self) -> Optional[outputs.AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsTurnLevelMetricsThresholds]:
        
        ...
    


@pulumi.output_type
class AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsExpectationLevelMetricsThresholds(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tool_invocation_parameter_correctness_threshold: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolInvocationParameterCorrectnessThreshold")
    def tool_invocation_parameter_correctness_threshold(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsTurnLevelMetricsThresholds(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, overall_tool_invocation_correctness_threshold: Optional[_builtins.float] = ..., semantic_similarity_success_threshold: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overallToolInvocationCorrectnessThreshold")
    def overall_tool_invocation_correctness_threshold(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="semanticSimilaritySuccessThreshold")
    def semantic_similarity_success_threshold(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AppLanguageSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_language_code: Optional[_builtins.str] = ..., enable_multilingual_support: Optional[_builtins.bool] = ..., fallback_action: Optional[_builtins.str] = ..., supported_language_codes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLanguageCode")
    def default_language_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMultilingualSupport")
    def enable_multilingual_support(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackAction")
    def fallback_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedLanguageCodes")
    def supported_language_codes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class AppLoggingSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, audio_recording_config: Optional[outputs.AppLoggingSettingsAudioRecordingConfig] = ..., bigquery_export_settings: Optional[outputs.AppLoggingSettingsBigqueryExportSettings] = ..., cloud_logging_settings: Optional[outputs.AppLoggingSettingsCloudLoggingSettings] = ..., conversation_logging_settings: Optional[outputs.AppLoggingSettingsConversationLoggingSettings] = ..., redaction_config: Optional[outputs.AppLoggingSettingsRedactionConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioRecordingConfig")
    def audio_recording_config(self) -> Optional[outputs.AppLoggingSettingsAudioRecordingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryExportSettings")
    def bigquery_export_settings(self) -> Optional[outputs.AppLoggingSettingsBigqueryExportSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudLoggingSettings")
    def cloud_logging_settings(self) -> Optional[outputs.AppLoggingSettingsCloudLoggingSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationLoggingSettings")
    def conversation_logging_settings(self) -> Optional[outputs.AppLoggingSettingsConversationLoggingSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactionConfig")
    def redaction_config(self) -> Optional[outputs.AppLoggingSettingsRedactionConfig]:
        
        ...
    


@pulumi.output_type
class AppLoggingSettingsAudioRecordingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gcs_bucket: Optional[_builtins.str] = ..., gcs_path_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsBucket")
    def gcs_bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsPathPrefix")
    def gcs_path_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppLoggingSettingsBigqueryExportSettings(dict):
    def __init__(__self__, *, dataset: Optional[_builtins.str] = ..., enabled: Optional[_builtins.bool] = ..., project: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppLoggingSettingsCloudLoggingSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_cloud_logging: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCloudLogging")
    def enable_cloud_logging(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AppLoggingSettingsConversationLoggingSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disable_conversation_logging: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableConversationLogging")
    def disable_conversation_logging(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AppLoggingSettingsRedactionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deidentify_template: Optional[_builtins.str] = ..., enable_redaction: Optional[_builtins.bool] = ..., inspect_template: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deidentifyTemplate")
    def deidentify_template(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableRedaction")
    def enable_redaction(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectTemplate")
    def inspect_template(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppModelSettings(dict):
    def __init__(__self__, *, model: Optional[_builtins.str] = ..., temperature: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AppTimeZoneSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, time_zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVariableDeclaration(dict):
    def __init__(__self__, *, description: _builtins.str, name: _builtins.str, schema: outputs.AppVariableDeclarationSchema) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schema(self) -> outputs.AppVariableDeclarationSchema:
        
        ...
    


@pulumi.output_type
class AppVariableDeclarationSchema(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, additional_properties: Optional[_builtins.str] = ..., any_of: Optional[_builtins.str] = ..., default: Optional[_builtins.str] = ..., defs: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., enums: Optional[Sequence[_builtins.str]] = ..., items: Optional[_builtins.str] = ..., nullable: Optional[_builtins.bool] = ..., prefix_items: Optional[_builtins.str] = ..., properties: Optional[_builtins.str] = ..., ref: Optional[_builtins.str] = ..., requireds: Optional[Sequence[_builtins.str]] = ..., title: Optional[_builtins.str] = ..., unique_items: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def defs(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enums(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixItems")
    def prefix_items(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requireds(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueItems")
    def unique_items(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshot(dict):
    def __init__(__self__, *, agents: Optional[Sequence[outputs.AppVersionSnapshotAgent]] = ..., apps: Optional[Sequence[outputs.AppVersionSnapshotApp]] = ..., examples: Optional[Sequence[outputs.AppVersionSnapshotExample]] = ..., guardrails: Optional[Sequence[outputs.AppVersionSnapshotGuardrail]] = ..., tools: Optional[Sequence[outputs.AppVersionSnapshotTool]] = ..., toolsets: Optional[Sequence[outputs.AppVersionSnapshotToolset]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def agents(self) -> Optional[Sequence[outputs.AppVersionSnapshotAgent]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def apps(self) -> Optional[Sequence[outputs.AppVersionSnapshotApp]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def examples(self) -> Optional[Sequence[outputs.AppVersionSnapshotExample]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def guardrails(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrail]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tools(self) -> Optional[Sequence[outputs.AppVersionSnapshotTool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def toolsets(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolset]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAgent(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, after_agent_callbacks: Optional[Sequence[outputs.AppVersionSnapshotAgentAfterAgentCallback]] = ..., after_model_callbacks: Optional[Sequence[outputs.AppVersionSnapshotAgentAfterModelCallback]] = ..., after_tool_callbacks: Optional[Sequence[outputs.AppVersionSnapshotAgentAfterToolCallback]] = ..., before_agent_callbacks: Optional[Sequence[outputs.AppVersionSnapshotAgentBeforeAgentCallback]] = ..., before_model_callbacks: Optional[Sequence[outputs.AppVersionSnapshotAgentBeforeModelCallback]] = ..., before_tool_callbacks: Optional[Sequence[outputs.AppVersionSnapshotAgentBeforeToolCallback]] = ..., child_agents: Optional[Sequence[_builtins.str]] = ..., create_time: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., etag: Optional[_builtins.str] = ..., generated_summary: Optional[_builtins.str] = ..., guardrails: Optional[Sequence[_builtins.str]] = ..., instruction: Optional[_builtins.str] = ..., llm_agents: Optional[Sequence[outputs.AppVersionSnapshotAgentLlmAgent]] = ..., model_settings: Optional[Sequence[outputs.AppVersionSnapshotAgentModelSetting]] = ..., name: Optional[_builtins.str] = ..., remote_dialogflow_agents: Optional[Sequence[outputs.AppVersionSnapshotAgentRemoteDialogflowAgent]] = ..., tools: Optional[Sequence[_builtins.str]] = ..., toolsets: Optional[Sequence[outputs.AppVersionSnapshotAgentToolset]] = ..., update_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterAgentCallbacks")
    def after_agent_callbacks(self) -> Optional[Sequence[outputs.AppVersionSnapshotAgentAfterAgentCallback]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterModelCallbacks")
    def after_model_callbacks(self) -> Optional[Sequence[outputs.AppVersionSnapshotAgentAfterModelCallback]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterToolCallbacks")
    def after_tool_callbacks(self) -> Optional[Sequence[outputs.AppVersionSnapshotAgentAfterToolCallback]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeAgentCallbacks")
    def before_agent_callbacks(self) -> Optional[Sequence[outputs.AppVersionSnapshotAgentBeforeAgentCallback]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeModelCallbacks")
    def before_model_callbacks(self) -> Optional[Sequence[outputs.AppVersionSnapshotAgentBeforeModelCallback]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeToolCallbacks")
    def before_tool_callbacks(self) -> Optional[Sequence[outputs.AppVersionSnapshotAgentBeforeToolCallback]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="childAgents")
    def child_agents(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatedSummary")
    def generated_summary(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def guardrails(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instruction(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="llmAgents")
    def llm_agents(self) -> Optional[Sequence[outputs.AppVersionSnapshotAgentLlmAgent]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotAgentModelSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteDialogflowAgents")
    def remote_dialogflow_agents(self) -> Optional[Sequence[outputs.AppVersionSnapshotAgentRemoteDialogflowAgent]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tools(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def toolsets(self) -> Optional[Sequence[outputs.AppVersionSnapshotAgentToolset]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAgentAfterAgentCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ..., python_code: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAgentAfterModelCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ..., python_code: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAgentAfterToolCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ..., python_code: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAgentBeforeAgentCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ..., python_code: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAgentBeforeModelCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ..., python_code: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAgentBeforeToolCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ..., python_code: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAgentLlmAgent(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class AppVersionSnapshotAgentModelSetting(dict):
    def __init__(__self__, *, model: Optional[_builtins.str] = ..., temperature: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAgentRemoteDialogflowAgent(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent: Optional[_builtins.str] = ..., environment_id: Optional[_builtins.str] = ..., flow_id: Optional[_builtins.str] = ..., input_variable_mapping: Optional[Mapping[str, _builtins.str]] = ..., output_variable_mapping: Optional[Mapping[str, _builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def agent(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="flowId")
    def flow_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inputVariableMapping")
    def input_variable_mapping(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="outputVariableMapping")
    def output_variable_mapping(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAgentToolset(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tool_ids: Optional[Sequence[_builtins.str]] = ..., toolset: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolIds")
    def tool_ids(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def toolset(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotApp(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, audio_processing_configs: Optional[Sequence[outputs.AppVersionSnapshotAppAudioProcessingConfig]] = ..., client_certificate_settings: Optional[Sequence[outputs.AppVersionSnapshotAppClientCertificateSetting]] = ..., create_time: Optional[_builtins.str] = ..., data_store_settings: Optional[Sequence[outputs.AppVersionSnapshotAppDataStoreSetting]] = ..., default_channel_profiles: Optional[Sequence[outputs.AppVersionSnapshotAppDefaultChannelProfile]] = ..., deployment_count: Optional[_builtins.int] = ..., description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., etag: Optional[_builtins.str] = ..., evaluation_metrics_thresholds: Optional[Sequence[outputs.AppVersionSnapshotAppEvaluationMetricsThreshold]] = ..., global_instruction: Optional[_builtins.str] = ..., guardrails: Optional[Sequence[_builtins.str]] = ..., language_settings: Optional[Sequence[outputs.AppVersionSnapshotAppLanguageSetting]] = ..., logging_settings: Optional[Sequence[outputs.AppVersionSnapshotAppLoggingSetting]] = ..., metadata: Optional[Mapping[str, _builtins.str]] = ..., model_settings: Optional[Sequence[outputs.AppVersionSnapshotAppModelSetting]] = ..., name: Optional[_builtins.str] = ..., root_agent: Optional[_builtins.str] = ..., time_zone_settings: Optional[Sequence[outputs.AppVersionSnapshotAppTimeZoneSetting]] = ..., update_time: Optional[_builtins.str] = ..., variable_declarations: Optional[Sequence[outputs.AppVersionSnapshotAppVariableDeclaration]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioProcessingConfigs")
    def audio_processing_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppAudioProcessingConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificateSettings")
    def client_certificate_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppClientCertificateSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreSettings")
    def data_store_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppDataStoreSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultChannelProfiles")
    def default_channel_profiles(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppDefaultChannelProfile]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deploymentCount")
    def deployment_count(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="evaluationMetricsThresholds")
    def evaluation_metrics_thresholds(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppEvaluationMetricsThreshold]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="globalInstruction")
    def global_instruction(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def guardrails(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageSettings")
    def language_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppLanguageSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingSettings")
    def logging_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppLoggingSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> Optional[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppModelSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rootAgent")
    def root_agent(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZoneSettings")
    def time_zone_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppTimeZoneSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="variableDeclarations")
    def variable_declarations(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppVariableDeclaration]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppAudioProcessingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ambient_sound_configs: Optional[Sequence[outputs.AppVersionSnapshotAppAudioProcessingConfigAmbientSoundConfig]] = ..., barge_in_configs: Optional[Sequence[outputs.AppVersionSnapshotAppAudioProcessingConfigBargeInConfig]] = ..., inactivity_timeout: Optional[_builtins.str] = ..., synthesize_speech_configs: Optional[Sequence[outputs.AppVersionSnapshotAppAudioProcessingConfigSynthesizeSpeechConfig]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ambientSoundConfigs")
    def ambient_sound_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppAudioProcessingConfigAmbientSoundConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bargeInConfigs")
    def barge_in_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppAudioProcessingConfigBargeInConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inactivityTimeout")
    def inactivity_timeout(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="synthesizeSpeechConfigs")
    def synthesize_speech_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppAudioProcessingConfigSynthesizeSpeechConfig]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppAudioProcessingConfigAmbientSoundConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gcs_uri: Optional[_builtins.str] = ..., prebuilt_ambient_sound: Optional[_builtins.str] = ..., volume_gain_db: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsUri")
    def gcs_uri(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prebuiltAmbientSound")
    def prebuilt_ambient_sound(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="volumeGainDb")
    def volume_gain_db(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppAudioProcessingConfigBargeInConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, barge_in_awareness: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bargeInAwareness")
    def barge_in_awareness(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppAudioProcessingConfigSynthesizeSpeechConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, language_code: _builtins.str, speaking_rate: Optional[_builtins.float] = ..., voice: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="speakingRate")
    def speaking_rate(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def voice(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppClientCertificateSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, passphrase: Optional[_builtins.str] = ..., private_key: Optional[_builtins.str] = ..., tls_certificate: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsCertificate")
    def tls_certificate(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppDataStoreSetting(dict):
    def __init__(__self__, *, engines: Optional[Sequence[outputs.AppVersionSnapshotAppDataStoreSettingEngine]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engines(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppDataStoreSettingEngine]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppDataStoreSettingEngine(dict):
    def __init__(__self__, *, name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppDefaultChannelProfile(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_type: Optional[_builtins.str] = ..., disable_barge_in_control: Optional[_builtins.bool] = ..., disable_dtmf: Optional[_builtins.bool] = ..., persona_properties: Optional[Sequence[outputs.AppVersionSnapshotAppDefaultChannelProfilePersonaProperty]] = ..., profile_id: Optional[_builtins.str] = ..., web_widget_configs: Optional[Sequence[outputs.AppVersionSnapshotAppDefaultChannelProfileWebWidgetConfig]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableBargeInControl")
    def disable_barge_in_control(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableDtmf")
    def disable_dtmf(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="personaProperties")
    def persona_properties(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppDefaultChannelProfilePersonaProperty]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webWidgetConfigs")
    def web_widget_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppDefaultChannelProfileWebWidgetConfig]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppDefaultChannelProfilePersonaProperty(dict):
    def __init__(__self__, *, persona: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def persona(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppDefaultChannelProfileWebWidgetConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, modality: Optional[_builtins.str] = ..., theme: Optional[_builtins.str] = ..., web_widget_title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def modality(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def theme(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webWidgetTitle")
    def web_widget_title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppEvaluationMetricsThreshold(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, golden_evaluation_metrics_thresholds: Optional[Sequence[outputs.AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThreshold]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="goldenEvaluationMetricsThresholds")
    def golden_evaluation_metrics_thresholds(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThreshold]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThreshold(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, expectation_level_metrics_thresholds: Optional[Sequence[outputs.AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdExpectationLevelMetricsThreshold]] = ..., turn_level_metrics_thresholds: Optional[Sequence[outputs.AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdTurnLevelMetricsThreshold]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="expectationLevelMetricsThresholds")
    def expectation_level_metrics_thresholds(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdExpectationLevelMetricsThreshold]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="turnLevelMetricsThresholds")
    def turn_level_metrics_thresholds(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdTurnLevelMetricsThreshold]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdExpectationLevelMetricsThreshold(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tool_invocation_parameter_correctness_threshold: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolInvocationParameterCorrectnessThreshold")
    def tool_invocation_parameter_correctness_threshold(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdTurnLevelMetricsThreshold(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, overall_tool_invocation_correctness_threshold: Optional[_builtins.float] = ..., semantic_similarity_success_threshold: Optional[_builtins.int] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="overallToolInvocationCorrectnessThreshold")
    def overall_tool_invocation_correctness_threshold(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="semanticSimilaritySuccessThreshold")
    def semantic_similarity_success_threshold(self) -> Optional[_builtins.int]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppLanguageSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_language_code: Optional[_builtins.str] = ..., enable_multilingual_support: Optional[_builtins.bool] = ..., fallback_action: Optional[_builtins.str] = ..., supported_language_codes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLanguageCode")
    def default_language_code(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMultilingualSupport")
    def enable_multilingual_support(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fallbackAction")
    def fallback_action(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedLanguageCodes")
    def supported_language_codes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppLoggingSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, audio_recording_configs: Optional[Sequence[outputs.AppVersionSnapshotAppLoggingSettingAudioRecordingConfig]] = ..., bigquery_export_settings: Optional[Sequence[outputs.AppVersionSnapshotAppLoggingSettingBigqueryExportSetting]] = ..., cloud_logging_settings: Optional[Sequence[outputs.AppVersionSnapshotAppLoggingSettingCloudLoggingSetting]] = ..., conversation_logging_settings: Optional[Sequence[outputs.AppVersionSnapshotAppLoggingSettingConversationLoggingSetting]] = ..., redaction_configs: Optional[Sequence[outputs.AppVersionSnapshotAppLoggingSettingRedactionConfig]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="audioRecordingConfigs")
    def audio_recording_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppLoggingSettingAudioRecordingConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bigqueryExportSettings")
    def bigquery_export_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppLoggingSettingBigqueryExportSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="cloudLoggingSettings")
    def cloud_logging_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppLoggingSettingCloudLoggingSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conversationLoggingSettings")
    def conversation_logging_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppLoggingSettingConversationLoggingSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="redactionConfigs")
    def redaction_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppLoggingSettingRedactionConfig]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppLoggingSettingAudioRecordingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, gcs_bucket: Optional[_builtins.str] = ..., gcs_path_prefix: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsBucket")
    def gcs_bucket(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gcsPathPrefix")
    def gcs_path_prefix(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppLoggingSettingBigqueryExportSetting(dict):
    def __init__(__self__, *, dataset: Optional[_builtins.str] = ..., enabled: Optional[_builtins.bool] = ..., project: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppLoggingSettingCloudLoggingSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, enable_cloud_logging: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableCloudLogging")
    def enable_cloud_logging(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppLoggingSettingConversationLoggingSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disable_conversation_logging: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableConversationLogging")
    def disable_conversation_logging(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppLoggingSettingRedactionConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, deidentify_template: Optional[_builtins.str] = ..., enable_redaction: Optional[_builtins.bool] = ..., inspect_template: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deidentifyTemplate")
    def deidentify_template(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableRedaction")
    def enable_redaction(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="inspectTemplate")
    def inspect_template(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppModelSetting(dict):
    def __init__(__self__, *, model: Optional[_builtins.str] = ..., temperature: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppTimeZoneSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, time_zone: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppVariableDeclaration(dict):
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., schemas: Optional[Sequence[outputs.AppVersionSnapshotAppVariableDeclarationSchema]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def schemas(self) -> Optional[Sequence[outputs.AppVersionSnapshotAppVariableDeclarationSchema]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotAppVariableDeclarationSchema(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_properties: Optional[_builtins.str] = ..., any_of: Optional[_builtins.str] = ..., default: Optional[_builtins.str] = ..., defs: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., enums: Optional[Sequence[_builtins.str]] = ..., items: Optional[_builtins.str] = ..., nullable: Optional[_builtins.bool] = ..., prefix_items: Optional[_builtins.str] = ..., properties: Optional[_builtins.str] = ..., ref: Optional[_builtins.str] = ..., requireds: Optional[Sequence[_builtins.str]] = ..., type: Optional[_builtins.str] = ..., unique_items: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def defs(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enums(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixItems")
    def prefix_items(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requireds(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueItems")
    def unique_items(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotExample(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, create_time: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., entry_agent: Optional[_builtins.str] = ..., etag: Optional[_builtins.str] = ..., invalid: Optional[_builtins.bool] = ..., messages: Optional[Sequence[outputs.AppVersionSnapshotExampleMessage]] = ..., name: Optional[_builtins.str] = ..., update_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="entryAgent")
    def entry_agent(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def invalid(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def messages(self) -> Optional[Sequence[outputs.AppVersionSnapshotExampleMessage]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotExampleMessage(dict):
    def __init__(__self__, *, chunks: Optional[Sequence[outputs.AppVersionSnapshotExampleMessageChunk]] = ..., role: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def chunks(self) -> Optional[Sequence[outputs.AppVersionSnapshotExampleMessageChunk]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotExampleMessageChunk(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_transfers: Optional[Sequence[outputs.AppVersionSnapshotExampleMessageChunkAgentTransfer]] = ..., images: Optional[Sequence[outputs.AppVersionSnapshotExampleMessageChunkImage]] = ..., text: Optional[_builtins.str] = ..., tool_calls: Optional[Sequence[outputs.AppVersionSnapshotExampleMessageChunkToolCall]] = ..., tool_responses: Optional[Sequence[outputs.AppVersionSnapshotExampleMessageChunkToolResponse]] = ..., updated_variables: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentTransfers")
    def agent_transfers(self) -> Optional[Sequence[outputs.AppVersionSnapshotExampleMessageChunkAgentTransfer]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def images(self) -> Optional[Sequence[outputs.AppVersionSnapshotExampleMessageChunkImage]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolCalls")
    def tool_calls(self) -> Optional[Sequence[outputs.AppVersionSnapshotExampleMessageChunkToolCall]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolResponses")
    def tool_responses(self) -> Optional[Sequence[outputs.AppVersionSnapshotExampleMessageChunkToolResponse]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedVariables")
    def updated_variables(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotExampleMessageChunkAgentTransfer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., target_agent: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAgent")
    def target_agent(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotExampleMessageChunkImage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data: Optional[_builtins.str] = ..., mime_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotExampleMessageChunkToolCall(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, args: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., tool: Optional[_builtins.str] = ..., toolset_tools: Optional[Sequence[outputs.AppVersionSnapshotExampleMessageChunkToolCallToolsetTool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tool(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolsetTools")
    def toolset_tools(self) -> Optional[Sequence[outputs.AppVersionSnapshotExampleMessageChunkToolCallToolsetTool]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotExampleMessageChunkToolCallToolsetTool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tool_id: Optional[_builtins.str] = ..., toolset: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolId")
    def tool_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def toolset(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotExampleMessageChunkToolResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, display_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., response: Optional[_builtins.str] = ..., tool: Optional[_builtins.str] = ..., toolset_tools: Optional[Sequence[outputs.AppVersionSnapshotExampleMessageChunkToolResponseToolsetTool]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tool(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolsetTools")
    def toolset_tools(self) -> Optional[Sequence[outputs.AppVersionSnapshotExampleMessageChunkToolResponseToolsetTool]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotExampleMessageChunkToolResponseToolsetTool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, tool_id: Optional[_builtins.str] = ..., toolset: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolId")
    def tool_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def toolset(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrail(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, actions: Optional[Sequence[outputs.AppVersionSnapshotGuardrailAction]] = ..., code_callbacks: Optional[Sequence[outputs.AppVersionSnapshotGuardrailCodeCallback]] = ..., content_filters: Optional[Sequence[outputs.AppVersionSnapshotGuardrailContentFilter]] = ..., create_time: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., enabled: Optional[_builtins.bool] = ..., etag: Optional[_builtins.str] = ..., llm_policies: Optional[Sequence[outputs.AppVersionSnapshotGuardrailLlmPolicy]] = ..., llm_prompt_securities: Optional[Sequence[outputs.AppVersionSnapshotGuardrailLlmPromptSecurity]] = ..., model_safeties: Optional[Sequence[outputs.AppVersionSnapshotGuardrailModelSafety]] = ..., name: Optional[_builtins.str] = ..., update_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def actions(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeCallbacks")
    def code_callbacks(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailCodeCallback]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentFilters")
    def content_filters(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailContentFilter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="llmPolicies")
    def llm_policies(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailLlmPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="llmPromptSecurities")
    def llm_prompt_securities(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailLlmPromptSecurity]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSafeties")
    def model_safeties(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailModelSafety]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, generative_answers: Optional[Sequence[outputs.AppVersionSnapshotGuardrailActionGenerativeAnswer]] = ..., respond_immediatelies: Optional[Sequence[outputs.AppVersionSnapshotGuardrailActionRespondImmediately]] = ..., transfer_agents: Optional[Sequence[outputs.AppVersionSnapshotGuardrailActionTransferAgent]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generativeAnswers")
    def generative_answers(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailActionGenerativeAnswer]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="respondImmediatelies")
    def respond_immediatelies(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailActionRespondImmediately]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferAgents")
    def transfer_agents(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailActionTransferAgent]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailActionGenerativeAnswer(dict):
    def __init__(__self__, *, prompt: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailActionRespondImmediately(dict):
    def __init__(__self__, *, responses: Optional[Sequence[outputs.AppVersionSnapshotGuardrailActionRespondImmediatelyResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def responses(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailActionRespondImmediatelyResponse]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailActionRespondImmediatelyResponse(dict):
    def __init__(__self__, *, disabled: Optional[_builtins.bool] = ..., text: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailActionTransferAgent(dict):
    def __init__(__self__, *, agent: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def agent(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailCodeCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, after_agent_callbacks: Optional[Sequence[outputs.AppVersionSnapshotGuardrailCodeCallbackAfterAgentCallback]] = ..., after_model_callbacks: Optional[Sequence[outputs.AppVersionSnapshotGuardrailCodeCallbackAfterModelCallback]] = ..., before_agent_callbacks: Optional[Sequence[outputs.AppVersionSnapshotGuardrailCodeCallbackBeforeAgentCallback]] = ..., before_model_callbacks: Optional[Sequence[outputs.AppVersionSnapshotGuardrailCodeCallbackBeforeModelCallback]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterAgentCallbacks")
    def after_agent_callbacks(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailCodeCallbackAfterAgentCallback]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterModelCallbacks")
    def after_model_callbacks(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailCodeCallbackAfterModelCallback]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeAgentCallbacks")
    def before_agent_callbacks(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailCodeCallbackBeforeAgentCallback]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeModelCallbacks")
    def before_model_callbacks(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailCodeCallbackBeforeModelCallback]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailCodeCallbackAfterAgentCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ..., python_code: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailCodeCallbackAfterModelCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ..., python_code: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailCodeCallbackBeforeAgentCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ..., python_code: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailCodeCallbackBeforeModelCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ..., python_code: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailContentFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, banned_contents: Optional[Sequence[_builtins.str]] = ..., banned_contents_in_agent_responses: Optional[Sequence[_builtins.str]] = ..., banned_contents_in_user_inputs: Optional[Sequence[_builtins.str]] = ..., disregard_diacritics: Optional[_builtins.bool] = ..., match_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bannedContents")
    def banned_contents(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bannedContentsInAgentResponses")
    def banned_contents_in_agent_responses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bannedContentsInUserInputs")
    def banned_contents_in_user_inputs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disregardDiacritics")
    def disregard_diacritics(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchType")
    def match_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailLlmPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fail_open: Optional[_builtins.bool] = ..., max_conversation_messages: Optional[_builtins.int] = ..., model_settings: Optional[Sequence[outputs.AppVersionSnapshotGuardrailLlmPolicyModelSetting]] = ..., policy_scope: Optional[_builtins.str] = ..., prompt: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOpen")
    def fail_open(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConversationMessages")
    def max_conversation_messages(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailLlmPolicyModelSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyScope")
    def policy_scope(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailLlmPolicyModelSetting(dict):
    def __init__(__self__, *, model: Optional[_builtins.str] = ..., temperature: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailLlmPromptSecurity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_policies: Optional[Sequence[outputs.AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicy]] = ..., default_settings: Optional[Sequence[outputs.AppVersionSnapshotGuardrailLlmPromptSecurityDefaultSetting]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPolicies")
    def custom_policies(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSettings")
    def default_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailLlmPromptSecurityDefaultSetting]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, fail_open: Optional[_builtins.bool] = ..., max_conversation_messages: Optional[_builtins.int] = ..., model_settings: Optional[Sequence[outputs.AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicyModelSetting]] = ..., policy_scope: Optional[_builtins.str] = ..., prompt: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOpen")
    def fail_open(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConversationMessages")
    def max_conversation_messages(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicyModelSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyScope")
    def policy_scope(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicyModelSetting(dict):
    def __init__(__self__, *, model: Optional[_builtins.str] = ..., temperature: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailLlmPromptSecurityDefaultSetting(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_prompt_template: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultPromptTemplate")
    def default_prompt_template(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailModelSafety(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, safety_settings: Optional[Sequence[outputs.AppVersionSnapshotGuardrailModelSafetySafetySetting]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="safetySettings")
    def safety_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotGuardrailModelSafetySafetySetting]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotGuardrailModelSafetySafetySetting(dict):
    def __init__(__self__, *, category: Optional[_builtins.str] = ..., threshold: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotTool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_functions: Optional[Sequence[outputs.AppVersionSnapshotToolClientFunction]] = ..., create_time: Optional[_builtins.str] = ..., data_store_tools: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreTool]] = ..., display_name: Optional[_builtins.str] = ..., etag: Optional[_builtins.str] = ..., execution_type: Optional[_builtins.str] = ..., generated_summary: Optional[_builtins.str] = ..., google_search_tools: Optional[Sequence[outputs.AppVersionSnapshotToolGoogleSearchTool]] = ..., name: Optional[_builtins.str] = ..., open_api_tools: Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiTool]] = ..., python_functions: Optional[Sequence[outputs.AppVersionSnapshotToolPythonFunction]] = ..., system_tools: Optional[Sequence[outputs.AppVersionSnapshotToolSystemTool]] = ..., update_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientFunctions")
    def client_functions(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolClientFunction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreTools")
    def data_store_tools(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreTool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionType")
    def execution_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatedSummary")
    def generated_summary(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="googleSearchTools")
    def google_search_tools(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolGoogleSearchTool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openApiTools")
    def open_api_tools(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiTool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonFunctions")
    def python_functions(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolPythonFunction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="systemTools")
    def system_tools(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolSystemTool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolClientFunction(dict):
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., parameters: Optional[Sequence[outputs.AppVersionSnapshotToolClientFunctionParameter]] = ..., responses: Optional[Sequence[outputs.AppVersionSnapshotToolClientFunctionResponse]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolClientFunctionParameter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def responses(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolClientFunctionResponse]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolClientFunctionParameter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_properties: Optional[_builtins.str] = ..., any_of: Optional[_builtins.str] = ..., default: Optional[_builtins.str] = ..., defs: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., enums: Optional[Sequence[_builtins.str]] = ..., items: Optional[_builtins.str] = ..., nullable: Optional[_builtins.bool] = ..., prefix_items: Optional[_builtins.str] = ..., properties: Optional[_builtins.str] = ..., ref: Optional[_builtins.str] = ..., requireds: Optional[Sequence[_builtins.str]] = ..., type: Optional[_builtins.str] = ..., unique_items: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def defs(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enums(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixItems")
    def prefix_items(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requireds(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueItems")
    def unique_items(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolClientFunctionResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, additional_properties: Optional[_builtins.str] = ..., any_of: Optional[_builtins.str] = ..., default: Optional[_builtins.str] = ..., defs: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., enums: Optional[Sequence[_builtins.str]] = ..., items: Optional[_builtins.str] = ..., nullable: Optional[_builtins.bool] = ..., prefix_items: Optional[_builtins.str] = ..., properties: Optional[_builtins.str] = ..., ref: Optional[_builtins.str] = ..., requireds: Optional[Sequence[_builtins.str]] = ..., type: Optional[_builtins.str] = ..., unique_items: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def defs(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enums(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixItems")
    def prefix_items(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requireds(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueItems")
    def unique_items(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreTool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boost_specs: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolBoostSpec]] = ..., description: Optional[_builtins.str] = ..., engine_sources: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolEngineSource]] = ..., max_results: Optional[_builtins.int] = ..., modality_configs: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolModalityConfig]] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boostSpecs")
    def boost_specs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolBoostSpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineSources")
    def engine_sources(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolEngineSource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxResults")
    def max_results(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modalityConfigs")
    def modality_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolModalityConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreToolBoostSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_stores: Optional[Sequence[_builtins.str]] = ..., specs: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolBoostSpecSpec]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStores")
    def data_stores(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def specs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolBoostSpecSpec]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreToolBoostSpecSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, condition_boost_specs: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpec]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionBoostSpecs")
    def condition_boost_specs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpec]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, boost: Optional[_builtins.float] = ..., boost_control_specs: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpec]] = ..., condition: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def boost(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boostControlSpecs")
    def boost_control_specs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attribute_type: Optional[_builtins.str] = ..., control_points: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPoint]] = ..., field_name: Optional[_builtins.str] = ..., interpolation_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeType")
    def attribute_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPoints")
    def control_points(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPoint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpolationType")
    def interpolation_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPoint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attribute_value: Optional[_builtins.str] = ..., boost_amount: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boostAmount")
    def boost_amount(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreToolEngineSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_store_sources: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSource]] = ..., engine: Optional[_builtins.str] = ..., filter: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreSources")
    def data_store_sources(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_stores: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStore]] = ..., filter: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStores")
    def data_stores(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStore]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStore(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, connector_configs: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfig]] = ..., create_time: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., document_processing_mode: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorConfigs")
    def connector_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentProcessingMode")
    def document_processing_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, collection: Optional[_builtins.str] = ..., collection_display_name: Optional[_builtins.str] = ..., data_source: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collection(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionDisplayName")
    def collection_display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreToolModalityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, grounding_configs: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolModalityConfigGroundingConfig]] = ..., modality_type: Optional[_builtins.str] = ..., rewriter_configs: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfig]] = ..., summarization_configs: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfig]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groundingConfigs")
    def grounding_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolModalityConfigGroundingConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modalityType")
    def modality_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rewriterConfigs")
    def rewriter_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="summarizationConfigs")
    def summarization_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfig]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreToolModalityConfigGroundingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disabled: Optional[_builtins.bool] = ..., grounding_level: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groundingLevel")
    def grounding_level(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disabled: Optional[_builtins.bool] = ..., model_settings: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfigModelSetting]] = ..., prompt: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfigModelSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfigModelSetting(dict):
    def __init__(__self__, *, model: Optional[_builtins.str] = ..., temperature: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disabled: Optional[_builtins.bool] = ..., model_settings: Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfigModelSetting]] = ..., prompt: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfigModelSetting]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfigModelSetting(dict):
    def __init__(__self__, *, model: Optional[_builtins.str] = ..., temperature: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolGoogleSearchTool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., exclude_domains: Optional[Sequence[_builtins.str]] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeDomains")
    def exclude_domains(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolOpenApiTool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_authentications: Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolApiAuthentication]] = ..., description: Optional[_builtins.str] = ..., ignore_unknown_fields: Optional[_builtins.bool] = ..., name: Optional[_builtins.str] = ..., open_api_schema: Optional[_builtins.str] = ..., service_directory_configs: Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolServiceDirectoryConfig]] = ..., tls_configs: Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolTlsConfig]] = ..., url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiAuthentications")
    def api_authentications(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolApiAuthentication]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreUnknownFields")
    def ignore_unknown_fields(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openApiSchema")
    def open_api_schema(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfigs")
    def service_directory_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolServiceDirectoryConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsConfigs")
    def tls_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolTlsConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolOpenApiToolApiAuthentication(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_key_configs: Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolApiAuthenticationApiKeyConfig]] = ..., oauth_configs: Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolApiAuthenticationOauthConfig]] = ..., service_account_auth_configs: Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAccountAuthConfig]] = ..., service_agent_id_token_auth_configs: Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfig]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyConfigs")
    def api_key_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolApiAuthenticationApiKeyConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthConfigs")
    def oauth_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolApiAuthenticationOauthConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountAuthConfigs")
    def service_account_auth_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAccountAuthConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAgentIdTokenAuthConfigs")
    def service_agent_id_token_auth_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfig]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolOpenApiToolApiAuthenticationApiKeyConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_key_secret_version: Optional[_builtins.str] = ..., key_name: Optional[_builtins.str] = ..., request_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeySecretVersion")
    def api_key_secret_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestLocation")
    def request_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolOpenApiToolApiAuthenticationOauthConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., client_secret_version: Optional[_builtins.str] = ..., oauth_grant_type: Optional[_builtins.str] = ..., scopes: Optional[Sequence[_builtins.str]] = ..., token_endpoint: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretVersion")
    def client_secret_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthGrantType")
    def oauth_grant_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAccountAuthConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_account: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfig(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolOpenApiToolServiceDirectoryConfig(dict):
    def __init__(__self__, *, service: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolOpenApiToolTlsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ca_certs: Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolTlsConfigCaCert]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolOpenApiToolTlsConfigCaCert]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolOpenApiToolTlsConfigCaCert(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cert: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolPythonFunction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., python_code: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolSystemTool(dict):
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolset(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, create_time: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., etag: Optional[_builtins.str] = ..., execution_type: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., open_api_toolsets: Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolset]] = ..., update_time: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="executionType")
    def execution_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openApiToolsets")
    def open_api_toolsets(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolset]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolsetOpenApiToolset(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_authentications: Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetApiAuthentication]] = ..., ignore_unknown_fields: Optional[_builtins.bool] = ..., open_api_schema: Optional[_builtins.str] = ..., service_directory_configs: Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetServiceDirectoryConfig]] = ..., tls_configs: Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetTlsConfig]] = ..., url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiAuthentications")
    def api_authentications(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetApiAuthentication]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreUnknownFields")
    def ignore_unknown_fields(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openApiSchema")
    def open_api_schema(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfigs")
    def service_directory_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetServiceDirectoryConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsConfigs")
    def tls_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetTlsConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolsetOpenApiToolsetApiAuthentication(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_key_configs: Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationApiKeyConfig]] = ..., bearer_token_configs: Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationBearerTokenConfig]] = ..., oauth_configs: Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationOauthConfig]] = ..., service_account_auth_configs: Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfig]] = ..., service_agent_id_token_auth_configs: Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfig]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyConfigs")
    def api_key_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationApiKeyConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bearerTokenConfigs")
    def bearer_token_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationBearerTokenConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthConfigs")
    def oauth_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationOauthConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountAuthConfigs")
    def service_account_auth_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAgentIdTokenAuthConfigs")
    def service_agent_id_token_auth_configs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfig]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationApiKeyConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_key_secret_version: Optional[_builtins.str] = ..., key_name: Optional[_builtins.str] = ..., request_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeySecretVersion")
    def api_key_secret_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestLocation")
    def request_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationBearerTokenConfig(dict):
    def __init__(__self__, *, token: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationOauthConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., client_secret_version: Optional[_builtins.str] = ..., oauth_grant_type: Optional[_builtins.str] = ..., scopes: Optional[Sequence[_builtins.str]] = ..., token_endpoint: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretVersion")
    def client_secret_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthGrantType")
    def oauth_grant_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_account: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfig(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolsetOpenApiToolsetServiceDirectoryConfig(dict):
    def __init__(__self__, *, service: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolsetOpenApiToolsetTlsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ca_certs: Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetTlsConfigCaCert]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(self) -> Optional[Sequence[outputs.AppVersionSnapshotToolsetOpenApiToolsetTlsConfigCaCert]]:
        
        ...
    


@pulumi.output_type
class AppVersionSnapshotToolsetOpenApiToolsetTlsConfigCaCert(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cert: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentChannelProfile(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, channel_type: Optional[_builtins.str] = ..., disable_barge_in_control: Optional[_builtins.bool] = ..., disable_dtmf: Optional[_builtins.bool] = ..., persona_property: Optional[outputs.DeploymentChannelProfilePersonaProperty] = ..., profile_id: Optional[_builtins.str] = ..., web_widget_config: Optional[outputs.DeploymentChannelProfileWebWidgetConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableBargeInControl")
    def disable_barge_in_control(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disableDtmf")
    def disable_dtmf(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="personaProperty")
    def persona_property(self) -> Optional[outputs.DeploymentChannelProfilePersonaProperty]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webWidgetConfig")
    def web_widget_config(self) -> Optional[outputs.DeploymentChannelProfileWebWidgetConfig]:
        
        ...
    


@pulumi.output_type
class DeploymentChannelProfilePersonaProperty(dict):
    def __init__(__self__, *, persona: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def persona(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class DeploymentChannelProfileWebWidgetConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, modality: Optional[_builtins.str] = ..., theme: Optional[_builtins.str] = ..., web_widget_title: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def modality(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def theme(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="webWidgetTitle")
    def web_widget_title(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExampleMessage(dict):
    def __init__(__self__, *, chunks: Optional[Sequence[outputs.ExampleMessageChunk]] = ..., role: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def chunks(self) -> Optional[Sequence[outputs.ExampleMessageChunk]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExampleMessageChunk(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, agent_transfer: Optional[outputs.ExampleMessageChunkAgentTransfer] = ..., image: Optional[outputs.ExampleMessageChunkImage] = ..., text: Optional[_builtins.str] = ..., tool_call: Optional[outputs.ExampleMessageChunkToolCall] = ..., tool_response: Optional[outputs.ExampleMessageChunkToolResponse] = ..., updated_variables: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentTransfer")
    def agent_transfer(self) -> Optional[outputs.ExampleMessageChunkAgentTransfer]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[outputs.ExampleMessageChunkImage]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolCall")
    def tool_call(self) -> Optional[outputs.ExampleMessageChunkToolCall]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolResponse")
    def tool_response(self) -> Optional[outputs.ExampleMessageChunkToolResponse]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updatedVariables")
    def updated_variables(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExampleMessageChunkAgentTransfer(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, target_agent: _builtins.str, display_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="targetAgent")
    def target_agent(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExampleMessageChunkImage(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data: _builtins.str, mime_type: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def data(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ExampleMessageChunkToolCall(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, args: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., tool: Optional[_builtins.str] = ..., toolset_tool: Optional[outputs.ExampleMessageChunkToolCallToolsetTool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tool(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolsetTool")
    def toolset_tool(self) -> Optional[outputs.ExampleMessageChunkToolCallToolsetTool]:
        
        ...
    


@pulumi.output_type
class ExampleMessageChunkToolCallToolsetTool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, toolset: _builtins.str, tool_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def toolset(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolId")
    def tool_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ExampleMessageChunkToolResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, response: _builtins.str, display_name: Optional[_builtins.str] = ..., id: Optional[_builtins.str] = ..., tool: Optional[_builtins.str] = ..., toolset_tool: Optional[outputs.ExampleMessageChunkToolResponseToolsetTool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tool(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolsetTool")
    def toolset_tool(self) -> Optional[outputs.ExampleMessageChunkToolResponseToolsetTool]:
        
        ...
    


@pulumi.output_type
class ExampleMessageChunkToolResponseToolsetTool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, toolset: _builtins.str, tool_id: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def toolset(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="toolId")
    def tool_id(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GuardrailAction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, generative_answer: Optional[outputs.GuardrailActionGenerativeAnswer] = ..., respond_immediately: Optional[outputs.GuardrailActionRespondImmediately] = ..., transfer_agent: Optional[outputs.GuardrailActionTransferAgent] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generativeAnswer")
    def generative_answer(self) -> Optional[outputs.GuardrailActionGenerativeAnswer]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="respondImmediately")
    def respond_immediately(self) -> Optional[outputs.GuardrailActionRespondImmediately]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="transferAgent")
    def transfer_agent(self) -> Optional[outputs.GuardrailActionTransferAgent]:
        
        ...
    


@pulumi.output_type
class GuardrailActionGenerativeAnswer(dict):
    def __init__(__self__, *, prompt: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GuardrailActionRespondImmediately(dict):
    def __init__(__self__, *, responses: Sequence[outputs.GuardrailActionRespondImmediatelyResponse]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def responses(self) -> Sequence[outputs.GuardrailActionRespondImmediatelyResponse]:
        
        ...
    


@pulumi.output_type
class GuardrailActionRespondImmediatelyResponse(dict):
    def __init__(__self__, *, text: _builtins.str, disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def text(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class GuardrailActionTransferAgent(dict):
    def __init__(__self__, *, agent: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def agent(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class GuardrailCodeCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, after_agent_callback: Optional[outputs.GuardrailCodeCallbackAfterAgentCallback] = ..., after_model_callback: Optional[outputs.GuardrailCodeCallbackAfterModelCallback] = ..., before_agent_callback: Optional[outputs.GuardrailCodeCallbackBeforeAgentCallback] = ..., before_model_callback: Optional[outputs.GuardrailCodeCallbackBeforeModelCallback] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterAgentCallback")
    def after_agent_callback(self) -> Optional[outputs.GuardrailCodeCallbackAfterAgentCallback]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterModelCallback")
    def after_model_callback(self) -> Optional[outputs.GuardrailCodeCallbackAfterModelCallback]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeAgentCallback")
    def before_agent_callback(self) -> Optional[outputs.GuardrailCodeCallbackBeforeAgentCallback]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeModelCallback")
    def before_model_callback(self) -> Optional[outputs.GuardrailCodeCallbackBeforeModelCallback]:
        
        ...
    


@pulumi.output_type
class GuardrailCodeCallbackAfterAgentCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, python_code: _builtins.str, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class GuardrailCodeCallbackAfterModelCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, python_code: _builtins.str, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class GuardrailCodeCallbackBeforeAgentCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, python_code: _builtins.str, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class GuardrailCodeCallbackBeforeModelCallback(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, python_code: _builtins.str, description: Optional[_builtins.str] = ..., disabled: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class GuardrailContentFilter(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, match_type: _builtins.str, banned_contents: Optional[Sequence[_builtins.str]] = ..., banned_contents_in_agent_responses: Optional[Sequence[_builtins.str]] = ..., banned_contents_in_user_inputs: Optional[Sequence[_builtins.str]] = ..., disregard_diacritics: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="matchType")
    def match_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bannedContents")
    def banned_contents(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bannedContentsInAgentResponses")
    def banned_contents_in_agent_responses(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bannedContentsInUserInputs")
    def banned_contents_in_user_inputs(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="disregardDiacritics")
    def disregard_diacritics(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class GuardrailLlmPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, policy_scope: _builtins.str, prompt: _builtins.str, allow_short_utterance: Optional[_builtins.bool] = ..., fail_open: Optional[_builtins.bool] = ..., max_conversation_messages: Optional[_builtins.int] = ..., model_settings: Optional[outputs.GuardrailLlmPolicyModelSettings] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyScope")
    def policy_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowShortUtterance")
    def allow_short_utterance(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOpen")
    def fail_open(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConversationMessages")
    def max_conversation_messages(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(self) -> Optional[outputs.GuardrailLlmPolicyModelSettings]:
        
        ...
    


@pulumi.output_type
class GuardrailLlmPolicyModelSettings(dict):
    def __init__(__self__, *, model: Optional[_builtins.str] = ..., temperature: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class GuardrailLlmPromptSecurity(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, custom_policy: Optional[outputs.GuardrailLlmPromptSecurityCustomPolicy] = ..., default_settings: Optional[outputs.GuardrailLlmPromptSecurityDefaultSettings] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customPolicy")
    def custom_policy(self) -> Optional[outputs.GuardrailLlmPromptSecurityCustomPolicy]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultSettings")
    def default_settings(self) -> Optional[outputs.GuardrailLlmPromptSecurityDefaultSettings]:
        
        ...
    


@pulumi.output_type
class GuardrailLlmPromptSecurityCustomPolicy(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, policy_scope: _builtins.str, prompt: _builtins.str, allow_short_utterance: Optional[_builtins.bool] = ..., fail_open: Optional[_builtins.bool] = ..., max_conversation_messages: Optional[_builtins.int] = ..., model_settings: Optional[outputs.GuardrailLlmPromptSecurityCustomPolicyModelSettings] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="policyScope")
    def policy_scope(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="allowShortUtterance")
    def allow_short_utterance(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failOpen")
    def fail_open(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxConversationMessages")
    def max_conversation_messages(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(self) -> Optional[outputs.GuardrailLlmPromptSecurityCustomPolicyModelSettings]:
        
        ...
    


@pulumi.output_type
class GuardrailLlmPromptSecurityCustomPolicyModelSettings(dict):
    def __init__(__self__, *, model: Optional[_builtins.str] = ..., temperature: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class GuardrailLlmPromptSecurityDefaultSettings(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, default_prompt_template: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultPromptTemplate")
    def default_prompt_template(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class GuardrailModelSafety(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, safety_settings: Sequence[outputs.GuardrailModelSafetySafetySetting]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="safetySettings")
    def safety_settings(self) -> Sequence[outputs.GuardrailModelSafetySafetySetting]:
        
        ...
    


@pulumi.output_type
class GuardrailModelSafetySafetySetting(dict):
    def __init__(__self__, *, category: _builtins.str, threshold: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def category(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ToolClientFunction(dict):
    def __init__(__self__, *, name: _builtins.str, description: Optional[_builtins.str] = ..., parameters: Optional[outputs.ToolClientFunctionParameters] = ..., response: Optional[outputs.ToolClientFunctionResponse] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[outputs.ToolClientFunctionParameters]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[outputs.ToolClientFunctionResponse]:
        
        ...
    


@pulumi.output_type
class ToolClientFunctionParameters(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, additional_properties: Optional[_builtins.str] = ..., any_of: Optional[_builtins.str] = ..., default: Optional[_builtins.str] = ..., defs: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., enums: Optional[Sequence[_builtins.str]] = ..., items: Optional[_builtins.str] = ..., max_items: Optional[_builtins.int] = ..., maximum: Optional[_builtins.float] = ..., min_items: Optional[_builtins.int] = ..., minimum: Optional[_builtins.float] = ..., nullable: Optional[_builtins.bool] = ..., prefix_items: Optional[_builtins.str] = ..., properties: Optional[_builtins.str] = ..., ref: Optional[_builtins.str] = ..., requireds: Optional[Sequence[_builtins.str]] = ..., title: Optional[_builtins.str] = ..., unique_items: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def defs(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enums(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxItems")
    def max_items(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minItems")
    def min_items(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixItems")
    def prefix_items(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requireds(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueItems")
    def unique_items(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ToolClientFunctionResponse(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, type: _builtins.str, additional_properties: Optional[_builtins.str] = ..., any_of: Optional[_builtins.str] = ..., default: Optional[_builtins.str] = ..., defs: Optional[_builtins.str] = ..., description: Optional[_builtins.str] = ..., enums: Optional[Sequence[_builtins.str]] = ..., items: Optional[_builtins.str] = ..., max_items: Optional[_builtins.int] = ..., maximum: Optional[_builtins.float] = ..., min_items: Optional[_builtins.int] = ..., minimum: Optional[_builtins.float] = ..., nullable: Optional[_builtins.bool] = ..., prefix_items: Optional[_builtins.str] = ..., properties: Optional[_builtins.str] = ..., ref: Optional[_builtins.str] = ..., requireds: Optional[Sequence[_builtins.str]] = ..., title: Optional[_builtins.str] = ..., unique_items: Optional[_builtins.bool] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def defs(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def enums(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxItems")
    def max_items(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="minItems")
    def min_items(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prefixItems")
    def prefix_items(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def requireds(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="uniqueItems")
    def unique_items(self) -> Optional[_builtins.bool]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreTool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, boost_specs: Optional[Sequence[outputs.ToolDataStoreToolBoostSpec]] = ..., description: Optional[_builtins.str] = ..., engine_source: Optional[outputs.ToolDataStoreToolEngineSource] = ..., max_results: Optional[_builtins.int] = ..., modality_configs: Optional[Sequence[outputs.ToolDataStoreToolModalityConfig]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boostSpecs")
    def boost_specs(self) -> Optional[Sequence[outputs.ToolDataStoreToolBoostSpec]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="engineSource")
    def engine_source(self) -> Optional[outputs.ToolDataStoreToolEngineSource]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="maxResults")
    def max_results(self) -> Optional[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modalityConfigs")
    def modality_configs(self) -> Optional[Sequence[outputs.ToolDataStoreToolModalityConfig]]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreToolBoostSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_stores: Sequence[_builtins.str], specs: Sequence[outputs.ToolDataStoreToolBoostSpecSpec]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStores")
    def data_stores(self) -> Sequence[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def specs(self) -> Sequence[outputs.ToolDataStoreToolBoostSpecSpec]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreToolBoostSpecSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, condition_boost_specs: Sequence[outputs.ToolDataStoreToolBoostSpecSpecConditionBoostSpec]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="conditionBoostSpecs")
    def condition_boost_specs(self) -> Sequence[outputs.ToolDataStoreToolBoostSpecSpecConditionBoostSpec]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreToolBoostSpecSpecConditionBoostSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, condition: _builtins.str, boost: Optional[_builtins.float] = ..., boost_control_spec: Optional[outputs.ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpec] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def condition(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def boost(self) -> Optional[_builtins.float]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boostControlSpec")
    def boost_control_spec(self) -> Optional[outputs.ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpec]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpec(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attribute_type: Optional[_builtins.str] = ..., control_points: Optional[Sequence[outputs.ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPoint]] = ..., field_name: Optional[_builtins.str] = ..., interpolation_type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeType")
    def attribute_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="controlPoints")
    def control_points(self) -> Optional[Sequence[outputs.ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPoint]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="fieldName")
    def field_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="interpolationType")
    def interpolation_type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPoint(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, attribute_value: Optional[_builtins.str] = ..., boost_amount: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="attributeValue")
    def attribute_value(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="boostAmount")
    def boost_amount(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreToolEngineSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, engine: _builtins.str, data_store_sources: Optional[Sequence[outputs.ToolDataStoreToolEngineSourceDataStoreSource]] = ..., filter: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def engine(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStoreSources")
    def data_store_sources(self) -> Optional[Sequence[outputs.ToolDataStoreToolEngineSourceDataStoreSource]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreToolEngineSourceDataStoreSource(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, data_store: Optional[outputs.ToolDataStoreToolEngineSourceDataStoreSourceDataStore] = ..., filter: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(self) -> Optional[outputs.ToolDataStoreToolEngineSourceDataStoreSourceDataStore]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreToolEngineSourceDataStoreSourceDataStore(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, connector_configs: Optional[Sequence[outputs.ToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfig]] = ..., create_time: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ..., document_processing_mode: Optional[_builtins.str] = ..., type: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="connectorConfigs")
    def connector_configs(self) -> Optional[Sequence[outputs.ToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="documentProcessingMode")
    def document_processing_mode(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, collection: Optional[_builtins.str] = ..., collection_display_name: Optional[_builtins.str] = ..., data_source: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def collection(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collectionDisplayName")
    def collection_display_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreToolModalityConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, modality_type: _builtins.str, grounding_config: Optional[outputs.ToolDataStoreToolModalityConfigGroundingConfig] = ..., rewriter_config: Optional[outputs.ToolDataStoreToolModalityConfigRewriterConfig] = ..., summarization_config: Optional[outputs.ToolDataStoreToolModalityConfigSummarizationConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modalityType")
    def modality_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groundingConfig")
    def grounding_config(self) -> Optional[outputs.ToolDataStoreToolModalityConfigGroundingConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="rewriterConfig")
    def rewriter_config(self) -> Optional[outputs.ToolDataStoreToolModalityConfigRewriterConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="summarizationConfig")
    def summarization_config(self) -> Optional[outputs.ToolDataStoreToolModalityConfigSummarizationConfig]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreToolModalityConfigGroundingConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disabled: Optional[_builtins.bool] = ..., grounding_level: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="groundingLevel")
    def grounding_level(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreToolModalityConfigRewriterConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, model_settings: outputs.ToolDataStoreToolModalityConfigRewriterConfigModelSettings, disabled: Optional[_builtins.bool] = ..., prompt: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(self) -> outputs.ToolDataStoreToolModalityConfigRewriterConfigModelSettings:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreToolModalityConfigRewriterConfigModelSettings(dict):
    def __init__(__self__, *, model: Optional[_builtins.str] = ..., temperature: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreToolModalityConfigSummarizationConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, disabled: Optional[_builtins.bool] = ..., model_settings: Optional[outputs.ToolDataStoreToolModalityConfigSummarizationConfigModelSettings] = ..., prompt: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(self) -> Optional[outputs.ToolDataStoreToolModalityConfigSummarizationConfigModelSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolDataStoreToolModalityConfigSummarizationConfigModelSettings(dict):
    def __init__(__self__, *, model: Optional[_builtins.str] = ..., temperature: Optional[_builtins.float] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[_builtins.float]:
        
        ...
    


@pulumi.output_type
class ToolGoogleSearchTool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, name: _builtins.str, context_urls: Optional[Sequence[_builtins.str]] = ..., description: Optional[_builtins.str] = ..., exclude_domains: Optional[Sequence[_builtins.str]] = ..., preferred_domains: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contextUrls")
    def context_urls(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="excludeDomains")
    def exclude_domains(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preferredDomains")
    def preferred_domains(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ToolOpenApiTool(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_authentications: Optional[Sequence[outputs.ToolOpenApiToolApiAuthentication]] = ..., description: Optional[_builtins.str] = ..., ignore_unknown_fields: Optional[_builtins.bool] = ..., name: Optional[_builtins.str] = ..., open_api_schema: Optional[_builtins.str] = ..., service_directory_configs: Optional[Sequence[outputs.ToolOpenApiToolServiceDirectoryConfig]] = ..., tls_configs: Optional[Sequence[outputs.ToolOpenApiToolTlsConfig]] = ..., url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiAuthentications")
    def api_authentications(self) -> Optional[Sequence[outputs.ToolOpenApiToolApiAuthentication]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreUnknownFields")
    def ignore_unknown_fields(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openApiSchema")
    def open_api_schema(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfigs")
    def service_directory_configs(self) -> Optional[Sequence[outputs.ToolOpenApiToolServiceDirectoryConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsConfigs")
    def tls_configs(self) -> Optional[Sequence[outputs.ToolOpenApiToolTlsConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolOpenApiToolApiAuthentication(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_key_configs: Optional[Sequence[outputs.ToolOpenApiToolApiAuthenticationApiKeyConfig]] = ..., bearer_token_configs: Optional[Sequence[outputs.ToolOpenApiToolApiAuthenticationBearerTokenConfig]] = ..., oauth_configs: Optional[Sequence[outputs.ToolOpenApiToolApiAuthenticationOauthConfig]] = ..., service_account_auth_configs: Optional[Sequence[outputs.ToolOpenApiToolApiAuthenticationServiceAccountAuthConfig]] = ..., service_agent_id_token_auth_configs: Optional[Sequence[outputs.ToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfig]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyConfigs")
    def api_key_configs(self) -> Optional[Sequence[outputs.ToolOpenApiToolApiAuthenticationApiKeyConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bearerTokenConfigs")
    def bearer_token_configs(self) -> Optional[Sequence[outputs.ToolOpenApiToolApiAuthenticationBearerTokenConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthConfigs")
    def oauth_configs(self) -> Optional[Sequence[outputs.ToolOpenApiToolApiAuthenticationOauthConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountAuthConfigs")
    def service_account_auth_configs(self) -> Optional[Sequence[outputs.ToolOpenApiToolApiAuthenticationServiceAccountAuthConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAgentIdTokenAuthConfigs")
    def service_agent_id_token_auth_configs(self) -> Optional[Sequence[outputs.ToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfig]]:
        
        ...
    


@pulumi.output_type
class ToolOpenApiToolApiAuthenticationApiKeyConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_key_secret_version: Optional[_builtins.str] = ..., key_name: Optional[_builtins.str] = ..., request_location: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeySecretVersion")
    def api_key_secret_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestLocation")
    def request_location(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolOpenApiToolApiAuthenticationBearerTokenConfig(dict):
    def __init__(__self__, *, token: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolOpenApiToolApiAuthenticationOauthConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: Optional[_builtins.str] = ..., client_secret_version: Optional[_builtins.str] = ..., oauth_grant_type: Optional[_builtins.str] = ..., scopes: Optional[Sequence[_builtins.str]] = ..., token_endpoint: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretVersion")
    def client_secret_version(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthGrantType")
    def oauth_grant_type(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolOpenApiToolApiAuthenticationServiceAccountAuthConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_account: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfig(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class ToolOpenApiToolServiceDirectoryConfig(dict):
    def __init__(__self__, *, service: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolOpenApiToolTlsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ca_certs: Optional[Sequence[outputs.ToolOpenApiToolTlsConfigCaCert]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(self) -> Optional[Sequence[outputs.ToolOpenApiToolTlsConfigCaCert]]:
        
        ...
    


@pulumi.output_type
class ToolOpenApiToolTlsConfigCaCert(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cert: Optional[_builtins.str] = ..., display_name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolPythonFunction(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ..., python_code: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolSystemTool(dict):
    def __init__(__self__, *, description: Optional[_builtins.str] = ..., name: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolsetMcpToolset(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, server_address: _builtins.str, api_authentication: Optional[outputs.ToolsetMcpToolsetApiAuthentication] = ..., service_directory_config: Optional[outputs.ToolsetMcpToolsetServiceDirectoryConfig] = ..., tls_config: Optional[outputs.ToolsetMcpToolsetTlsConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serverAddress")
    def server_address(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiAuthentication")
    def api_authentication(self) -> Optional[outputs.ToolsetMcpToolsetApiAuthentication]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(self) -> Optional[outputs.ToolsetMcpToolsetServiceDirectoryConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[outputs.ToolsetMcpToolsetTlsConfig]:
        
        ...
    


@pulumi.output_type
class ToolsetMcpToolsetApiAuthentication(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_key_config: Optional[outputs.ToolsetMcpToolsetApiAuthenticationApiKeyConfig] = ..., bearer_token_config: Optional[outputs.ToolsetMcpToolsetApiAuthenticationBearerTokenConfig] = ..., oauth_config: Optional[outputs.ToolsetMcpToolsetApiAuthenticationOauthConfig] = ..., service_account_auth_config: Optional[outputs.ToolsetMcpToolsetApiAuthenticationServiceAccountAuthConfig] = ..., service_agent_id_token_auth_config: Optional[outputs.ToolsetMcpToolsetApiAuthenticationServiceAgentIdTokenAuthConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyConfig")
    def api_key_config(self) -> Optional[outputs.ToolsetMcpToolsetApiAuthenticationApiKeyConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bearerTokenConfig")
    def bearer_token_config(self) -> Optional[outputs.ToolsetMcpToolsetApiAuthenticationBearerTokenConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthConfig")
    def oauth_config(self) -> Optional[outputs.ToolsetMcpToolsetApiAuthenticationOauthConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountAuthConfig")
    def service_account_auth_config(self) -> Optional[outputs.ToolsetMcpToolsetApiAuthenticationServiceAccountAuthConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAgentIdTokenAuthConfig")
    def service_agent_id_token_auth_config(self) -> Optional[outputs.ToolsetMcpToolsetApiAuthenticationServiceAgentIdTokenAuthConfig]:
        
        ...
    


@pulumi.output_type
class ToolsetMcpToolsetApiAuthenticationApiKeyConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_key_secret_version: _builtins.str, key_name: _builtins.str, request_location: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeySecretVersion")
    def api_key_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestLocation")
    def request_location(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ToolsetMcpToolsetApiAuthenticationBearerTokenConfig(dict):
    def __init__(__self__, *, token: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolsetMcpToolsetApiAuthenticationOauthConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, client_secret_version: _builtins.str, oauth_grant_type: _builtins.str, token_endpoint: _builtins.str, scopes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretVersion")
    def client_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthGrantType")
    def oauth_grant_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ToolsetMcpToolsetApiAuthenticationServiceAccountAuthConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_account: _builtins.str, scopes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ToolsetMcpToolsetApiAuthenticationServiceAgentIdTokenAuthConfig(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class ToolsetMcpToolsetServiceDirectoryConfig(dict):
    def __init__(__self__, *, service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ToolsetMcpToolsetTlsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ca_certs: Sequence[outputs.ToolsetMcpToolsetTlsConfigCaCert]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(self) -> Sequence[outputs.ToolsetMcpToolsetTlsConfigCaCert]:
        
        ...
    


@pulumi.output_type
class ToolsetMcpToolsetTlsConfigCaCert(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cert: _builtins.str, display_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cert(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ToolsetOpenApiToolset(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, open_api_schema: _builtins.str, api_authentication: Optional[outputs.ToolsetOpenApiToolsetApiAuthentication] = ..., ignore_unknown_fields: Optional[_builtins.bool] = ..., service_directory_config: Optional[outputs.ToolsetOpenApiToolsetServiceDirectoryConfig] = ..., tls_config: Optional[outputs.ToolsetOpenApiToolsetTlsConfig] = ..., url: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="openApiSchema")
    def open_api_schema(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiAuthentication")
    def api_authentication(self) -> Optional[outputs.ToolsetOpenApiToolsetApiAuthentication]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ignoreUnknownFields")
    def ignore_unknown_fields(self) -> Optional[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(self) -> Optional[outputs.ToolsetOpenApiToolsetServiceDirectoryConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[outputs.ToolsetOpenApiToolsetTlsConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolsetOpenApiToolsetApiAuthentication(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_key_config: Optional[outputs.ToolsetOpenApiToolsetApiAuthenticationApiKeyConfig] = ..., bearer_token_config: Optional[outputs.ToolsetOpenApiToolsetApiAuthenticationBearerTokenConfig] = ..., oauth_config: Optional[outputs.ToolsetOpenApiToolsetApiAuthenticationOauthConfig] = ..., service_account_auth_config: Optional[outputs.ToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfig] = ..., service_agent_id_token_auth_config: Optional[outputs.ToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfig] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeyConfig")
    def api_key_config(self) -> Optional[outputs.ToolsetOpenApiToolsetApiAuthenticationApiKeyConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="bearerTokenConfig")
    def bearer_token_config(self) -> Optional[outputs.ToolsetOpenApiToolsetApiAuthenticationBearerTokenConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthConfig")
    def oauth_config(self) -> Optional[outputs.ToolsetOpenApiToolsetApiAuthenticationOauthConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccountAuthConfig")
    def service_account_auth_config(self) -> Optional[outputs.ToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfig]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAgentIdTokenAuthConfig")
    def service_agent_id_token_auth_config(self) -> Optional[outputs.ToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfig]:
        
        ...
    


@pulumi.output_type
class ToolsetOpenApiToolsetApiAuthenticationApiKeyConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, api_key_secret_version: _builtins.str, key_name: _builtins.str, request_location: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiKeySecretVersion")
    def api_key_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="requestLocation")
    def request_location(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ToolsetOpenApiToolsetApiAuthenticationBearerTokenConfig(dict):
    def __init__(__self__, *, token: Optional[_builtins.str] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[_builtins.str]:
        
        ...
    


@pulumi.output_type
class ToolsetOpenApiToolsetApiAuthenticationOauthConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, client_id: _builtins.str, client_secret_version: _builtins.str, oauth_grant_type: _builtins.str, token_endpoint: _builtins.str, scopes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientSecretVersion")
    def client_secret_version(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="oauthGrantType")
    def oauth_grant_type(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, service_account: _builtins.str, scopes: Optional[Sequence[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def scopes(self) -> Optional[Sequence[_builtins.str]]:
        
        ...
    


@pulumi.output_type
class ToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfig(dict):
    def __init__(__self__) -> None:
        ...
    


@pulumi.output_type
class ToolsetOpenApiToolsetServiceDirectoryConfig(dict):
    def __init__(__self__, *, service: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def service(self) -> _builtins.str:
        
        ...
    


@pulumi.output_type
class ToolsetOpenApiToolsetTlsConfig(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, ca_certs: Sequence[outputs.ToolsetOpenApiToolsetTlsConfigCaCert]) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(self) -> Sequence[outputs.ToolsetOpenApiToolsetTlsConfigCaCert]:
        
        ...
    


@pulumi.output_type
class ToolsetOpenApiToolsetTlsConfigCaCert(dict):
    def __getitem__(self, key: str) -> Any:
        ...
    
    def get(self, key: str, default=...) -> Any:
        ...
    
    def __init__(__self__, *, cert: _builtins.str, display_name: _builtins.str) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def cert(self) -> _builtins.str:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> _builtins.str:
        
        ...
    


