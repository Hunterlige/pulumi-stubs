import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AgentAfterAgentCallbackArgs",
    "AgentAfterAgentCallbackArgsDict",
    "AgentAfterModelCallbackArgs",
    "AgentAfterModelCallbackArgsDict",
    "AgentAfterToolCallbackArgs",
    "AgentAfterToolCallbackArgsDict",
    "AgentBeforeAgentCallbackArgs",
    "AgentBeforeAgentCallbackArgsDict",
    "AgentBeforeModelCallbackArgs",
    "AgentBeforeModelCallbackArgsDict",
    "AgentBeforeToolCallbackArgs",
    "AgentBeforeToolCallbackArgsDict",
    "AgentLlmAgentArgs",
    "AgentLlmAgentArgsDict",
    "AgentModelSettingsArgs",
    "AgentModelSettingsArgsDict",
    "AgentRemoteDialogflowAgentArgs",
    "AgentRemoteDialogflowAgentArgsDict",
    "AgentToolsetArgs",
    "AgentToolsetArgsDict",
    "AppAudioProcessingConfigArgs",
    "AppAudioProcessingConfigArgsDict",
    "AppAudioProcessingConfigAmbientSoundConfigArgs",
    "AppAudioProcessingConfigAmbientSoundConfigArgsDict",
    "AppAudioProcessingConfigBargeInConfigArgs",
    "AppAudioProcessingConfigBargeInConfigArgsDict",
    "AppAudioProcessingConfigSynthesizeSpeechConfigArgs",
    ...,
    "AppClientCertificateSettingsArgs",
    "AppClientCertificateSettingsArgsDict",
    "AppDataStoreSettingsArgs",
    "AppDataStoreSettingsArgsDict",
    "AppDataStoreSettingsEngineArgs",
    "AppDataStoreSettingsEngineArgsDict",
    "AppDefaultChannelProfileArgs",
    "AppDefaultChannelProfileArgsDict",
    "AppDefaultChannelProfilePersonaPropertyArgs",
    "AppDefaultChannelProfilePersonaPropertyArgsDict",
    "AppDefaultChannelProfileWebWidgetConfigArgs",
    "AppDefaultChannelProfileWebWidgetConfigArgsDict",
    "AppEvaluationMetricsThresholdsArgs",
    "AppEvaluationMetricsThresholdsArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AppLanguageSettingsArgs",
    "AppLanguageSettingsArgsDict",
    "AppLoggingSettingsArgs",
    "AppLoggingSettingsArgsDict",
    "AppLoggingSettingsAudioRecordingConfigArgs",
    "AppLoggingSettingsAudioRecordingConfigArgsDict",
    "AppLoggingSettingsBigqueryExportSettingsArgs",
    "AppLoggingSettingsBigqueryExportSettingsArgsDict",
    "AppLoggingSettingsCloudLoggingSettingsArgs",
    "AppLoggingSettingsCloudLoggingSettingsArgsDict",
    "AppLoggingSettingsConversationLoggingSettingsArgs",
    ...,
    "AppLoggingSettingsRedactionConfigArgs",
    "AppLoggingSettingsRedactionConfigArgsDict",
    "AppModelSettingsArgs",
    "AppModelSettingsArgsDict",
    "AppTimeZoneSettingsArgs",
    "AppTimeZoneSettingsArgsDict",
    "AppVariableDeclarationArgs",
    "AppVariableDeclarationArgsDict",
    "AppVariableDeclarationSchemaArgs",
    "AppVariableDeclarationSchemaArgsDict",
    "AppVersionSnapshotArgs",
    "AppVersionSnapshotArgsDict",
    "AppVersionSnapshotAgentArgs",
    "AppVersionSnapshotAgentArgsDict",
    "AppVersionSnapshotAgentAfterAgentCallbackArgs",
    "AppVersionSnapshotAgentAfterAgentCallbackArgsDict",
    "AppVersionSnapshotAgentAfterModelCallbackArgs",
    "AppVersionSnapshotAgentAfterModelCallbackArgsDict",
    "AppVersionSnapshotAgentAfterToolCallbackArgs",
    "AppVersionSnapshotAgentAfterToolCallbackArgsDict",
    "AppVersionSnapshotAgentBeforeAgentCallbackArgs",
    "AppVersionSnapshotAgentBeforeAgentCallbackArgsDict",
    "AppVersionSnapshotAgentBeforeModelCallbackArgs",
    "AppVersionSnapshotAgentBeforeModelCallbackArgsDict",
    "AppVersionSnapshotAgentBeforeToolCallbackArgs",
    "AppVersionSnapshotAgentBeforeToolCallbackArgsDict",
    "AppVersionSnapshotAgentLlmAgentArgs",
    "AppVersionSnapshotAgentLlmAgentArgsDict",
    "AppVersionSnapshotAgentModelSettingArgs",
    "AppVersionSnapshotAgentModelSettingArgsDict",
    "AppVersionSnapshotAgentRemoteDialogflowAgentArgs",
    ...,
    "AppVersionSnapshotAgentToolsetArgs",
    "AppVersionSnapshotAgentToolsetArgsDict",
    "AppVersionSnapshotAppArgs",
    "AppVersionSnapshotAppArgsDict",
    "AppVersionSnapshotAppAudioProcessingConfigArgs",
    "AppVersionSnapshotAppAudioProcessingConfigArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AppVersionSnapshotAppClientCertificateSettingArgs",
    ...,
    "AppVersionSnapshotAppDataStoreSettingArgs",
    "AppVersionSnapshotAppDataStoreSettingArgsDict",
    "AppVersionSnapshotAppDataStoreSettingEngineArgs",
    ...,
    "AppVersionSnapshotAppDefaultChannelProfileArgs",
    "AppVersionSnapshotAppDefaultChannelProfileArgsDict",
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
    "AppVersionSnapshotAppLanguageSettingArgs",
    "AppVersionSnapshotAppLanguageSettingArgsDict",
    "AppVersionSnapshotAppLoggingSettingArgs",
    "AppVersionSnapshotAppLoggingSettingArgsDict",
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
    "AppVersionSnapshotAppModelSettingArgs",
    "AppVersionSnapshotAppModelSettingArgsDict",
    "AppVersionSnapshotAppTimeZoneSettingArgs",
    "AppVersionSnapshotAppTimeZoneSettingArgsDict",
    "AppVersionSnapshotAppVariableDeclarationArgs",
    "AppVersionSnapshotAppVariableDeclarationArgsDict",
    "AppVersionSnapshotAppVariableDeclarationSchemaArgs",
    ...,
    "AppVersionSnapshotExampleArgs",
    "AppVersionSnapshotExampleArgsDict",
    "AppVersionSnapshotExampleMessageArgs",
    "AppVersionSnapshotExampleMessageArgsDict",
    "AppVersionSnapshotExampleMessageChunkArgs",
    "AppVersionSnapshotExampleMessageChunkArgsDict",
    ...,
    ...,
    "AppVersionSnapshotExampleMessageChunkImageArgs",
    "AppVersionSnapshotExampleMessageChunkImageArgsDict",
    "AppVersionSnapshotExampleMessageChunkToolCallArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AppVersionSnapshotGuardrailArgs",
    "AppVersionSnapshotGuardrailArgsDict",
    "AppVersionSnapshotGuardrailActionArgs",
    "AppVersionSnapshotGuardrailActionArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AppVersionSnapshotGuardrailActionTransferAgentArgs",
    ...,
    "AppVersionSnapshotGuardrailCodeCallbackArgs",
    "AppVersionSnapshotGuardrailCodeCallbackArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AppVersionSnapshotGuardrailContentFilterArgs",
    "AppVersionSnapshotGuardrailContentFilterArgsDict",
    "AppVersionSnapshotGuardrailLlmPolicyArgs",
    "AppVersionSnapshotGuardrailLlmPolicyArgsDict",
    ...,
    ...,
    "AppVersionSnapshotGuardrailLlmPromptSecurityArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "AppVersionSnapshotGuardrailModelSafetyArgs",
    "AppVersionSnapshotGuardrailModelSafetyArgsDict",
    ...,
    ...,
    "AppVersionSnapshotToolArgs",
    "AppVersionSnapshotToolArgsDict",
    "AppVersionSnapshotToolClientFunctionArgs",
    "AppVersionSnapshotToolClientFunctionArgsDict",
    "AppVersionSnapshotToolClientFunctionParameterArgs",
    ...,
    "AppVersionSnapshotToolClientFunctionResponseArgs",
    ...,
    "AppVersionSnapshotToolDataStoreToolArgs",
    "AppVersionSnapshotToolDataStoreToolArgsDict",
    "AppVersionSnapshotToolDataStoreToolBoostSpecArgs",
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
    "AppVersionSnapshotToolGoogleSearchToolArgs",
    "AppVersionSnapshotToolGoogleSearchToolArgsDict",
    "AppVersionSnapshotToolOpenApiToolArgs",
    "AppVersionSnapshotToolOpenApiToolArgsDict",
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
    "AppVersionSnapshotToolOpenApiToolTlsConfigArgs",
    "AppVersionSnapshotToolOpenApiToolTlsConfigArgsDict",
    ...,
    ...,
    "AppVersionSnapshotToolPythonFunctionArgs",
    "AppVersionSnapshotToolPythonFunctionArgsDict",
    "AppVersionSnapshotToolSystemToolArgs",
    "AppVersionSnapshotToolSystemToolArgsDict",
    "AppVersionSnapshotToolsetArgs",
    "AppVersionSnapshotToolsetArgsDict",
    "AppVersionSnapshotToolsetOpenApiToolsetArgs",
    "AppVersionSnapshotToolsetOpenApiToolsetArgsDict",
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
    "DeploymentChannelProfileArgs",
    "DeploymentChannelProfileArgsDict",
    "DeploymentChannelProfilePersonaPropertyArgs",
    "DeploymentChannelProfilePersonaPropertyArgsDict",
    "DeploymentChannelProfileWebWidgetConfigArgs",
    "DeploymentChannelProfileWebWidgetConfigArgsDict",
    "ExampleMessageArgs",
    "ExampleMessageArgsDict",
    "ExampleMessageChunkArgs",
    "ExampleMessageChunkArgsDict",
    "ExampleMessageChunkAgentTransferArgs",
    "ExampleMessageChunkAgentTransferArgsDict",
    "ExampleMessageChunkImageArgs",
    "ExampleMessageChunkImageArgsDict",
    "ExampleMessageChunkToolCallArgs",
    "ExampleMessageChunkToolCallArgsDict",
    "ExampleMessageChunkToolCallToolsetToolArgs",
    "ExampleMessageChunkToolCallToolsetToolArgsDict",
    "ExampleMessageChunkToolResponseArgs",
    "ExampleMessageChunkToolResponseArgsDict",
    "ExampleMessageChunkToolResponseToolsetToolArgs",
    "ExampleMessageChunkToolResponseToolsetToolArgsDict",
    "GuardrailActionArgs",
    "GuardrailActionArgsDict",
    "GuardrailActionGenerativeAnswerArgs",
    "GuardrailActionGenerativeAnswerArgsDict",
    "GuardrailActionRespondImmediatelyArgs",
    "GuardrailActionRespondImmediatelyArgsDict",
    "GuardrailActionRespondImmediatelyResponseArgs",
    "GuardrailActionRespondImmediatelyResponseArgsDict",
    "GuardrailActionTransferAgentArgs",
    "GuardrailActionTransferAgentArgsDict",
    "GuardrailCodeCallbackArgs",
    "GuardrailCodeCallbackArgsDict",
    "GuardrailCodeCallbackAfterAgentCallbackArgs",
    "GuardrailCodeCallbackAfterAgentCallbackArgsDict",
    "GuardrailCodeCallbackAfterModelCallbackArgs",
    "GuardrailCodeCallbackAfterModelCallbackArgsDict",
    "GuardrailCodeCallbackBeforeAgentCallbackArgs",
    "GuardrailCodeCallbackBeforeAgentCallbackArgsDict",
    "GuardrailCodeCallbackBeforeModelCallbackArgs",
    "GuardrailCodeCallbackBeforeModelCallbackArgsDict",
    "GuardrailContentFilterArgs",
    "GuardrailContentFilterArgsDict",
    "GuardrailLlmPolicyArgs",
    "GuardrailLlmPolicyArgsDict",
    "GuardrailLlmPolicyModelSettingsArgs",
    "GuardrailLlmPolicyModelSettingsArgsDict",
    "GuardrailLlmPromptSecurityArgs",
    "GuardrailLlmPromptSecurityArgsDict",
    "GuardrailLlmPromptSecurityCustomPolicyArgs",
    "GuardrailLlmPromptSecurityCustomPolicyArgsDict",
    ...,
    ...,
    "GuardrailLlmPromptSecurityDefaultSettingsArgs",
    "GuardrailLlmPromptSecurityDefaultSettingsArgsDict",
    "GuardrailModelSafetyArgs",
    "GuardrailModelSafetyArgsDict",
    "GuardrailModelSafetySafetySettingArgs",
    "GuardrailModelSafetySafetySettingArgsDict",
    "ToolClientFunctionArgs",
    "ToolClientFunctionArgsDict",
    "ToolClientFunctionParametersArgs",
    "ToolClientFunctionParametersArgsDict",
    "ToolClientFunctionResponseArgs",
    "ToolClientFunctionResponseArgsDict",
    "ToolDataStoreToolArgs",
    "ToolDataStoreToolArgsDict",
    "ToolDataStoreToolBoostSpecArgs",
    "ToolDataStoreToolBoostSpecArgsDict",
    "ToolDataStoreToolBoostSpecSpecArgs",
    "ToolDataStoreToolBoostSpecSpecArgsDict",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ToolDataStoreToolEngineSourceArgs",
    "ToolDataStoreToolEngineSourceArgsDict",
    "ToolDataStoreToolEngineSourceDataStoreSourceArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "ToolDataStoreToolModalityConfigArgs",
    "ToolDataStoreToolModalityConfigArgsDict",
    "ToolDataStoreToolModalityConfigGroundingConfigArgs",
    ...,
    "ToolDataStoreToolModalityConfigRewriterConfigArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "ToolGoogleSearchToolArgs",
    "ToolGoogleSearchToolArgsDict",
    "ToolOpenApiToolArgs",
    "ToolOpenApiToolArgsDict",
    "ToolOpenApiToolApiAuthenticationArgs",
    "ToolOpenApiToolApiAuthenticationArgsDict",
    "ToolOpenApiToolApiAuthenticationApiKeyConfigArgs",
    ...,
    ...,
    ...,
    "ToolOpenApiToolApiAuthenticationOauthConfigArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "ToolOpenApiToolServiceDirectoryConfigArgs",
    "ToolOpenApiToolServiceDirectoryConfigArgsDict",
    "ToolOpenApiToolTlsConfigArgs",
    "ToolOpenApiToolTlsConfigArgsDict",
    "ToolOpenApiToolTlsConfigCaCertArgs",
    "ToolOpenApiToolTlsConfigCaCertArgsDict",
    "ToolPythonFunctionArgs",
    "ToolPythonFunctionArgsDict",
    "ToolSystemToolArgs",
    "ToolSystemToolArgsDict",
    "ToolsetMcpToolsetArgs",
    "ToolsetMcpToolsetArgsDict",
    "ToolsetMcpToolsetApiAuthenticationArgs",
    "ToolsetMcpToolsetApiAuthenticationArgsDict",
    "ToolsetMcpToolsetApiAuthenticationApiKeyConfigArgs",
    ...,
    ...,
    ...,
    "ToolsetMcpToolsetApiAuthenticationOauthConfigArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "ToolsetMcpToolsetServiceDirectoryConfigArgs",
    "ToolsetMcpToolsetServiceDirectoryConfigArgsDict",
    "ToolsetMcpToolsetTlsConfigArgs",
    "ToolsetMcpToolsetTlsConfigArgsDict",
    "ToolsetMcpToolsetTlsConfigCaCertArgs",
    "ToolsetMcpToolsetTlsConfigCaCertArgsDict",
    "ToolsetOpenApiToolsetArgs",
    "ToolsetOpenApiToolsetArgsDict",
    "ToolsetOpenApiToolsetApiAuthenticationArgs",
    "ToolsetOpenApiToolsetApiAuthenticationArgsDict",
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
    "ToolsetOpenApiToolsetServiceDirectoryConfigArgs",
    ...,
    "ToolsetOpenApiToolsetTlsConfigArgs",
    "ToolsetOpenApiToolsetTlsConfigArgsDict",
    "ToolsetOpenApiToolsetTlsConfigCaCertArgs",
    "ToolsetOpenApiToolsetTlsConfigCaCertArgsDict",
]

class AgentAfterAgentCallbackArgsDict(TypedDict):
    python_code: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AgentAfterAgentCallbackArgs:
    def __init__(
        __self__,
        *,
        python_code: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> pulumi.Input[_builtins.str]: ...
    @python_code.setter
    def python_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentAfterModelCallbackArgsDict(TypedDict):
    python_code: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AgentAfterModelCallbackArgs:
    def __init__(
        __self__,
        *,
        python_code: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> pulumi.Input[_builtins.str]: ...
    @python_code.setter
    def python_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentAfterToolCallbackArgsDict(TypedDict):
    python_code: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AgentAfterToolCallbackArgs:
    def __init__(
        __self__,
        *,
        python_code: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> pulumi.Input[_builtins.str]: ...
    @python_code.setter
    def python_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentBeforeAgentCallbackArgsDict(TypedDict):
    python_code: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AgentBeforeAgentCallbackArgs:
    def __init__(
        __self__,
        *,
        python_code: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> pulumi.Input[_builtins.str]: ...
    @python_code.setter
    def python_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentBeforeModelCallbackArgsDict(TypedDict):
    python_code: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AgentBeforeModelCallbackArgs:
    def __init__(
        __self__,
        *,
        python_code: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> pulumi.Input[_builtins.str]: ...
    @python_code.setter
    def python_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentBeforeToolCallbackArgsDict(TypedDict):
    python_code: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AgentBeforeToolCallbackArgs:
    def __init__(
        __self__,
        *,
        python_code: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> pulumi.Input[_builtins.str]: ...
    @python_code.setter
    def python_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AgentLlmAgentArgsDict(TypedDict): ...

@pulumi.input_type
class AgentLlmAgentArgs:
    def __init__(__self__) -> None: ...

class AgentModelSettingsArgsDict(TypedDict):
    model: NotRequired[pulumi.Input[_builtins.str]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class AgentModelSettingsArgs:
    def __init__(
        __self__,
        *,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        temperature: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AgentRemoteDialogflowAgentArgsDict(TypedDict):
    agent: pulumi.Input[_builtins.str]
    flow_id: pulumi.Input[_builtins.str]
    environment_id: NotRequired[pulumi.Input[_builtins.str]]
    input_variable_mapping: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    output_variable_mapping: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class AgentRemoteDialogflowAgentArgs:
    def __init__(
        __self__,
        *,
        agent: pulumi.Input[_builtins.str],
        flow_id: pulumi.Input[_builtins.str],
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        input_variable_mapping: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        output_variable_mapping: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def agent(self) -> pulumi.Input[_builtins.str]: ...
    @agent.setter
    def agent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="flowId")
    def flow_id(self) -> pulumi.Input[_builtins.str]: ...
    @flow_id.setter
    def flow_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputVariableMapping")
    def input_variable_mapping(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @input_variable_mapping.setter
    def input_variable_mapping(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputVariableMapping")
    def output_variable_mapping(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @output_variable_mapping.setter
    def output_variable_mapping(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class AgentToolsetArgsDict(TypedDict):
    toolset: pulumi.Input[_builtins.str]
    tool_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class AgentToolsetArgs:
    def __init__(
        __self__,
        *,
        toolset: pulumi.Input[_builtins.str],
        tool_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def toolset(self) -> pulumi.Input[_builtins.str]: ...
    @toolset.setter
    def toolset(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="toolIds")
    def tool_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tool_ids.setter
    def tool_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AppAudioProcessingConfigArgsDict(TypedDict):
    ambient_sound_config: NotRequired[
        pulumi.Input[AppAudioProcessingConfigAmbientSoundConfigArgsDict]
    ]
    barge_in_config: NotRequired[
        pulumi.Input[AppAudioProcessingConfigBargeInConfigArgsDict]
    ]
    inactivity_timeout: NotRequired[pulumi.Input[_builtins.str]]
    synthesize_speech_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppAudioProcessingConfigSynthesizeSpeechConfigArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppAudioProcessingConfigArgs:
    def __init__(
        __self__,
        *,
        ambient_sound_config: Optional[
            pulumi.Input[AppAudioProcessingConfigAmbientSoundConfigArgs]
        ] = ...,
        barge_in_config: Optional[
            pulumi.Input[AppAudioProcessingConfigBargeInConfigArgs]
        ] = ...,
        inactivity_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        synthesize_speech_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppAudioProcessingConfigSynthesizeSpeechConfigArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ambientSoundConfig")
    def ambient_sound_config(
        self,
    ) -> Optional[pulumi.Input[AppAudioProcessingConfigAmbientSoundConfigArgs]]: ...
    @ambient_sound_config.setter
    def ambient_sound_config(
        self,
        value: Optional[pulumi.Input[AppAudioProcessingConfigAmbientSoundConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bargeInConfig")
    def barge_in_config(
        self,
    ) -> Optional[pulumi.Input[AppAudioProcessingConfigBargeInConfigArgs]]: ...
    @barge_in_config.setter
    def barge_in_config(
        self, value: Optional[pulumi.Input[AppAudioProcessingConfigBargeInConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="inactivityTimeout")
    def inactivity_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inactivity_timeout.setter
    def inactivity_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="synthesizeSpeechConfigs")
    def synthesize_speech_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppAudioProcessingConfigSynthesizeSpeechConfigArgs]]
        ]
    ]: ...
    @synthesize_speech_configs.setter
    def synthesize_speech_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppAudioProcessingConfigSynthesizeSpeechConfigArgs]
                ]
            ]
        ],
    ): ...

class AppAudioProcessingConfigAmbientSoundConfigArgsDict(TypedDict):
    gcs_uri: NotRequired[pulumi.Input[_builtins.str]]
    prebuilt_ambient_sound: NotRequired[pulumi.Input[_builtins.str]]
    volume_gain_db: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class AppAudioProcessingConfigAmbientSoundConfigArgs:
    def __init__(
        __self__,
        *,
        gcs_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        prebuilt_ambient_sound: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_gain_db: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcsUri")
    def gcs_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcs_uri.setter
    def gcs_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="prebuiltAmbientSound")
    def prebuilt_ambient_sound(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prebuilt_ambient_sound.setter
    def prebuilt_ambient_sound(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeGainDb")
    def volume_gain_db(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @volume_gain_db.setter
    def volume_gain_db(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AppAudioProcessingConfigBargeInConfigArgsDict(TypedDict):
    barge_in_awareness: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AppAudioProcessingConfigBargeInConfigArgs:
    def __init__(
        __self__, *, barge_in_awareness: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bargeInAwareness")
    def barge_in_awareness(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @barge_in_awareness.setter
    def barge_in_awareness(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AppAudioProcessingConfigSynthesizeSpeechConfigArgsDict(TypedDict):
    language_code: pulumi.Input[_builtins.str]
    speaking_rate: NotRequired[pulumi.Input[_builtins.float]]
    voice: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppAudioProcessingConfigSynthesizeSpeechConfigArgs:
    def __init__(
        __self__,
        *,
        language_code: pulumi.Input[_builtins.str],
        speaking_rate: Optional[pulumi.Input[_builtins.float]] = ...,
        voice: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Input[_builtins.str]: ...
    @language_code.setter
    def language_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="speakingRate")
    def speaking_rate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @speaking_rate.setter
    def speaking_rate(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def voice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @voice.setter
    def voice(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppClientCertificateSettingsArgsDict(TypedDict):
    private_key: pulumi.Input[_builtins.str]
    tls_certificate: pulumi.Input[_builtins.str]
    passphrase: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppClientCertificateSettingsArgs:
    def __init__(
        __self__,
        *,
        private_key: pulumi.Input[_builtins.str],
        tls_certificate: pulumi.Input[_builtins.str],
        passphrase: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> pulumi.Input[_builtins.str]: ...
    @private_key.setter
    def private_key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tlsCertificate")
    def tls_certificate(self) -> pulumi.Input[_builtins.str]: ...
    @tls_certificate.setter
    def tls_certificate(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @passphrase.setter
    def passphrase(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppDataStoreSettingsArgsDict(TypedDict):
    engines: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AppDataStoreSettingsEngineArgsDict]]]
    ]
    ...

@pulumi.input_type
class AppDataStoreSettingsArgs:
    def __init__(
        __self__,
        *,
        engines: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppDataStoreSettingsEngineArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def engines(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppDataStoreSettingsEngineArgs]]]
    ]: ...
    @engines.setter
    def engines(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppDataStoreSettingsEngineArgs]]]
        ],
    ): ...

class AppDataStoreSettingsEngineArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppDataStoreSettingsEngineArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppDefaultChannelProfileArgsDict(TypedDict):
    channel_type: NotRequired[pulumi.Input[_builtins.str]]
    disable_barge_in_control: NotRequired[pulumi.Input[_builtins.bool]]
    disable_dtmf: NotRequired[pulumi.Input[_builtins.bool]]
    persona_property: NotRequired[
        pulumi.Input[AppDefaultChannelProfilePersonaPropertyArgsDict]
    ]
    profile_id: NotRequired[pulumi.Input[_builtins.str]]
    web_widget_config: NotRequired[
        pulumi.Input[AppDefaultChannelProfileWebWidgetConfigArgsDict]
    ]
    ...

@pulumi.input_type
class AppDefaultChannelProfileArgs:
    def __init__(
        __self__,
        *,
        channel_type: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_barge_in_control: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_dtmf: Optional[pulumi.Input[_builtins.bool]] = ...,
        persona_property: Optional[
            pulumi.Input[AppDefaultChannelProfilePersonaPropertyArgs]
        ] = ...,
        profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        web_widget_config: Optional[
            pulumi.Input[AppDefaultChannelProfileWebWidgetConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @channel_type.setter
    def channel_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableBargeInControl")
    def disable_barge_in_control(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_barge_in_control.setter
    def disable_barge_in_control(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableDtmf")
    def disable_dtmf(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_dtmf.setter
    def disable_dtmf(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="personaProperty")
    def persona_property(
        self,
    ) -> Optional[pulumi.Input[AppDefaultChannelProfilePersonaPropertyArgs]]: ...
    @persona_property.setter
    def persona_property(
        self, value: Optional[pulumi.Input[AppDefaultChannelProfilePersonaPropertyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile_id.setter
    def profile_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webWidgetConfig")
    def web_widget_config(
        self,
    ) -> Optional[pulumi.Input[AppDefaultChannelProfileWebWidgetConfigArgs]]: ...
    @web_widget_config.setter
    def web_widget_config(
        self, value: Optional[pulumi.Input[AppDefaultChannelProfileWebWidgetConfigArgs]]
    ): ...

class AppDefaultChannelProfilePersonaPropertyArgsDict(TypedDict):
    persona: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppDefaultChannelProfilePersonaPropertyArgs:
    def __init__(
        __self__, *, persona: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def persona(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @persona.setter
    def persona(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppDefaultChannelProfileWebWidgetConfigArgsDict(TypedDict):
    modality: NotRequired[pulumi.Input[_builtins.str]]
    theme: NotRequired[pulumi.Input[_builtins.str]]
    web_widget_title: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppDefaultChannelProfileWebWidgetConfigArgs:
    def __init__(
        __self__,
        *,
        modality: Optional[pulumi.Input[_builtins.str]] = ...,
        theme: Optional[pulumi.Input[_builtins.str]] = ...,
        web_widget_title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def modality(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @modality.setter
    def modality(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def theme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @theme.setter
    def theme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webWidgetTitle")
    def web_widget_title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_widget_title.setter
    def web_widget_title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppEvaluationMetricsThresholdsArgsDict(TypedDict):
    golden_evaluation_metrics_thresholds: NotRequired[
        pulumi.Input[
            AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class AppEvaluationMetricsThresholdsArgs:
    def __init__(
        __self__,
        *,
        golden_evaluation_metrics_thresholds: Optional[
            pulumi.Input[
                AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="goldenEvaluationMetricsThresholds")
    def golden_evaluation_metrics_thresholds(
        self,
    ) -> Optional[
        pulumi.Input[
            AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsArgs
        ]
    ]: ...
    @golden_evaluation_metrics_thresholds.setter
    def golden_evaluation_metrics_thresholds(
        self,
        value: Optional[
            pulumi.Input[
                AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsArgs
            ]
        ],
    ): ...

class AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsArgsDict(
    TypedDict
):
    expectation_level_metrics_thresholds: NotRequired[
        pulumi.Input[
            AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsExpectationLevelMetricsThresholdsArgsDict
        ]
    ]
    turn_level_metrics_thresholds: NotRequired[
        pulumi.Input[
            AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsTurnLevelMetricsThresholdsArgsDict
        ]
    ]
    ...

@pulumi.input_type
class AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsArgs:
    def __init__(
        __self__,
        *,
        expectation_level_metrics_thresholds: Optional[
            pulumi.Input[
                AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsExpectationLevelMetricsThresholdsArgs
            ]
        ] = ...,
        turn_level_metrics_thresholds: Optional[
            pulumi.Input[
                AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsTurnLevelMetricsThresholdsArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="expectationLevelMetricsThresholds")
    def expectation_level_metrics_thresholds(
        self,
    ) -> Optional[
        pulumi.Input[
            AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsExpectationLevelMetricsThresholdsArgs
        ]
    ]: ...
    @expectation_level_metrics_thresholds.setter
    def expectation_level_metrics_thresholds(
        self,
        value: Optional[
            pulumi.Input[
                AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsExpectationLevelMetricsThresholdsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="turnLevelMetricsThresholds")
    def turn_level_metrics_thresholds(
        self,
    ) -> Optional[
        pulumi.Input[
            AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsTurnLevelMetricsThresholdsArgs
        ]
    ]: ...
    @turn_level_metrics_thresholds.setter
    def turn_level_metrics_thresholds(
        self,
        value: Optional[
            pulumi.Input[
                AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsTurnLevelMetricsThresholdsArgs
            ]
        ],
    ): ...

class AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsExpectationLevelMetricsThresholdsArgsDict(
    TypedDict
):
    tool_invocation_parameter_correctness_threshold: NotRequired[
        pulumi.Input[_builtins.float]
    ]
    ...

@pulumi.input_type
class AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsExpectationLevelMetricsThresholdsArgs:
    def __init__(
        __self__,
        *,
        tool_invocation_parameter_correctness_threshold: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="toolInvocationParameterCorrectnessThreshold")
    def tool_invocation_parameter_correctness_threshold(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @tool_invocation_parameter_correctness_threshold.setter
    def tool_invocation_parameter_correctness_threshold(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

class AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsTurnLevelMetricsThresholdsArgsDict(
    TypedDict
):
    overall_tool_invocation_correctness_threshold: NotRequired[
        pulumi.Input[_builtins.float]
    ]
    semantic_similarity_success_threshold: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AppEvaluationMetricsThresholdsGoldenEvaluationMetricsThresholdsTurnLevelMetricsThresholdsArgs:
    def __init__(
        __self__,
        *,
        overall_tool_invocation_correctness_threshold: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        semantic_similarity_success_threshold: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="overallToolInvocationCorrectnessThreshold")
    def overall_tool_invocation_correctness_threshold(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @overall_tool_invocation_correctness_threshold.setter
    def overall_tool_invocation_correctness_threshold(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="semanticSimilaritySuccessThreshold")
    def semantic_similarity_success_threshold(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @semantic_similarity_success_threshold.setter
    def semantic_similarity_success_threshold(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class AppLanguageSettingsArgsDict(TypedDict):
    default_language_code: NotRequired[pulumi.Input[_builtins.str]]
    enable_multilingual_support: NotRequired[pulumi.Input[_builtins.bool]]
    fallback_action: NotRequired[pulumi.Input[_builtins.str]]
    supported_language_codes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class AppLanguageSettingsArgs:
    def __init__(
        __self__,
        *,
        default_language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_multilingual_support: Optional[pulumi.Input[_builtins.bool]] = ...,
        fallback_action: Optional[pulumi.Input[_builtins.str]] = ...,
        supported_language_codes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultLanguageCode")
    def default_language_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_language_code.setter
    def default_language_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableMultilingualSupport")
    def enable_multilingual_support(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_multilingual_support.setter
    def enable_multilingual_support(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fallbackAction")
    def fallback_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fallback_action.setter
    def fallback_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="supportedLanguageCodes")
    def supported_language_codes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @supported_language_codes.setter
    def supported_language_codes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AppLoggingSettingsArgsDict(TypedDict):
    audio_recording_config: NotRequired[
        pulumi.Input[AppLoggingSettingsAudioRecordingConfigArgsDict]
    ]
    bigquery_export_settings: NotRequired[
        pulumi.Input[AppLoggingSettingsBigqueryExportSettingsArgsDict]
    ]
    cloud_logging_settings: NotRequired[
        pulumi.Input[AppLoggingSettingsCloudLoggingSettingsArgsDict]
    ]
    conversation_logging_settings: NotRequired[
        pulumi.Input[AppLoggingSettingsConversationLoggingSettingsArgsDict]
    ]
    redaction_config: NotRequired[
        pulumi.Input[AppLoggingSettingsRedactionConfigArgsDict]
    ]
    ...

@pulumi.input_type
class AppLoggingSettingsArgs:
    def __init__(
        __self__,
        *,
        audio_recording_config: Optional[
            pulumi.Input[AppLoggingSettingsAudioRecordingConfigArgs]
        ] = ...,
        bigquery_export_settings: Optional[
            pulumi.Input[AppLoggingSettingsBigqueryExportSettingsArgs]
        ] = ...,
        cloud_logging_settings: Optional[
            pulumi.Input[AppLoggingSettingsCloudLoggingSettingsArgs]
        ] = ...,
        conversation_logging_settings: Optional[
            pulumi.Input[AppLoggingSettingsConversationLoggingSettingsArgs]
        ] = ...,
        redaction_config: Optional[
            pulumi.Input[AppLoggingSettingsRedactionConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioRecordingConfig")
    def audio_recording_config(
        self,
    ) -> Optional[pulumi.Input[AppLoggingSettingsAudioRecordingConfigArgs]]: ...
    @audio_recording_config.setter
    def audio_recording_config(
        self, value: Optional[pulumi.Input[AppLoggingSettingsAudioRecordingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bigqueryExportSettings")
    def bigquery_export_settings(
        self,
    ) -> Optional[pulumi.Input[AppLoggingSettingsBigqueryExportSettingsArgs]]: ...
    @bigquery_export_settings.setter
    def bigquery_export_settings(
        self,
        value: Optional[pulumi.Input[AppLoggingSettingsBigqueryExportSettingsArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudLoggingSettings")
    def cloud_logging_settings(
        self,
    ) -> Optional[pulumi.Input[AppLoggingSettingsCloudLoggingSettingsArgs]]: ...
    @cloud_logging_settings.setter
    def cloud_logging_settings(
        self, value: Optional[pulumi.Input[AppLoggingSettingsCloudLoggingSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="conversationLoggingSettings")
    def conversation_logging_settings(
        self,
    ) -> Optional[pulumi.Input[AppLoggingSettingsConversationLoggingSettingsArgs]]: ...
    @conversation_logging_settings.setter
    def conversation_logging_settings(
        self,
        value: Optional[
            pulumi.Input[AppLoggingSettingsConversationLoggingSettingsArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="redactionConfig")
    def redaction_config(
        self,
    ) -> Optional[pulumi.Input[AppLoggingSettingsRedactionConfigArgs]]: ...
    @redaction_config.setter
    def redaction_config(
        self, value: Optional[pulumi.Input[AppLoggingSettingsRedactionConfigArgs]]
    ): ...

class AppLoggingSettingsAudioRecordingConfigArgsDict(TypedDict):
    gcs_bucket: NotRequired[pulumi.Input[_builtins.str]]
    gcs_path_prefix: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppLoggingSettingsAudioRecordingConfigArgs:
    def __init__(
        __self__,
        *,
        gcs_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        gcs_path_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcsBucket")
    def gcs_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcs_bucket.setter
    def gcs_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gcsPathPrefix")
    def gcs_path_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcs_path_prefix.setter
    def gcs_path_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppLoggingSettingsBigqueryExportSettingsArgsDict(TypedDict):
    dataset: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    project: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppLoggingSettingsBigqueryExportSettingsArgs:
    def __init__(
        __self__,
        *,
        dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset.setter
    def dataset(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppLoggingSettingsCloudLoggingSettingsArgsDict(TypedDict):
    enable_cloud_logging: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AppLoggingSettingsCloudLoggingSettingsArgs:
    def __init__(
        __self__, *, enable_cloud_logging: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableCloudLogging")
    def enable_cloud_logging(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_cloud_logging.setter
    def enable_cloud_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AppLoggingSettingsConversationLoggingSettingsArgsDict(TypedDict):
    disable_conversation_logging: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AppLoggingSettingsConversationLoggingSettingsArgs:
    def __init__(
        __self__,
        *,
        disable_conversation_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableConversationLogging")
    def disable_conversation_logging(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_conversation_logging.setter
    def disable_conversation_logging(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AppLoggingSettingsRedactionConfigArgsDict(TypedDict):
    deidentify_template: NotRequired[pulumi.Input[_builtins.str]]
    enable_redaction: NotRequired[pulumi.Input[_builtins.bool]]
    inspect_template: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppLoggingSettingsRedactionConfigArgs:
    def __init__(
        __self__,
        *,
        deidentify_template: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_redaction: Optional[pulumi.Input[_builtins.bool]] = ...,
        inspect_template: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deidentifyTemplate")
    def deidentify_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deidentify_template.setter
    def deidentify_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableRedaction")
    def enable_redaction(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_redaction.setter
    def enable_redaction(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="inspectTemplate")
    def inspect_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inspect_template.setter
    def inspect_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppModelSettingsArgsDict(TypedDict):
    model: NotRequired[pulumi.Input[_builtins.str]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class AppModelSettingsArgs:
    def __init__(
        __self__,
        *,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        temperature: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AppTimeZoneSettingsArgsDict(TypedDict):
    time_zone: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppTimeZoneSettingsArgs:
    def __init__(
        __self__, *, time_zone: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVariableDeclarationArgsDict(TypedDict):
    description: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    schema: pulumi.Input[AppVariableDeclarationSchemaArgsDict]
    ...

@pulumi.input_type
class AppVariableDeclarationArgs:
    def __init__(
        __self__,
        *,
        description: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        schema: pulumi.Input[AppVariableDeclarationSchemaArgs],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]: ...
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def schema(self) -> pulumi.Input[AppVariableDeclarationSchemaArgs]: ...
    @schema.setter
    def schema(self, value: pulumi.Input[AppVariableDeclarationSchemaArgs]): ...

class AppVariableDeclarationSchemaArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    additional_properties: NotRequired[pulumi.Input[_builtins.str]]
    any_of: NotRequired[pulumi.Input[_builtins.str]]
    default: NotRequired[pulumi.Input[_builtins.str]]
    defs: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    enums: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    items: NotRequired[pulumi.Input[_builtins.str]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    prefix_items: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[_builtins.str]]
    ref: NotRequired[pulumi.Input[_builtins.str]]
    requireds: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    title: NotRequired[pulumi.Input[_builtins.str]]
    unique_items: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AppVariableDeclarationSchemaArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        additional_properties: Optional[pulumi.Input[_builtins.str]] = ...,
        any_of: Optional[pulumi.Input[_builtins.str]] = ...,
        default: Optional[pulumi.Input[_builtins.str]] = ...,
        defs: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enums: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        items: Optional[pulumi.Input[_builtins.str]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        prefix_items: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[_builtins.str]] = ...,
        ref: Optional[pulumi.Input[_builtins.str]] = ...,
        requireds: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
        unique_items: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_properties.setter
    def additional_properties(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @any_of.setter
    def any_of(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default.setter
    def default(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def defs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @defs.setter
    def defs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enums(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enums.setter
    def enums(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items.setter
    def items(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixItems")
    def prefix_items(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix_items.setter
    def prefix_items(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ref.setter
    def ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def requireds(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @requireds.setter
    def requireds(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="uniqueItems")
    def unique_items(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @unique_items.setter
    def unique_items(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AppVersionSnapshotArgsDict(TypedDict):
    agents: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAgentArgsDict]]]
    ]
    apps: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAppArgsDict]]]
    ]
    examples: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotExampleArgsDict]]]
    ]
    guardrails: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotGuardrailArgsDict]]]
    ]
    tools: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolArgsDict]]]
    ]
    toolsets: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolsetArgsDict]]]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotArgs:
    def __init__(
        __self__,
        *,
        agents: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAgentArgs]]]
        ] = ...,
        apps: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAppArgs]]]
        ] = ...,
        examples: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotExampleArgs]]]
        ] = ...,
        guardrails: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotGuardrailArgs]]]
        ] = ...,
        tools: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolArgs]]]
        ] = ...,
        toolsets: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolsetArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def agents(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAgentArgs]]]
    ]: ...
    @agents.setter
    def agents(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAgentArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def apps(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAppArgs]]]]: ...
    @apps.setter
    def apps(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAppArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def examples(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotExampleArgs]]]
    ]: ...
    @examples.setter
    def examples(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotExampleArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def guardrails(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotGuardrailArgs]]]
    ]: ...
    @guardrails.setter
    def guardrails(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotGuardrailArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolArgs]]]]: ...
    @tools.setter
    def tools(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def toolsets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolsetArgs]]]
    ]: ...
    @toolsets.setter
    def toolsets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolsetArgs]]]
        ],
    ): ...

class AppVersionSnapshotAgentArgsDict(TypedDict):
    after_agent_callbacks: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAgentAfterAgentCallbackArgsDict]]
        ]
    ]
    after_model_callbacks: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAgentAfterModelCallbackArgsDict]]
        ]
    ]
    after_tool_callbacks: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAgentAfterToolCallbackArgsDict]]
        ]
    ]
    before_agent_callbacks: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAgentBeforeAgentCallbackArgsDict]]
        ]
    ]
    before_model_callbacks: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAgentBeforeModelCallbackArgsDict]]
        ]
    ]
    before_tool_callbacks: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAgentBeforeToolCallbackArgsDict]]
        ]
    ]
    child_agents: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    generated_summary: NotRequired[pulumi.Input[_builtins.str]]
    guardrails: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    instruction: NotRequired[pulumi.Input[_builtins.str]]
    llm_agents: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAgentLlmAgentArgsDict]]]
    ]
    model_settings: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAgentModelSettingArgsDict]]
        ]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    remote_dialogflow_agents: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAgentRemoteDialogflowAgentArgsDict]]
        ]
    ]
    tools: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    toolsets: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAgentToolsetArgsDict]]]
    ]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAgentArgs:
    def __init__(
        __self__,
        *,
        after_agent_callbacks: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentAfterAgentCallbackArgs]]
            ]
        ] = ...,
        after_model_callbacks: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentAfterModelCallbackArgs]]
            ]
        ] = ...,
        after_tool_callbacks: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentAfterToolCallbackArgs]]
            ]
        ] = ...,
        before_agent_callbacks: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentBeforeAgentCallbackArgs]]
            ]
        ] = ...,
        before_model_callbacks: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentBeforeModelCallbackArgs]]
            ]
        ] = ...,
        before_tool_callbacks: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentBeforeToolCallbackArgs]]
            ]
        ] = ...,
        child_agents: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        generated_summary: Optional[pulumi.Input[_builtins.str]] = ...,
        guardrails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        instruction: Optional[pulumi.Input[_builtins.str]] = ...,
        llm_agents: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAgentLlmAgentArgs]]]
        ] = ...,
        model_settings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentModelSettingArgs]]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        remote_dialogflow_agents: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentRemoteDialogflowAgentArgs]]
            ]
        ] = ...,
        tools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        toolsets: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAgentToolsetArgs]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="afterAgentCallbacks")
    def after_agent_callbacks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAgentAfterAgentCallbackArgs]]
        ]
    ]: ...
    @after_agent_callbacks.setter
    def after_agent_callbacks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentAfterAgentCallbackArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="afterModelCallbacks")
    def after_model_callbacks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAgentAfterModelCallbackArgs]]
        ]
    ]: ...
    @after_model_callbacks.setter
    def after_model_callbacks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentAfterModelCallbackArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="afterToolCallbacks")
    def after_tool_callbacks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAgentAfterToolCallbackArgs]]
        ]
    ]: ...
    @after_tool_callbacks.setter
    def after_tool_callbacks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentAfterToolCallbackArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="beforeAgentCallbacks")
    def before_agent_callbacks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAgentBeforeAgentCallbackArgs]]
        ]
    ]: ...
    @before_agent_callbacks.setter
    def before_agent_callbacks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentBeforeAgentCallbackArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="beforeModelCallbacks")
    def before_model_callbacks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAgentBeforeModelCallbackArgs]]
        ]
    ]: ...
    @before_model_callbacks.setter
    def before_model_callbacks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentBeforeModelCallbackArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="beforeToolCallbacks")
    def before_tool_callbacks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAgentBeforeToolCallbackArgs]]
        ]
    ]: ...
    @before_tool_callbacks.setter
    def before_tool_callbacks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentBeforeToolCallbackArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="childAgents")
    def child_agents(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @child_agents.setter
    def child_agents(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="generatedSummary")
    def generated_summary(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generated_summary.setter
    def generated_summary(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def guardrails(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @guardrails.setter
    def guardrails(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def instruction(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @instruction.setter
    def instruction(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="llmAgents")
    def llm_agents(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAgentLlmAgentArgs]]]
    ]: ...
    @llm_agents.setter
    def llm_agents(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAgentLlmAgentArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAgentModelSettingArgs]]]
    ]: ...
    @model_settings.setter
    def model_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentModelSettingArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="remoteDialogflowAgents")
    def remote_dialogflow_agents(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAgentRemoteDialogflowAgentArgs]]
        ]
    ]: ...
    @remote_dialogflow_agents.setter
    def remote_dialogflow_agents(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAgentRemoteDialogflowAgentArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tools(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tools.setter
    def tools(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def toolsets(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAgentToolsetArgs]]]
    ]: ...
    @toolsets.setter
    def toolsets(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAgentToolsetArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAgentAfterAgentCallbackArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    python_code: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAgentAfterAgentCallbackArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        python_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @python_code.setter
    def python_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAgentAfterModelCallbackArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    python_code: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAgentAfterModelCallbackArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        python_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @python_code.setter
    def python_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAgentAfterToolCallbackArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    python_code: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAgentAfterToolCallbackArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        python_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @python_code.setter
    def python_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAgentBeforeAgentCallbackArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    python_code: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAgentBeforeAgentCallbackArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        python_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @python_code.setter
    def python_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAgentBeforeModelCallbackArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    python_code: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAgentBeforeModelCallbackArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        python_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @python_code.setter
    def python_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAgentBeforeToolCallbackArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    python_code: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAgentBeforeToolCallbackArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        python_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @python_code.setter
    def python_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAgentLlmAgentArgsDict(TypedDict): ...

@pulumi.input_type
class AppVersionSnapshotAgentLlmAgentArgs:
    def __init__(__self__) -> None: ...

class AppVersionSnapshotAgentModelSettingArgsDict(TypedDict):
    model: NotRequired[pulumi.Input[_builtins.str]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class AppVersionSnapshotAgentModelSettingArgs:
    def __init__(
        __self__,
        *,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        temperature: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AppVersionSnapshotAgentRemoteDialogflowAgentArgsDict(TypedDict):
    agent: NotRequired[pulumi.Input[_builtins.str]]
    environment_id: NotRequired[pulumi.Input[_builtins.str]]
    flow_id: NotRequired[pulumi.Input[_builtins.str]]
    input_variable_mapping: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    output_variable_mapping: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotAgentRemoteDialogflowAgentArgs:
    def __init__(
        __self__,
        *,
        agent: Optional[pulumi.Input[_builtins.str]] = ...,
        environment_id: Optional[pulumi.Input[_builtins.str]] = ...,
        flow_id: Optional[pulumi.Input[_builtins.str]] = ...,
        input_variable_mapping: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        output_variable_mapping: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def agent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent.setter
    def agent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @environment_id.setter
    def environment_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="flowId")
    def flow_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @flow_id.setter
    def flow_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="inputVariableMapping")
    def input_variable_mapping(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @input_variable_mapping.setter
    def input_variable_mapping(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="outputVariableMapping")
    def output_variable_mapping(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @output_variable_mapping.setter
    def output_variable_mapping(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class AppVersionSnapshotAgentToolsetArgsDict(TypedDict):
    tool_ids: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    toolset: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAgentToolsetArgs:
    def __init__(
        __self__,
        *,
        tool_ids: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        toolset: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="toolIds")
    def tool_ids(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tool_ids.setter
    def tool_ids(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def toolset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @toolset.setter
    def toolset(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAppArgsDict(TypedDict):
    audio_processing_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAppAudioProcessingConfigArgsDict]]
        ]
    ]
    client_certificate_settings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotAppClientCertificateSettingArgsDict]
            ]
        ]
    ]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    data_store_settings: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAppDataStoreSettingArgsDict]]
        ]
    ]
    default_channel_profiles: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAppDefaultChannelProfileArgsDict]]
        ]
    ]
    deployment_count: NotRequired[pulumi.Input[_builtins.int]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    evaluation_metrics_thresholds: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotAppEvaluationMetricsThresholdArgsDict]
            ]
        ]
    ]
    global_instruction: NotRequired[pulumi.Input[_builtins.str]]
    guardrails: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    language_settings: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAppLanguageSettingArgsDict]]
        ]
    ]
    logging_settings: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAppLoggingSettingArgsDict]]
        ]
    ]
    metadata: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    model_settings: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAppModelSettingArgsDict]]]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    root_agent: NotRequired[pulumi.Input[_builtins.str]]
    time_zone_settings: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAppTimeZoneSettingArgsDict]]
        ]
    ]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    variable_declarations: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAppVariableDeclarationArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotAppArgs:
    def __init__(
        __self__,
        *,
        audio_processing_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppAudioProcessingConfigArgs]]
            ]
        ] = ...,
        client_certificate_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotAppClientCertificateSettingArgs]
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        data_store_settings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppDataStoreSettingArgs]]
            ]
        ] = ...,
        default_channel_profiles: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppDefaultChannelProfileArgs]]
            ]
        ] = ...,
        deployment_count: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        evaluation_metrics_thresholds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotAppEvaluationMetricsThresholdArgs]
                ]
            ]
        ] = ...,
        global_instruction: Optional[pulumi.Input[_builtins.str]] = ...,
        guardrails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        language_settings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppLanguageSettingArgs]]
            ]
        ] = ...,
        logging_settings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppLoggingSettingArgs]]
            ]
        ] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        model_settings: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAppModelSettingArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        root_agent: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone_settings: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppTimeZoneSettingArgs]]
            ]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        variable_declarations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppVariableDeclarationArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioProcessingConfigs")
    def audio_processing_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAppAudioProcessingConfigArgs]]
        ]
    ]: ...
    @audio_processing_configs.setter
    def audio_processing_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppAudioProcessingConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientCertificateSettings")
    def client_certificate_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAppClientCertificateSettingArgs]]
        ]
    ]: ...
    @client_certificate_settings.setter
    def client_certificate_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotAppClientCertificateSettingArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataStoreSettings")
    def data_store_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAppDataStoreSettingArgs]]]
    ]: ...
    @data_store_settings.setter
    def data_store_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppDataStoreSettingArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultChannelProfiles")
    def default_channel_profiles(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAppDefaultChannelProfileArgs]]
        ]
    ]: ...
    @default_channel_profiles.setter
    def default_channel_profiles(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppDefaultChannelProfileArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="deploymentCount")
    def deployment_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @deployment_count.setter
    def deployment_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="evaluationMetricsThresholds")
    def evaluation_metrics_thresholds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAppEvaluationMetricsThresholdArgs]]
        ]
    ]: ...
    @evaluation_metrics_thresholds.setter
    def evaluation_metrics_thresholds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotAppEvaluationMetricsThresholdArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="globalInstruction")
    def global_instruction(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @global_instruction.setter
    def global_instruction(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def guardrails(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @guardrails.setter
    def guardrails(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="languageSettings")
    def language_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAppLanguageSettingArgs]]]
    ]: ...
    @language_settings.setter
    def language_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppLanguageSettingArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingSettings")
    def logging_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAppLoggingSettingArgs]]]
    ]: ...
    @logging_settings.setter
    def logging_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppLoggingSettingArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def metadata(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @metadata.setter
    def metadata(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAppModelSettingArgs]]]
    ]: ...
    @model_settings.setter
    def model_settings(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAppModelSettingArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootAgent")
    def root_agent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_agent.setter
    def root_agent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZoneSettings")
    def time_zone_settings(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotAppTimeZoneSettingArgs]]]
    ]: ...
    @time_zone_settings.setter
    def time_zone_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppTimeZoneSettingArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="variableDeclarations")
    def variable_declarations(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAppVariableDeclarationArgs]]
        ]
    ]: ...
    @variable_declarations.setter
    def variable_declarations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppVariableDeclarationArgs]]
            ]
        ],
    ): ...

class AppVersionSnapshotAppAudioProcessingConfigArgsDict(TypedDict):
    ambient_sound_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppAudioProcessingConfigAmbientSoundConfigArgsDict
                ]
            ]
        ]
    ]
    barge_in_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppAudioProcessingConfigBargeInConfigArgsDict
                ]
            ]
        ]
    ]
    inactivity_timeout: NotRequired[pulumi.Input[_builtins.str]]
    synthesize_speech_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppAudioProcessingConfigSynthesizeSpeechConfigArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotAppAudioProcessingConfigArgs:
    def __init__(
        __self__,
        *,
        ambient_sound_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppAudioProcessingConfigAmbientSoundConfigArgs
                    ]
                ]
            ]
        ] = ...,
        barge_in_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppAudioProcessingConfigBargeInConfigArgs
                    ]
                ]
            ]
        ] = ...,
        inactivity_timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        synthesize_speech_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppAudioProcessingConfigSynthesizeSpeechConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="ambientSoundConfigs")
    def ambient_sound_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppAudioProcessingConfigAmbientSoundConfigArgs
                ]
            ]
        ]
    ]: ...
    @ambient_sound_configs.setter
    def ambient_sound_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppAudioProcessingConfigAmbientSoundConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bargeInConfigs")
    def barge_in_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppAudioProcessingConfigBargeInConfigArgs
                ]
            ]
        ]
    ]: ...
    @barge_in_configs.setter
    def barge_in_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppAudioProcessingConfigBargeInConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="inactivityTimeout")
    def inactivity_timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inactivity_timeout.setter
    def inactivity_timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="synthesizeSpeechConfigs")
    def synthesize_speech_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppAudioProcessingConfigSynthesizeSpeechConfigArgs
                ]
            ]
        ]
    ]: ...
    @synthesize_speech_configs.setter
    def synthesize_speech_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppAudioProcessingConfigSynthesizeSpeechConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotAppAudioProcessingConfigAmbientSoundConfigArgsDict(TypedDict):
    gcs_uri: NotRequired[pulumi.Input[_builtins.str]]
    prebuilt_ambient_sound: NotRequired[pulumi.Input[_builtins.str]]
    volume_gain_db: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppAudioProcessingConfigAmbientSoundConfigArgs:
    def __init__(
        __self__,
        *,
        gcs_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        prebuilt_ambient_sound: Optional[pulumi.Input[_builtins.str]] = ...,
        volume_gain_db: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcsUri")
    def gcs_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcs_uri.setter
    def gcs_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="prebuiltAmbientSound")
    def prebuilt_ambient_sound(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prebuilt_ambient_sound.setter
    def prebuilt_ambient_sound(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="volumeGainDb")
    def volume_gain_db(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @volume_gain_db.setter
    def volume_gain_db(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AppVersionSnapshotAppAudioProcessingConfigBargeInConfigArgsDict(TypedDict):
    barge_in_awareness: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppAudioProcessingConfigBargeInConfigArgs:
    def __init__(
        __self__, *, barge_in_awareness: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bargeInAwareness")
    def barge_in_awareness(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @barge_in_awareness.setter
    def barge_in_awareness(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AppVersionSnapshotAppAudioProcessingConfigSynthesizeSpeechConfigArgsDict(
    TypedDict
):
    language_code: pulumi.Input[_builtins.str]
    speaking_rate: NotRequired[pulumi.Input[_builtins.float]]
    voice: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppAudioProcessingConfigSynthesizeSpeechConfigArgs:
    def __init__(
        __self__,
        *,
        language_code: pulumi.Input[_builtins.str],
        speaking_rate: Optional[pulumi.Input[_builtins.float]] = ...,
        voice: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Input[_builtins.str]: ...
    @language_code.setter
    def language_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="speakingRate")
    def speaking_rate(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @speaking_rate.setter
    def speaking_rate(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def voice(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @voice.setter
    def voice(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAppClientCertificateSettingArgsDict(TypedDict):
    passphrase: NotRequired[pulumi.Input[_builtins.str]]
    private_key: NotRequired[pulumi.Input[_builtins.str]]
    tls_certificate: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppClientCertificateSettingArgs:
    def __init__(
        __self__,
        *,
        passphrase: Optional[pulumi.Input[_builtins.str]] = ...,
        private_key: Optional[pulumi.Input[_builtins.str]] = ...,
        tls_certificate: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def passphrase(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @passphrase.setter
    def passphrase(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="privateKey")
    def private_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @private_key.setter
    def private_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="tlsCertificate")
    def tls_certificate(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tls_certificate.setter
    def tls_certificate(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAppDataStoreSettingArgsDict(TypedDict):
    engines: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAppDataStoreSettingEngineArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotAppDataStoreSettingArgs:
    def __init__(
        __self__,
        *,
        engines: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppDataStoreSettingEngineArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def engines(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAppDataStoreSettingEngineArgs]]
        ]
    ]: ...
    @engines.setter
    def engines(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotAppDataStoreSettingEngineArgs]]
            ]
        ],
    ): ...

class AppVersionSnapshotAppDataStoreSettingEngineArgsDict(TypedDict):
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppDataStoreSettingEngineArgs:
    def __init__(
        __self__,
        *,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAppDefaultChannelProfileArgsDict(TypedDict):
    channel_type: NotRequired[pulumi.Input[_builtins.str]]
    disable_barge_in_control: NotRequired[pulumi.Input[_builtins.bool]]
    disable_dtmf: NotRequired[pulumi.Input[_builtins.bool]]
    persona_properties: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppDefaultChannelProfilePersonaPropertyArgsDict
                ]
            ]
        ]
    ]
    profile_id: NotRequired[pulumi.Input[_builtins.str]]
    web_widget_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppDefaultChannelProfileWebWidgetConfigArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotAppDefaultChannelProfileArgs:
    def __init__(
        __self__,
        *,
        channel_type: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_barge_in_control: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_dtmf: Optional[pulumi.Input[_builtins.bool]] = ...,
        persona_properties: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppDefaultChannelProfilePersonaPropertyArgs
                    ]
                ]
            ]
        ] = ...,
        profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        web_widget_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppDefaultChannelProfileWebWidgetConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @channel_type.setter
    def channel_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableBargeInControl")
    def disable_barge_in_control(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_barge_in_control.setter
    def disable_barge_in_control(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableDtmf")
    def disable_dtmf(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_dtmf.setter
    def disable_dtmf(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="personaProperties")
    def persona_properties(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppDefaultChannelProfilePersonaPropertyArgs
                ]
            ]
        ]
    ]: ...
    @persona_properties.setter
    def persona_properties(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppDefaultChannelProfilePersonaPropertyArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile_id.setter
    def profile_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webWidgetConfigs")
    def web_widget_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppDefaultChannelProfileWebWidgetConfigArgs
                ]
            ]
        ]
    ]: ...
    @web_widget_configs.setter
    def web_widget_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppDefaultChannelProfileWebWidgetConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotAppDefaultChannelProfilePersonaPropertyArgsDict(TypedDict):
    persona: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppDefaultChannelProfilePersonaPropertyArgs:
    def __init__(
        __self__, *, persona: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def persona(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @persona.setter
    def persona(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAppDefaultChannelProfileWebWidgetConfigArgsDict(TypedDict):
    modality: NotRequired[pulumi.Input[_builtins.str]]
    theme: NotRequired[pulumi.Input[_builtins.str]]
    web_widget_title: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppDefaultChannelProfileWebWidgetConfigArgs:
    def __init__(
        __self__,
        *,
        modality: Optional[pulumi.Input[_builtins.str]] = ...,
        theme: Optional[pulumi.Input[_builtins.str]] = ...,
        web_widget_title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def modality(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @modality.setter
    def modality(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def theme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @theme.setter
    def theme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webWidgetTitle")
    def web_widget_title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_widget_title.setter
    def web_widget_title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAppEvaluationMetricsThresholdArgsDict(TypedDict):
    golden_evaluation_metrics_thresholds: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotAppEvaluationMetricsThresholdArgs:
    def __init__(
        __self__,
        *,
        golden_evaluation_metrics_thresholds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="goldenEvaluationMetricsThresholds")
    def golden_evaluation_metrics_thresholds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdArgs
                ]
            ]
        ]
    ]: ...
    @golden_evaluation_metrics_thresholds.setter
    def golden_evaluation_metrics_thresholds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdArgsDict(
    TypedDict
):
    expectation_level_metrics_thresholds: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdExpectationLevelMetricsThresholdArgsDict
                ]
            ]
        ]
    ]
    turn_level_metrics_thresholds: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdTurnLevelMetricsThresholdArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdArgs:
    def __init__(
        __self__,
        *,
        expectation_level_metrics_thresholds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdExpectationLevelMetricsThresholdArgs
                    ]
                ]
            ]
        ] = ...,
        turn_level_metrics_thresholds: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdTurnLevelMetricsThresholdArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="expectationLevelMetricsThresholds")
    def expectation_level_metrics_thresholds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdExpectationLevelMetricsThresholdArgs
                ]
            ]
        ]
    ]: ...
    @expectation_level_metrics_thresholds.setter
    def expectation_level_metrics_thresholds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdExpectationLevelMetricsThresholdArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="turnLevelMetricsThresholds")
    def turn_level_metrics_thresholds(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdTurnLevelMetricsThresholdArgs
                ]
            ]
        ]
    ]: ...
    @turn_level_metrics_thresholds.setter
    def turn_level_metrics_thresholds(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdTurnLevelMetricsThresholdArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdExpectationLevelMetricsThresholdArgsDict(
    TypedDict
):
    tool_invocation_parameter_correctness_threshold: NotRequired[
        pulumi.Input[_builtins.float]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdExpectationLevelMetricsThresholdArgs:
    def __init__(
        __self__,
        *,
        tool_invocation_parameter_correctness_threshold: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="toolInvocationParameterCorrectnessThreshold")
    def tool_invocation_parameter_correctness_threshold(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @tool_invocation_parameter_correctness_threshold.setter
    def tool_invocation_parameter_correctness_threshold(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...

class AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdTurnLevelMetricsThresholdArgsDict(
    TypedDict
):
    overall_tool_invocation_correctness_threshold: NotRequired[
        pulumi.Input[_builtins.float]
    ]
    semantic_similarity_success_threshold: NotRequired[pulumi.Input[_builtins.int]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppEvaluationMetricsThresholdGoldenEvaluationMetricsThresholdTurnLevelMetricsThresholdArgs:
    def __init__(
        __self__,
        *,
        overall_tool_invocation_correctness_threshold: Optional[
            pulumi.Input[_builtins.float]
        ] = ...,
        semantic_similarity_success_threshold: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="overallToolInvocationCorrectnessThreshold")
    def overall_tool_invocation_correctness_threshold(
        self,
    ) -> Optional[pulumi.Input[_builtins.float]]: ...
    @overall_tool_invocation_correctness_threshold.setter
    def overall_tool_invocation_correctness_threshold(
        self, value: Optional[pulumi.Input[_builtins.float]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="semanticSimilaritySuccessThreshold")
    def semantic_similarity_success_threshold(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @semantic_similarity_success_threshold.setter
    def semantic_similarity_success_threshold(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class AppVersionSnapshotAppLanguageSettingArgsDict(TypedDict):
    default_language_code: NotRequired[pulumi.Input[_builtins.str]]
    enable_multilingual_support: NotRequired[pulumi.Input[_builtins.bool]]
    fallback_action: NotRequired[pulumi.Input[_builtins.str]]
    supported_language_codes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotAppLanguageSettingArgs:
    def __init__(
        __self__,
        *,
        default_language_code: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_multilingual_support: Optional[pulumi.Input[_builtins.bool]] = ...,
        fallback_action: Optional[pulumi.Input[_builtins.str]] = ...,
        supported_language_codes: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultLanguageCode")
    def default_language_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_language_code.setter
    def default_language_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableMultilingualSupport")
    def enable_multilingual_support(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_multilingual_support.setter
    def enable_multilingual_support(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="fallbackAction")
    def fallback_action(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fallback_action.setter
    def fallback_action(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="supportedLanguageCodes")
    def supported_language_codes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @supported_language_codes.setter
    def supported_language_codes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class AppVersionSnapshotAppLoggingSettingArgsDict(TypedDict):
    audio_recording_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppLoggingSettingAudioRecordingConfigArgsDict
                ]
            ]
        ]
    ]
    bigquery_export_settings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppLoggingSettingBigqueryExportSettingArgsDict
                ]
            ]
        ]
    ]
    cloud_logging_settings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppLoggingSettingCloudLoggingSettingArgsDict
                ]
            ]
        ]
    ]
    conversation_logging_settings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppLoggingSettingConversationLoggingSettingArgsDict
                ]
            ]
        ]
    ]
    redaction_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotAppLoggingSettingRedactionConfigArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotAppLoggingSettingArgs:
    def __init__(
        __self__,
        *,
        audio_recording_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppLoggingSettingAudioRecordingConfigArgs
                    ]
                ]
            ]
        ] = ...,
        bigquery_export_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppLoggingSettingBigqueryExportSettingArgs
                    ]
                ]
            ]
        ] = ...,
        cloud_logging_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppLoggingSettingCloudLoggingSettingArgs
                    ]
                ]
            ]
        ] = ...,
        conversation_logging_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppLoggingSettingConversationLoggingSettingArgs
                    ]
                ]
            ]
        ] = ...,
        redaction_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotAppLoggingSettingRedactionConfigArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="audioRecordingConfigs")
    def audio_recording_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppLoggingSettingAudioRecordingConfigArgs
                ]
            ]
        ]
    ]: ...
    @audio_recording_configs.setter
    def audio_recording_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppLoggingSettingAudioRecordingConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bigqueryExportSettings")
    def bigquery_export_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppLoggingSettingBigqueryExportSettingArgs
                ]
            ]
        ]
    ]: ...
    @bigquery_export_settings.setter
    def bigquery_export_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppLoggingSettingBigqueryExportSettingArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="cloudLoggingSettings")
    def cloud_logging_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotAppLoggingSettingCloudLoggingSettingArgs]
            ]
        ]
    ]: ...
    @cloud_logging_settings.setter
    def cloud_logging_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppLoggingSettingCloudLoggingSettingArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="conversationLoggingSettings")
    def conversation_logging_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotAppLoggingSettingConversationLoggingSettingArgs
                ]
            ]
        ]
    ]: ...
    @conversation_logging_settings.setter
    def conversation_logging_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotAppLoggingSettingConversationLoggingSettingArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="redactionConfigs")
    def redaction_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotAppLoggingSettingRedactionConfigArgs]
            ]
        ]
    ]: ...
    @redaction_configs.setter
    def redaction_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotAppLoggingSettingRedactionConfigArgs]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotAppLoggingSettingAudioRecordingConfigArgsDict(TypedDict):
    gcs_bucket: NotRequired[pulumi.Input[_builtins.str]]
    gcs_path_prefix: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppLoggingSettingAudioRecordingConfigArgs:
    def __init__(
        __self__,
        *,
        gcs_bucket: Optional[pulumi.Input[_builtins.str]] = ...,
        gcs_path_prefix: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gcsBucket")
    def gcs_bucket(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcs_bucket.setter
    def gcs_bucket(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gcsPathPrefix")
    def gcs_path_prefix(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @gcs_path_prefix.setter
    def gcs_path_prefix(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAppLoggingSettingBigqueryExportSettingArgsDict(TypedDict):
    dataset: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    project: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppLoggingSettingBigqueryExportSettingArgs:
    def __init__(
        __self__,
        *,
        dataset: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def dataset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @dataset.setter
    def dataset(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAppLoggingSettingCloudLoggingSettingArgsDict(TypedDict):
    enable_cloud_logging: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppLoggingSettingCloudLoggingSettingArgs:
    def __init__(
        __self__, *, enable_cloud_logging: Optional[pulumi.Input[_builtins.bool]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="enableCloudLogging")
    def enable_cloud_logging(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_cloud_logging.setter
    def enable_cloud_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AppVersionSnapshotAppLoggingSettingConversationLoggingSettingArgsDict(TypedDict):
    disable_conversation_logging: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppLoggingSettingConversationLoggingSettingArgs:
    def __init__(
        __self__,
        *,
        disable_conversation_logging: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="disableConversationLogging")
    def disable_conversation_logging(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_conversation_logging.setter
    def disable_conversation_logging(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...

class AppVersionSnapshotAppLoggingSettingRedactionConfigArgsDict(TypedDict):
    deidentify_template: NotRequired[pulumi.Input[_builtins.str]]
    enable_redaction: NotRequired[pulumi.Input[_builtins.bool]]
    inspect_template: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppLoggingSettingRedactionConfigArgs:
    def __init__(
        __self__,
        *,
        deidentify_template: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_redaction: Optional[pulumi.Input[_builtins.bool]] = ...,
        inspect_template: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="deidentifyTemplate")
    def deidentify_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @deidentify_template.setter
    def deidentify_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableRedaction")
    def enable_redaction(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_redaction.setter
    def enable_redaction(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="inspectTemplate")
    def inspect_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @inspect_template.setter
    def inspect_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAppModelSettingArgsDict(TypedDict):
    model: NotRequired[pulumi.Input[_builtins.str]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppModelSettingArgs:
    def __init__(
        __self__,
        *,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        temperature: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AppVersionSnapshotAppTimeZoneSettingArgsDict(TypedDict):
    time_zone: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppTimeZoneSettingArgs:
    def __init__(
        __self__, *, time_zone: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotAppVariableDeclarationArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    schemas: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotAppVariableDeclarationSchemaArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotAppVariableDeclarationArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        schemas: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotAppVariableDeclarationSchemaArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def schemas(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotAppVariableDeclarationSchemaArgs]]
        ]
    ]: ...
    @schemas.setter
    def schemas(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotAppVariableDeclarationSchemaArgs]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotAppVariableDeclarationSchemaArgsDict(TypedDict):
    additional_properties: NotRequired[pulumi.Input[_builtins.str]]
    any_of: NotRequired[pulumi.Input[_builtins.str]]
    default: NotRequired[pulumi.Input[_builtins.str]]
    defs: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    enums: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    items: NotRequired[pulumi.Input[_builtins.str]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    prefix_items: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[_builtins.str]]
    ref: NotRequired[pulumi.Input[_builtins.str]]
    requireds: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    unique_items: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AppVersionSnapshotAppVariableDeclarationSchemaArgs:
    def __init__(
        __self__,
        *,
        additional_properties: Optional[pulumi.Input[_builtins.str]] = ...,
        any_of: Optional[pulumi.Input[_builtins.str]] = ...,
        default: Optional[pulumi.Input[_builtins.str]] = ...,
        defs: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enums: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        items: Optional[pulumi.Input[_builtins.str]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        prefix_items: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[_builtins.str]] = ...,
        ref: Optional[pulumi.Input[_builtins.str]] = ...,
        requireds: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        unique_items: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_properties.setter
    def additional_properties(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @any_of.setter
    def any_of(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default.setter
    def default(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def defs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @defs.setter
    def defs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enums(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enums.setter
    def enums(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items.setter
    def items(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixItems")
    def prefix_items(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix_items.setter
    def prefix_items(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ref.setter
    def ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def requireds(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @requireds.setter
    def requireds(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="uniqueItems")
    def unique_items(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @unique_items.setter
    def unique_items(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AppVersionSnapshotExampleArgsDict(TypedDict):
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    entry_agent: NotRequired[pulumi.Input[_builtins.str]]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    invalid: NotRequired[pulumi.Input[_builtins.bool]]
    messages: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotExampleMessageArgsDict]]]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotExampleArgs:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        entry_agent: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        invalid: Optional[pulumi.Input[_builtins.bool]] = ...,
        messages: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotExampleMessageArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="entryAgent")
    def entry_agent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @entry_agent.setter
    def entry_agent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def invalid(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @invalid.setter
    def invalid(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def messages(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotExampleMessageArgs]]]
    ]: ...
    @messages.setter
    def messages(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotExampleMessageArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotExampleMessageArgsDict(TypedDict):
    chunks: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotExampleMessageChunkArgsDict]]
        ]
    ]
    role: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotExampleMessageArgs:
    def __init__(
        __self__,
        *,
        chunks: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotExampleMessageChunkArgs]]
            ]
        ] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def chunks(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotExampleMessageChunkArgs]]]
    ]: ...
    @chunks.setter
    def chunks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotExampleMessageChunkArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotExampleMessageChunkArgsDict(TypedDict):
    agent_transfers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotExampleMessageChunkAgentTransferArgsDict]
            ]
        ]
    ]
    images: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotExampleMessageChunkImageArgsDict]]
        ]
    ]
    text: NotRequired[pulumi.Input[_builtins.str]]
    tool_calls: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotExampleMessageChunkToolCallArgsDict]
            ]
        ]
    ]
    tool_responses: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotExampleMessageChunkToolResponseArgsDict]
            ]
        ]
    ]
    updated_variables: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotExampleMessageChunkArgs:
    def __init__(
        __self__,
        *,
        agent_transfers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotExampleMessageChunkAgentTransferArgs]
                ]
            ]
        ] = ...,
        images: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotExampleMessageChunkImageArgs]]
            ]
        ] = ...,
        text: Optional[pulumi.Input[_builtins.str]] = ...,
        tool_calls: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotExampleMessageChunkToolCallArgs]
                ]
            ]
        ] = ...,
        tool_responses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotExampleMessageChunkToolResponseArgs]
                ]
            ]
        ] = ...,
        updated_variables: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentTransfers")
    def agent_transfers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotExampleMessageChunkAgentTransferArgs]
            ]
        ]
    ]: ...
    @agent_transfers.setter
    def agent_transfers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotExampleMessageChunkAgentTransferArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def images(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotExampleMessageChunkImageArgs]]
        ]
    ]: ...
    @images.setter
    def images(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotExampleMessageChunkImageArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="toolCalls")
    def tool_calls(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotExampleMessageChunkToolCallArgs]]
        ]
    ]: ...
    @tool_calls.setter
    def tool_calls(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotExampleMessageChunkToolCallArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="toolResponses")
    def tool_responses(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotExampleMessageChunkToolResponseArgs]
            ]
        ]
    ]: ...
    @tool_responses.setter
    def tool_responses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotExampleMessageChunkToolResponseArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updatedVariables")
    def updated_variables(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @updated_variables.setter
    def updated_variables(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotExampleMessageChunkAgentTransferArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    target_agent: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotExampleMessageChunkAgentTransferArgs:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        target_agent: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="targetAgent")
    def target_agent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @target_agent.setter
    def target_agent(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotExampleMessageChunkImageArgsDict(TypedDict):
    data: NotRequired[pulumi.Input[_builtins.str]]
    mime_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotExampleMessageChunkImageArgs:
    def __init__(
        __self__,
        *,
        data: Optional[pulumi.Input[_builtins.str]] = ...,
        mime_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data.setter
    def data(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mime_type.setter
    def mime_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotExampleMessageChunkToolCallArgsDict(TypedDict):
    args: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    tool: NotRequired[pulumi.Input[_builtins.str]]
    toolset_tools: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotExampleMessageChunkToolCallToolsetToolArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotExampleMessageChunkToolCallArgs:
    def __init__(
        __self__,
        *,
        args: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        tool: Optional[pulumi.Input[_builtins.str]] = ...,
        toolset_tools: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotExampleMessageChunkToolCallToolsetToolArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @args.setter
    def args(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tool.setter
    def tool(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="toolsetTools")
    def toolset_tools(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotExampleMessageChunkToolCallToolsetToolArgs
                ]
            ]
        ]
    ]: ...
    @toolset_tools.setter
    def toolset_tools(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotExampleMessageChunkToolCallToolsetToolArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotExampleMessageChunkToolCallToolsetToolArgsDict(TypedDict):
    tool_id: NotRequired[pulumi.Input[_builtins.str]]
    toolset: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotExampleMessageChunkToolCallToolsetToolArgs:
    def __init__(
        __self__,
        *,
        tool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        toolset: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="toolId")
    def tool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tool_id.setter
    def tool_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def toolset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @toolset.setter
    def toolset(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotExampleMessageChunkToolResponseArgsDict(TypedDict):
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    response: NotRequired[pulumi.Input[_builtins.str]]
    tool: NotRequired[pulumi.Input[_builtins.str]]
    toolset_tools: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotExampleMessageChunkToolResponseToolsetToolArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotExampleMessageChunkToolResponseArgs:
    def __init__(
        __self__,
        *,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        response: Optional[pulumi.Input[_builtins.str]] = ...,
        tool: Optional[pulumi.Input[_builtins.str]] = ...,
        toolset_tools: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotExampleMessageChunkToolResponseToolsetToolArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @response.setter
    def response(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tool.setter
    def tool(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="toolsetTools")
    def toolset_tools(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotExampleMessageChunkToolResponseToolsetToolArgs
                ]
            ]
        ]
    ]: ...
    @toolset_tools.setter
    def toolset_tools(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotExampleMessageChunkToolResponseToolsetToolArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotExampleMessageChunkToolResponseToolsetToolArgsDict(TypedDict):
    tool_id: NotRequired[pulumi.Input[_builtins.str]]
    toolset: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotExampleMessageChunkToolResponseToolsetToolArgs:
    def __init__(
        __self__,
        *,
        tool_id: Optional[pulumi.Input[_builtins.str]] = ...,
        toolset: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="toolId")
    def tool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tool_id.setter
    def tool_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def toolset(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @toolset.setter
    def toolset(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotGuardrailArgsDict(TypedDict):
    actions: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotGuardrailActionArgsDict]]]
    ]
    code_callbacks: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotGuardrailCodeCallbackArgsDict]]
        ]
    ]
    content_filters: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotGuardrailContentFilterArgsDict]]
        ]
    ]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    enabled: NotRequired[pulumi.Input[_builtins.bool]]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    llm_policies: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotGuardrailLlmPolicyArgsDict]]
        ]
    ]
    llm_prompt_securities: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotGuardrailLlmPromptSecurityArgsDict]]
        ]
    ]
    model_safeties: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotGuardrailModelSafetyArgsDict]]
        ]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailArgs:
    def __init__(
        __self__,
        *,
        actions: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotGuardrailActionArgs]]]
        ] = ...,
        code_callbacks: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotGuardrailCodeCallbackArgs]]
            ]
        ] = ...,
        content_filters: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotGuardrailContentFilterArgs]]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        enabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        llm_policies: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotGuardrailLlmPolicyArgs]]
            ]
        ] = ...,
        llm_prompt_securities: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotGuardrailLlmPromptSecurityArgs]]
            ]
        ] = ...,
        model_safeties: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotGuardrailModelSafetyArgs]]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def actions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotGuardrailActionArgs]]]
    ]: ...
    @actions.setter
    def actions(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotGuardrailActionArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="codeCallbacks")
    def code_callbacks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotGuardrailCodeCallbackArgs]]
        ]
    ]: ...
    @code_callbacks.setter
    def code_callbacks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotGuardrailCodeCallbackArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="contentFilters")
    def content_filters(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotGuardrailContentFilterArgs]]
        ]
    ]: ...
    @content_filters.setter
    def content_filters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotGuardrailContentFilterArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="llmPolicies")
    def llm_policies(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotGuardrailLlmPolicyArgs]]]
    ]: ...
    @llm_policies.setter
    def llm_policies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotGuardrailLlmPolicyArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="llmPromptSecurities")
    def llm_prompt_securities(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotGuardrailLlmPromptSecurityArgs]]
        ]
    ]: ...
    @llm_prompt_securities.setter
    def llm_prompt_securities(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotGuardrailLlmPromptSecurityArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelSafeties")
    def model_safeties(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotGuardrailModelSafetyArgs]]]
    ]: ...
    @model_safeties.setter
    def model_safeties(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotGuardrailModelSafetyArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotGuardrailActionArgsDict(TypedDict):
    generative_answers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotGuardrailActionGenerativeAnswerArgsDict]
            ]
        ]
    ]
    respond_immediatelies: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailActionRespondImmediatelyArgsDict
                ]
            ]
        ]
    ]
    transfer_agents: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotGuardrailActionTransferAgentArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailActionArgs:
    def __init__(
        __self__,
        *,
        generative_answers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotGuardrailActionGenerativeAnswerArgs]
                ]
            ]
        ] = ...,
        respond_immediatelies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailActionRespondImmediatelyArgs
                    ]
                ]
            ]
        ] = ...,
        transfer_agents: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotGuardrailActionTransferAgentArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="generativeAnswers")
    def generative_answers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotGuardrailActionGenerativeAnswerArgs]
            ]
        ]
    ]: ...
    @generative_answers.setter
    def generative_answers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotGuardrailActionGenerativeAnswerArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="respondImmediatelies")
    def respond_immediatelies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotGuardrailActionRespondImmediatelyArgs]
            ]
        ]
    ]: ...
    @respond_immediatelies.setter
    def respond_immediatelies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailActionRespondImmediatelyArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="transferAgents")
    def transfer_agents(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotGuardrailActionTransferAgentArgs]]
        ]
    ]: ...
    @transfer_agents.setter
    def transfer_agents(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotGuardrailActionTransferAgentArgs]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotGuardrailActionGenerativeAnswerArgsDict(TypedDict):
    prompt: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailActionGenerativeAnswerArgs:
    def __init__(
        __self__, *, prompt: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prompt.setter
    def prompt(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotGuardrailActionRespondImmediatelyArgsDict(TypedDict):
    responses: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailActionRespondImmediatelyResponseArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailActionRespondImmediatelyArgs:
    def __init__(
        __self__,
        *,
        responses: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailActionRespondImmediatelyResponseArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def responses(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailActionRespondImmediatelyResponseArgs
                ]
            ]
        ]
    ]: ...
    @responses.setter
    def responses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailActionRespondImmediatelyResponseArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotGuardrailActionRespondImmediatelyResponseArgsDict(TypedDict):
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    text: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailActionRespondImmediatelyResponseArgs:
    def __init__(
        __self__,
        *,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        text: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotGuardrailActionTransferAgentArgsDict(TypedDict):
    agent: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailActionTransferAgentArgs:
    def __init__(
        __self__, *, agent: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def agent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent.setter
    def agent(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotGuardrailCodeCallbackArgsDict(TypedDict):
    after_agent_callbacks: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailCodeCallbackAfterAgentCallbackArgsDict
                ]
            ]
        ]
    ]
    after_model_callbacks: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailCodeCallbackAfterModelCallbackArgsDict
                ]
            ]
        ]
    ]
    before_agent_callbacks: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailCodeCallbackBeforeAgentCallbackArgsDict
                ]
            ]
        ]
    ]
    before_model_callbacks: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailCodeCallbackBeforeModelCallbackArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailCodeCallbackArgs:
    def __init__(
        __self__,
        *,
        after_agent_callbacks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailCodeCallbackAfterAgentCallbackArgs
                    ]
                ]
            ]
        ] = ...,
        after_model_callbacks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailCodeCallbackAfterModelCallbackArgs
                    ]
                ]
            ]
        ] = ...,
        before_agent_callbacks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailCodeCallbackBeforeAgentCallbackArgs
                    ]
                ]
            ]
        ] = ...,
        before_model_callbacks: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailCodeCallbackBeforeModelCallbackArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="afterAgentCallbacks")
    def after_agent_callbacks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailCodeCallbackAfterAgentCallbackArgs
                ]
            ]
        ]
    ]: ...
    @after_agent_callbacks.setter
    def after_agent_callbacks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailCodeCallbackAfterAgentCallbackArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="afterModelCallbacks")
    def after_model_callbacks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailCodeCallbackAfterModelCallbackArgs
                ]
            ]
        ]
    ]: ...
    @after_model_callbacks.setter
    def after_model_callbacks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailCodeCallbackAfterModelCallbackArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="beforeAgentCallbacks")
    def before_agent_callbacks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailCodeCallbackBeforeAgentCallbackArgs
                ]
            ]
        ]
    ]: ...
    @before_agent_callbacks.setter
    def before_agent_callbacks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailCodeCallbackBeforeAgentCallbackArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="beforeModelCallbacks")
    def before_model_callbacks(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailCodeCallbackBeforeModelCallbackArgs
                ]
            ]
        ]
    ]: ...
    @before_model_callbacks.setter
    def before_model_callbacks(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailCodeCallbackBeforeModelCallbackArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotGuardrailCodeCallbackAfterAgentCallbackArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    python_code: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailCodeCallbackAfterAgentCallbackArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        python_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @python_code.setter
    def python_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotGuardrailCodeCallbackAfterModelCallbackArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    python_code: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailCodeCallbackAfterModelCallbackArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        python_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @python_code.setter
    def python_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotGuardrailCodeCallbackBeforeAgentCallbackArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    python_code: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailCodeCallbackBeforeAgentCallbackArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        python_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @python_code.setter
    def python_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotGuardrailCodeCallbackBeforeModelCallbackArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    python_code: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailCodeCallbackBeforeModelCallbackArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        python_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @python_code.setter
    def python_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotGuardrailContentFilterArgsDict(TypedDict):
    banned_contents: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    banned_contents_in_agent_responses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    banned_contents_in_user_inputs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    disregard_diacritics: NotRequired[pulumi.Input[_builtins.bool]]
    match_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailContentFilterArgs:
    def __init__(
        __self__,
        *,
        banned_contents: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        banned_contents_in_agent_responses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        banned_contents_in_user_inputs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        disregard_diacritics: Optional[pulumi.Input[_builtins.bool]] = ...,
        match_type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="bannedContents")
    def banned_contents(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @banned_contents.setter
    def banned_contents(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bannedContentsInAgentResponses")
    def banned_contents_in_agent_responses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @banned_contents_in_agent_responses.setter
    def banned_contents_in_agent_responses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bannedContentsInUserInputs")
    def banned_contents_in_user_inputs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @banned_contents_in_user_inputs.setter
    def banned_contents_in_user_inputs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disregardDiacritics")
    def disregard_diacritics(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disregard_diacritics.setter
    def disregard_diacritics(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="matchType")
    def match_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @match_type.setter
    def match_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotGuardrailLlmPolicyArgsDict(TypedDict):
    fail_open: NotRequired[pulumi.Input[_builtins.bool]]
    max_conversation_messages: NotRequired[pulumi.Input[_builtins.int]]
    model_settings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotGuardrailLlmPolicyModelSettingArgsDict]
            ]
        ]
    ]
    policy_scope: NotRequired[pulumi.Input[_builtins.str]]
    prompt: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailLlmPolicyArgs:
    def __init__(
        __self__,
        *,
        fail_open: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_conversation_messages: Optional[pulumi.Input[_builtins.int]] = ...,
        model_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotGuardrailLlmPolicyModelSettingArgs]
                ]
            ]
        ] = ...,
        policy_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        prompt: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failOpen")
    def fail_open(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fail_open.setter
    def fail_open(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxConversationMessages")
    def max_conversation_messages(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_conversation_messages.setter
    def max_conversation_messages(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotGuardrailLlmPolicyModelSettingArgs]]
        ]
    ]: ...
    @model_settings.setter
    def model_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotGuardrailLlmPolicyModelSettingArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyScope")
    def policy_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_scope.setter
    def policy_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prompt.setter
    def prompt(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotGuardrailLlmPolicyModelSettingArgsDict(TypedDict):
    model: NotRequired[pulumi.Input[_builtins.str]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailLlmPolicyModelSettingArgs:
    def __init__(
        __self__,
        *,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        temperature: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AppVersionSnapshotGuardrailLlmPromptSecurityArgsDict(TypedDict):
    custom_policies: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicyArgsDict
                ]
            ]
        ]
    ]
    default_settings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailLlmPromptSecurityDefaultSettingArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailLlmPromptSecurityArgs:
    def __init__(
        __self__,
        *,
        custom_policies: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicyArgs
                    ]
                ]
            ]
        ] = ...,
        default_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailLlmPromptSecurityDefaultSettingArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customPolicies")
    def custom_policies(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicyArgs
                ]
            ]
        ]
    ]: ...
    @custom_policies.setter
    def custom_policies(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicyArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultSettings")
    def default_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailLlmPromptSecurityDefaultSettingArgs
                ]
            ]
        ]
    ]: ...
    @default_settings.setter
    def default_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailLlmPromptSecurityDefaultSettingArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicyArgsDict(TypedDict):
    fail_open: NotRequired[pulumi.Input[_builtins.bool]]
    max_conversation_messages: NotRequired[pulumi.Input[_builtins.int]]
    model_settings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicyModelSettingArgsDict
                ]
            ]
        ]
    ]
    policy_scope: NotRequired[pulumi.Input[_builtins.str]]
    prompt: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicyArgs:
    def __init__(
        __self__,
        *,
        fail_open: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_conversation_messages: Optional[pulumi.Input[_builtins.int]] = ...,
        model_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicyModelSettingArgs
                    ]
                ]
            ]
        ] = ...,
        policy_scope: Optional[pulumi.Input[_builtins.str]] = ...,
        prompt: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failOpen")
    def fail_open(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fail_open.setter
    def fail_open(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxConversationMessages")
    def max_conversation_messages(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_conversation_messages.setter
    def max_conversation_messages(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicyModelSettingArgs
                ]
            ]
        ]
    ]: ...
    @model_settings.setter
    def model_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicyModelSettingArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyScope")
    def policy_scope(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy_scope.setter
    def policy_scope(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prompt.setter
    def prompt(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicyModelSettingArgsDict(
    TypedDict
):
    model: NotRequired[pulumi.Input[_builtins.str]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailLlmPromptSecurityCustomPolicyModelSettingArgs:
    def __init__(
        __self__,
        *,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        temperature: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AppVersionSnapshotGuardrailLlmPromptSecurityDefaultSettingArgsDict(TypedDict):
    default_prompt_template: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailLlmPromptSecurityDefaultSettingArgs:
    def __init__(
        __self__,
        *,
        default_prompt_template: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultPromptTemplate")
    def default_prompt_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_prompt_template.setter
    def default_prompt_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotGuardrailModelSafetyArgsDict(TypedDict):
    safety_settings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotGuardrailModelSafetySafetySettingArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailModelSafetyArgs:
    def __init__(
        __self__,
        *,
        safety_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailModelSafetySafetySettingArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="safetySettings")
    def safety_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotGuardrailModelSafetySafetySettingArgs]
            ]
        ]
    ]: ...
    @safety_settings.setter
    def safety_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotGuardrailModelSafetySafetySettingArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotGuardrailModelSafetySafetySettingArgsDict(TypedDict):
    category: NotRequired[pulumi.Input[_builtins.str]]
    threshold: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotGuardrailModelSafetySafetySettingArgs:
    def __init__(
        __self__,
        *,
        category: Optional[pulumi.Input[_builtins.str]] = ...,
        threshold: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @category.setter
    def category(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @threshold.setter
    def threshold(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolArgsDict(TypedDict):
    client_functions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolClientFunctionArgsDict]]
        ]
    ]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    data_store_tools: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolDataStoreToolArgsDict]]
        ]
    ]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    execution_type: NotRequired[pulumi.Input[_builtins.str]]
    generated_summary: NotRequired[pulumi.Input[_builtins.str]]
    google_search_tools: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolGoogleSearchToolArgsDict]]
        ]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    open_api_tools: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolOpenApiToolArgsDict]]]
    ]
    python_functions: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolPythonFunctionArgsDict]]
        ]
    ]
    system_tools: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolSystemToolArgsDict]]]
    ]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolArgs:
    def __init__(
        __self__,
        *,
        client_functions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolClientFunctionArgs]]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        data_store_tools: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolDataStoreToolArgs]]
            ]
        ] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_type: Optional[pulumi.Input[_builtins.str]] = ...,
        generated_summary: Optional[pulumi.Input[_builtins.str]] = ...,
        google_search_tools: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolGoogleSearchToolArgs]]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        open_api_tools: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolOpenApiToolArgs]]]
        ] = ...,
        python_functions: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolPythonFunctionArgs]]
            ]
        ] = ...,
        system_tools: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolSystemToolArgs]]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientFunctions")
    def client_functions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolClientFunctionArgs]]]
    ]: ...
    @client_functions.setter
    def client_functions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolClientFunctionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataStoreTools")
    def data_store_tools(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolDataStoreToolArgs]]]
    ]: ...
    @data_store_tools.setter
    def data_store_tools(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolDataStoreToolArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionType")
    def execution_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_type.setter
    def execution_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="generatedSummary")
    def generated_summary(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generated_summary.setter
    def generated_summary(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="googleSearchTools")
    def google_search_tools(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolGoogleSearchToolArgs]]]
    ]: ...
    @google_search_tools.setter
    def google_search_tools(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolGoogleSearchToolArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="openApiTools")
    def open_api_tools(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolOpenApiToolArgs]]]
    ]: ...
    @open_api_tools.setter
    def open_api_tools(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolOpenApiToolArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="pythonFunctions")
    def python_functions(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolPythonFunctionArgs]]]
    ]: ...
    @python_functions.setter
    def python_functions(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolPythonFunctionArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="systemTools")
    def system_tools(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolSystemToolArgs]]]
    ]: ...
    @system_tools.setter
    def system_tools(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVersionSnapshotToolSystemToolArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolClientFunctionArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotToolClientFunctionParameterArgsDict]
            ]
        ]
    ]
    responses: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolClientFunctionResponseArgsDict]]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotToolClientFunctionArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotToolClientFunctionParameterArgs]
                ]
            ]
        ] = ...,
        responses: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolClientFunctionResponseArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
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
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolClientFunctionParameterArgs]]
        ]
    ]: ...
    @parameters.setter
    def parameters(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotToolClientFunctionParameterArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def responses(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolClientFunctionResponseArgs]]
        ]
    ]: ...
    @responses.setter
    def responses(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolClientFunctionResponseArgs]]
            ]
        ],
    ): ...

class AppVersionSnapshotToolClientFunctionParameterArgsDict(TypedDict):
    additional_properties: NotRequired[pulumi.Input[_builtins.str]]
    any_of: NotRequired[pulumi.Input[_builtins.str]]
    default: NotRequired[pulumi.Input[_builtins.str]]
    defs: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    enums: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    items: NotRequired[pulumi.Input[_builtins.str]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    prefix_items: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[_builtins.str]]
    ref: NotRequired[pulumi.Input[_builtins.str]]
    requireds: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    unique_items: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolClientFunctionParameterArgs:
    def __init__(
        __self__,
        *,
        additional_properties: Optional[pulumi.Input[_builtins.str]] = ...,
        any_of: Optional[pulumi.Input[_builtins.str]] = ...,
        default: Optional[pulumi.Input[_builtins.str]] = ...,
        defs: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enums: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        items: Optional[pulumi.Input[_builtins.str]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        prefix_items: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[_builtins.str]] = ...,
        ref: Optional[pulumi.Input[_builtins.str]] = ...,
        requireds: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        unique_items: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_properties.setter
    def additional_properties(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @any_of.setter
    def any_of(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default.setter
    def default(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def defs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @defs.setter
    def defs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enums(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enums.setter
    def enums(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items.setter
    def items(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixItems")
    def prefix_items(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix_items.setter
    def prefix_items(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ref.setter
    def ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def requireds(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @requireds.setter
    def requireds(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="uniqueItems")
    def unique_items(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @unique_items.setter
    def unique_items(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AppVersionSnapshotToolClientFunctionResponseArgsDict(TypedDict):
    additional_properties: NotRequired[pulumi.Input[_builtins.str]]
    any_of: NotRequired[pulumi.Input[_builtins.str]]
    default: NotRequired[pulumi.Input[_builtins.str]]
    defs: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    enums: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    items: NotRequired[pulumi.Input[_builtins.str]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    prefix_items: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[_builtins.str]]
    ref: NotRequired[pulumi.Input[_builtins.str]]
    requireds: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    unique_items: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolClientFunctionResponseArgs:
    def __init__(
        __self__,
        *,
        additional_properties: Optional[pulumi.Input[_builtins.str]] = ...,
        any_of: Optional[pulumi.Input[_builtins.str]] = ...,
        default: Optional[pulumi.Input[_builtins.str]] = ...,
        defs: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enums: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        items: Optional[pulumi.Input[_builtins.str]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        prefix_items: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[_builtins.str]] = ...,
        ref: Optional[pulumi.Input[_builtins.str]] = ...,
        requireds: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        unique_items: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_properties.setter
    def additional_properties(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @any_of.setter
    def any_of(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default.setter
    def default(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def defs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @defs.setter
    def defs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enums(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enums.setter
    def enums(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items.setter
    def items(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixItems")
    def prefix_items(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix_items.setter
    def prefix_items(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ref.setter
    def ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def requireds(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @requireds.setter
    def requireds(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="uniqueItems")
    def unique_items(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @unique_items.setter
    def unique_items(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class AppVersionSnapshotToolDataStoreToolArgsDict(TypedDict):
    boost_specs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolDataStoreToolBoostSpecArgsDict]]
        ]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    engine_sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotToolDataStoreToolEngineSourceArgsDict]
            ]
        ]
    ]
    max_results: NotRequired[pulumi.Input[_builtins.int]]
    modality_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotToolDataStoreToolModalityConfigArgsDict]
            ]
        ]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolArgs:
    def __init__(
        __self__,
        *,
        boost_specs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolDataStoreToolBoostSpecArgs]]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotToolDataStoreToolEngineSourceArgs]
                ]
            ]
        ] = ...,
        max_results: Optional[pulumi.Input[_builtins.int]] = ...,
        modality_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotToolDataStoreToolModalityConfigArgs]
                ]
            ]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="boostSpecs")
    def boost_specs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolDataStoreToolBoostSpecArgs]]
        ]
    ]: ...
    @boost_specs.setter
    def boost_specs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolDataStoreToolBoostSpecArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineSources")
    def engine_sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolDataStoreToolEngineSourceArgs]]
        ]
    ]: ...
    @engine_sources.setter
    def engine_sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotToolDataStoreToolEngineSourceArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxResults")
    def max_results(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_results.setter
    def max_results(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="modalityConfigs")
    def modality_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotToolDataStoreToolModalityConfigArgs]
            ]
        ]
    ]: ...
    @modality_configs.setter
    def modality_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotToolDataStoreToolModalityConfigArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolDataStoreToolBoostSpecArgsDict(TypedDict):
    data_stores: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    specs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotToolDataStoreToolBoostSpecSpecArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolBoostSpecArgs:
    def __init__(
        __self__,
        *,
        data_stores: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        specs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotToolDataStoreToolBoostSpecSpecArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStores")
    def data_stores(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @data_stores.setter
    def data_stores(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def specs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolDataStoreToolBoostSpecSpecArgs]]
        ]
    ]: ...
    @specs.setter
    def specs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotToolDataStoreToolBoostSpecSpecArgs]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotToolDataStoreToolBoostSpecSpecArgsDict(TypedDict):
    condition_boost_specs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolBoostSpecSpecArgs:
    def __init__(
        __self__,
        *,
        condition_boost_specs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionBoostSpecs")
    def condition_boost_specs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecArgs
                ]
            ]
        ]
    ]: ...
    @condition_boost_specs.setter
    def condition_boost_specs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecArgsDict(
    TypedDict
):
    boost: NotRequired[pulumi.Input[_builtins.float]]
    boost_control_specs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecArgsDict
                ]
            ]
        ]
    ]
    condition: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecArgs:
    def __init__(
        __self__,
        *,
        boost: Optional[pulumi.Input[_builtins.float]] = ...,
        boost_control_specs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecArgs
                    ]
                ]
            ]
        ] = ...,
        condition: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def boost(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @boost.setter
    def boost(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="boostControlSpecs")
    def boost_control_specs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecArgs
                ]
            ]
        ]
    ]: ...
    @boost_control_specs.setter
    def boost_control_specs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @condition.setter
    def condition(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecArgsDict(
    TypedDict
):
    attribute_type: NotRequired[pulumi.Input[_builtins.str]]
    control_points: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPointArgsDict
                ]
            ]
        ]
    ]
    field_name: NotRequired[pulumi.Input[_builtins.str]]
    interpolation_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecArgs:
    def __init__(
        __self__,
        *,
        attribute_type: Optional[pulumi.Input[_builtins.str]] = ...,
        control_points: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPointArgs
                    ]
                ]
            ]
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
    @pulumi.getter(name="controlPoints")
    def control_points(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPointArgs
                ]
            ]
        ]
    ]: ...
    @control_points.setter
    def control_points(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPointArgs
                    ]
                ]
            ]
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

class AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPointArgsDict(
    TypedDict
):
    attribute_value: NotRequired[pulumi.Input[_builtins.str]]
    boost_amount: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPointArgs:
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

class AppVersionSnapshotToolDataStoreToolEngineSourceArgsDict(TypedDict):
    data_store_sources: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceArgsDict
                ]
            ]
        ]
    ]
    engine: NotRequired[pulumi.Input[_builtins.str]]
    filter: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolEngineSourceArgs:
    def __init__(
        __self__,
        *,
        data_store_sources: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceArgs
                    ]
                ]
            ]
        ] = ...,
        engine: Optional[pulumi.Input[_builtins.str]] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreSources")
    def data_store_sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceArgs
                ]
            ]
        ]
    ]: ...
    @data_store_sources.setter
    def data_store_sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @engine.setter
    def engine(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceArgsDict(TypedDict):
    data_stores: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStoreArgsDict
                ]
            ]
        ]
    ]
    filter: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceArgs:
    def __init__(
        __self__,
        *,
        data_stores: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStoreArgs
                    ]
                ]
            ]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStores")
    def data_stores(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStoreArgs
                ]
            ]
        ]
    ]: ...
    @data_stores.setter
    def data_stores(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStoreArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStoreArgsDict(
    TypedDict
):
    connector_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfigArgsDict
                ]
            ]
        ]
    ]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    document_processing_mode: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStoreArgs:
    def __init__(
        __self__,
        *,
        connector_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfigArgs
                    ]
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        document_processing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="connectorConfigs")
    def connector_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfigArgs
                ]
            ]
        ]
    ]: ...
    @connector_configs.setter
    def connector_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="documentProcessingMode")
    def document_processing_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @document_processing_mode.setter
    def document_processing_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfigArgsDict(
    TypedDict
):
    collection: NotRequired[pulumi.Input[_builtins.str]]
    collection_display_name: NotRequired[pulumi.Input[_builtins.str]]
    data_source: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfigArgs:
    def __init__(
        __self__,
        *,
        collection: Optional[pulumi.Input[_builtins.str]] = ...,
        collection_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        data_source: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collection.setter
    def collection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="collectionDisplayName")
    def collection_display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collection_display_name.setter
    def collection_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolDataStoreToolModalityConfigArgsDict(TypedDict):
    grounding_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolModalityConfigGroundingConfigArgsDict
                ]
            ]
        ]
    ]
    modality_type: NotRequired[pulumi.Input[_builtins.str]]
    rewriter_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfigArgsDict
                ]
            ]
        ]
    ]
    summarization_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfigArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolModalityConfigArgs:
    def __init__(
        __self__,
        *,
        grounding_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolModalityConfigGroundingConfigArgs
                    ]
                ]
            ]
        ] = ...,
        modality_type: Optional[pulumi.Input[_builtins.str]] = ...,
        rewriter_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfigArgs
                    ]
                ]
            ]
        ] = ...,
        summarization_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="groundingConfigs")
    def grounding_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolModalityConfigGroundingConfigArgs
                ]
            ]
        ]
    ]: ...
    @grounding_configs.setter
    def grounding_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolModalityConfigGroundingConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="modalityType")
    def modality_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @modality_type.setter
    def modality_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rewriterConfigs")
    def rewriter_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfigArgs
                ]
            ]
        ]
    ]: ...
    @rewriter_configs.setter
    def rewriter_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="summarizationConfigs")
    def summarization_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfigArgs
                ]
            ]
        ]
    ]: ...
    @summarization_configs.setter
    def summarization_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotToolDataStoreToolModalityConfigGroundingConfigArgsDict(
    TypedDict
):
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    grounding_level: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolModalityConfigGroundingConfigArgs:
    def __init__(
        __self__,
        *,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        grounding_level: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="groundingLevel")
    def grounding_level(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @grounding_level.setter
    def grounding_level(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfigArgsDict(
    TypedDict
):
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    model_settings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfigModelSettingArgsDict
                ]
            ]
        ]
    ]
    prompt: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfigArgs:
    def __init__(
        __self__,
        *,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        model_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfigModelSettingArgs
                    ]
                ]
            ]
        ] = ...,
        prompt: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfigModelSettingArgs
                ]
            ]
        ]
    ]: ...
    @model_settings.setter
    def model_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfigModelSettingArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prompt.setter
    def prompt(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfigModelSettingArgsDict(
    TypedDict
):
    model: NotRequired[pulumi.Input[_builtins.str]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolModalityConfigRewriterConfigModelSettingArgs:
    def __init__(
        __self__,
        *,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        temperature: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfigArgsDict(
    TypedDict
):
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    model_settings: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfigModelSettingArgsDict
                ]
            ]
        ]
    ]
    prompt: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfigArgs:
    def __init__(
        __self__,
        *,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        model_settings: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfigModelSettingArgs
                    ]
                ]
            ]
        ] = ...,
        prompt: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfigModelSettingArgs
                ]
            ]
        ]
    ]: ...
    @model_settings.setter
    def model_settings(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfigModelSettingArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prompt.setter
    def prompt(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfigModelSettingArgsDict(
    TypedDict
):
    model: NotRequired[pulumi.Input[_builtins.str]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolDataStoreToolModalityConfigSummarizationConfigModelSettingArgs:
    def __init__(
        __self__,
        *,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        temperature: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class AppVersionSnapshotToolGoogleSearchToolArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    exclude_domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolGoogleSearchToolArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        exclude_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="excludeDomains")
    def exclude_domains(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_domains.setter
    def exclude_domains(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolOpenApiToolArgsDict(TypedDict):
    api_authentications: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotToolOpenApiToolApiAuthenticationArgsDict]
            ]
        ]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ignore_unknown_fields: NotRequired[pulumi.Input[_builtins.bool]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    open_api_schema: NotRequired[pulumi.Input[_builtins.str]]
    service_directory_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolOpenApiToolServiceDirectoryConfigArgsDict
                ]
            ]
        ]
    ]
    tls_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolOpenApiToolTlsConfigArgsDict]]
        ]
    ]
    url: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolOpenApiToolArgs:
    def __init__(
        __self__,
        *,
        api_authentications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotToolOpenApiToolApiAuthenticationArgs]
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_unknown_fields: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        open_api_schema: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolOpenApiToolServiceDirectoryConfigArgs
                    ]
                ]
            ]
        ] = ...,
        tls_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolOpenApiToolTlsConfigArgs]]
            ]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiAuthentications")
    def api_authentications(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotToolOpenApiToolApiAuthenticationArgs]
            ]
        ]
    ]: ...
    @api_authentications.setter
    def api_authentications(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotToolOpenApiToolApiAuthenticationArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreUnknownFields")
    def ignore_unknown_fields(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_unknown_fields.setter
    def ignore_unknown_fields(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="openApiSchema")
    def open_api_schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @open_api_schema.setter
    def open_api_schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfigs")
    def service_directory_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolOpenApiToolServiceDirectoryConfigArgs
                ]
            ]
        ]
    ]: ...
    @service_directory_configs.setter
    def service_directory_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolOpenApiToolServiceDirectoryConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tlsConfigs")
    def tls_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolOpenApiToolTlsConfigArgs]]
        ]
    ]: ...
    @tls_configs.setter
    def tls_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolOpenApiToolTlsConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolOpenApiToolApiAuthenticationArgsDict(TypedDict):
    api_key_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolOpenApiToolApiAuthenticationApiKeyConfigArgsDict
                ]
            ]
        ]
    ]
    oauth_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolOpenApiToolApiAuthenticationOauthConfigArgsDict
                ]
            ]
        ]
    ]
    service_account_auth_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAccountAuthConfigArgsDict
                ]
            ]
        ]
    ]
    service_agent_id_token_auth_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfigArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotToolOpenApiToolApiAuthenticationArgs:
    def __init__(
        __self__,
        *,
        api_key_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolOpenApiToolApiAuthenticationApiKeyConfigArgs
                    ]
                ]
            ]
        ] = ...,
        oauth_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolOpenApiToolApiAuthenticationOauthConfigArgs
                    ]
                ]
            ]
        ] = ...,
        service_account_auth_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAccountAuthConfigArgs
                    ]
                ]
            ]
        ] = ...,
        service_agent_id_token_auth_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyConfigs")
    def api_key_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolOpenApiToolApiAuthenticationApiKeyConfigArgs
                ]
            ]
        ]
    ]: ...
    @api_key_configs.setter
    def api_key_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolOpenApiToolApiAuthenticationApiKeyConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="oauthConfigs")
    def oauth_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolOpenApiToolApiAuthenticationOauthConfigArgs
                ]
            ]
        ]
    ]: ...
    @oauth_configs.setter
    def oauth_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolOpenApiToolApiAuthenticationOauthConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountAuthConfigs")
    def service_account_auth_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAccountAuthConfigArgs
                ]
            ]
        ]
    ]: ...
    @service_account_auth_configs.setter
    def service_account_auth_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAccountAuthConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAgentIdTokenAuthConfigs")
    def service_agent_id_token_auth_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfigArgs
                ]
            ]
        ]
    ]: ...
    @service_agent_id_token_auth_configs.setter
    def service_agent_id_token_auth_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotToolOpenApiToolApiAuthenticationApiKeyConfigArgsDict(TypedDict):
    api_key_secret_version: NotRequired[pulumi.Input[_builtins.str]]
    key_name: NotRequired[pulumi.Input[_builtins.str]]
    request_location: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolOpenApiToolApiAuthenticationApiKeyConfigArgs:
    def __init__(
        __self__,
        *,
        api_key_secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
        key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        request_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeySecretVersion")
    def api_key_secret_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key_secret_version.setter
    def api_key_secret_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestLocation")
    def request_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_location.setter
    def request_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolOpenApiToolApiAuthenticationOauthConfigArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_version: NotRequired[pulumi.Input[_builtins.str]]
    oauth_grant_type: NotRequired[pulumi.Input[_builtins.str]]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    token_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolOpenApiToolApiAuthenticationOauthConfigArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_grant_type: Optional[pulumi.Input[_builtins.str]] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        token_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecretVersion")
    def client_secret_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret_version.setter
    def client_secret_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthGrantType")
    def oauth_grant_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oauth_grant_type.setter
    def oauth_grant_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scopes.setter
    def scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token_endpoint.setter
    def token_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAccountAuthConfigArgsDict(
    TypedDict
):
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAccountAuthConfigArgs:
    def __init__(
        __self__, *, service_account: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfigArgsDict(
    TypedDict
): ...

@pulumi.input_type
class AppVersionSnapshotToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfigArgs:
    def __init__(__self__) -> None: ...

class AppVersionSnapshotToolOpenApiToolServiceDirectoryConfigArgsDict(TypedDict):
    service: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolOpenApiToolServiceDirectoryConfigArgs:
    def __init__(
        __self__, *, service: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolOpenApiToolTlsConfigArgsDict(TypedDict):
    ca_certs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotToolOpenApiToolTlsConfigCaCertArgsDict]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotToolOpenApiToolTlsConfigArgs:
    def __init__(
        __self__,
        *,
        ca_certs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotToolOpenApiToolTlsConfigCaCertArgs]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolOpenApiToolTlsConfigCaCertArgs]]
        ]
    ]: ...
    @ca_certs.setter
    def ca_certs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotToolOpenApiToolTlsConfigCaCertArgs]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotToolOpenApiToolTlsConfigCaCertArgsDict(TypedDict):
    cert: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolOpenApiToolTlsConfigCaCertArgs:
    def __init__(
        __self__,
        *,
        cert: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cert.setter
    def cert(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolPythonFunctionArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    python_code: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolPythonFunctionArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        python_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @python_code.setter
    def python_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolSystemToolArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolSystemToolArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolsetArgsDict(TypedDict):
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    etag: NotRequired[pulumi.Input[_builtins.str]]
    execution_type: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    open_api_toolsets: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolsetOpenApiToolsetArgsDict]]
        ]
    ]
    update_time: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolsetArgs:
    def __init__(
        __self__,
        *,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_type: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        open_api_toolsets: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolsetOpenApiToolsetArgs]]
            ]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionType")
    def execution_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_type.setter
    def execution_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="openApiToolsets")
    def open_api_toolsets(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolsetOpenApiToolsetArgs]]
        ]
    ]: ...
    @open_api_toolsets.setter
    def open_api_toolsets(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AppVersionSnapshotToolsetOpenApiToolsetArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolsetOpenApiToolsetArgsDict(TypedDict):
    api_authentications: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationArgsDict
                ]
            ]
        ]
    ]
    ignore_unknown_fields: NotRequired[pulumi.Input[_builtins.bool]]
    open_api_schema: NotRequired[pulumi.Input[_builtins.str]]
    service_directory_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolsetOpenApiToolsetServiceDirectoryConfigArgsDict
                ]
            ]
        ]
    ]
    tls_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotToolsetOpenApiToolsetTlsConfigArgsDict]
            ]
        ]
    ]
    url: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolsetOpenApiToolsetArgs:
    def __init__(
        __self__,
        *,
        api_authentications: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationArgs
                    ]
                ]
            ]
        ] = ...,
        ignore_unknown_fields: Optional[pulumi.Input[_builtins.bool]] = ...,
        open_api_schema: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetServiceDirectoryConfigArgs
                    ]
                ]
            ]
        ] = ...,
        tls_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotToolsetOpenApiToolsetTlsConfigArgs]
                ]
            ]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiAuthentications")
    def api_authentications(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationArgs
                ]
            ]
        ]
    ]: ...
    @api_authentications.setter
    def api_authentications(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="ignoreUnknownFields")
    def ignore_unknown_fields(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_unknown_fields.setter
    def ignore_unknown_fields(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="openApiSchema")
    def open_api_schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @open_api_schema.setter
    def open_api_schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfigs")
    def service_directory_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolsetOpenApiToolsetServiceDirectoryConfigArgs
                ]
            ]
        ]
    ]: ...
    @service_directory_configs.setter
    def service_directory_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetServiceDirectoryConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tlsConfigs")
    def tls_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[AppVersionSnapshotToolsetOpenApiToolsetTlsConfigArgs]]
        ]
    ]: ...
    @tls_configs.setter
    def tls_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[AppVersionSnapshotToolsetOpenApiToolsetTlsConfigArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationArgsDict(TypedDict):
    api_key_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationApiKeyConfigArgsDict
                ]
            ]
        ]
    ]
    bearer_token_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationBearerTokenConfigArgsDict
                ]
            ]
        ]
    ]
    oauth_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationOauthConfigArgsDict
                ]
            ]
        ]
    ]
    service_account_auth_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfigArgsDict
                ]
            ]
        ]
    ]
    service_agent_id_token_auth_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationArgs:
    def __init__(
        __self__,
        *,
        api_key_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationApiKeyConfigArgs
                    ]
                ]
            ]
        ] = ...,
        bearer_token_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationBearerTokenConfigArgs
                    ]
                ]
            ]
        ] = ...,
        oauth_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationOauthConfigArgs
                    ]
                ]
            ]
        ] = ...,
        service_account_auth_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfigArgs
                    ]
                ]
            ]
        ] = ...,
        service_agent_id_token_auth_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyConfigs")
    def api_key_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationApiKeyConfigArgs
                ]
            ]
        ]
    ]: ...
    @api_key_configs.setter
    def api_key_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationApiKeyConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bearerTokenConfigs")
    def bearer_token_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationBearerTokenConfigArgs
                ]
            ]
        ]
    ]: ...
    @bearer_token_configs.setter
    def bearer_token_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationBearerTokenConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="oauthConfigs")
    def oauth_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationOauthConfigArgs
                ]
            ]
        ]
    ]: ...
    @oauth_configs.setter
    def oauth_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationOauthConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountAuthConfigs")
    def service_account_auth_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfigArgs
                ]
            ]
        ]
    ]: ...
    @service_account_auth_configs.setter
    def service_account_auth_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAgentIdTokenAuthConfigs")
    def service_agent_id_token_auth_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgs
                ]
            ]
        ]
    ]: ...
    @service_agent_id_token_auth_configs.setter
    def service_agent_id_token_auth_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationApiKeyConfigArgsDict(
    TypedDict
):
    api_key_secret_version: NotRequired[pulumi.Input[_builtins.str]]
    key_name: NotRequired[pulumi.Input[_builtins.str]]
    request_location: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationApiKeyConfigArgs:
    def __init__(
        __self__,
        *,
        api_key_secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
        key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        request_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeySecretVersion")
    def api_key_secret_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key_secret_version.setter
    def api_key_secret_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestLocation")
    def request_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_location.setter
    def request_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationBearerTokenConfigArgsDict(
    TypedDict
):
    token: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationBearerTokenConfigArgs:
    def __init__(
        __self__, *, token: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token.setter
    def token(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationOauthConfigArgsDict(
    TypedDict
):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_version: NotRequired[pulumi.Input[_builtins.str]]
    oauth_grant_type: NotRequired[pulumi.Input[_builtins.str]]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    token_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationOauthConfigArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_grant_type: Optional[pulumi.Input[_builtins.str]] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        token_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecretVersion")
    def client_secret_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret_version.setter
    def client_secret_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthGrantType")
    def oauth_grant_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oauth_grant_type.setter
    def oauth_grant_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scopes.setter
    def scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token_endpoint.setter
    def token_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfigArgsDict(
    TypedDict
):
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfigArgs:
    def __init__(
        __self__, *, service_account: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgsDict(
    TypedDict
): ...

@pulumi.input_type
class AppVersionSnapshotToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgs:
    def __init__(__self__) -> None: ...

class AppVersionSnapshotToolsetOpenApiToolsetServiceDirectoryConfigArgsDict(TypedDict):
    service: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolsetOpenApiToolsetServiceDirectoryConfigArgs:
    def __init__(
        __self__, *, service: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class AppVersionSnapshotToolsetOpenApiToolsetTlsConfigArgsDict(TypedDict):
    ca_certs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    AppVersionSnapshotToolsetOpenApiToolsetTlsConfigCaCertArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class AppVersionSnapshotToolsetOpenApiToolsetTlsConfigArgs:
    def __init__(
        __self__,
        *,
        ca_certs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetTlsConfigCaCertArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[AppVersionSnapshotToolsetOpenApiToolsetTlsConfigCaCertArgs]
            ]
        ]
    ]: ...
    @ca_certs.setter
    def ca_certs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        AppVersionSnapshotToolsetOpenApiToolsetTlsConfigCaCertArgs
                    ]
                ]
            ]
        ],
    ): ...

class AppVersionSnapshotToolsetOpenApiToolsetTlsConfigCaCertArgsDict(TypedDict):
    cert: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class AppVersionSnapshotToolsetOpenApiToolsetTlsConfigCaCertArgs:
    def __init__(
        __self__,
        *,
        cert: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cert.setter
    def cert(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeploymentChannelProfileArgsDict(TypedDict):
    channel_type: NotRequired[pulumi.Input[_builtins.str]]
    disable_barge_in_control: NotRequired[pulumi.Input[_builtins.bool]]
    disable_dtmf: NotRequired[pulumi.Input[_builtins.bool]]
    persona_property: NotRequired[
        pulumi.Input[DeploymentChannelProfilePersonaPropertyArgsDict]
    ]
    profile_id: NotRequired[pulumi.Input[_builtins.str]]
    web_widget_config: NotRequired[
        pulumi.Input[DeploymentChannelProfileWebWidgetConfigArgsDict]
    ]
    ...

@pulumi.input_type
class DeploymentChannelProfileArgs:
    def __init__(
        __self__,
        *,
        channel_type: Optional[pulumi.Input[_builtins.str]] = ...,
        disable_barge_in_control: Optional[pulumi.Input[_builtins.bool]] = ...,
        disable_dtmf: Optional[pulumi.Input[_builtins.bool]] = ...,
        persona_property: Optional[
            pulumi.Input[DeploymentChannelProfilePersonaPropertyArgs]
        ] = ...,
        profile_id: Optional[pulumi.Input[_builtins.str]] = ...,
        web_widget_config: Optional[
            pulumi.Input[DeploymentChannelProfileWebWidgetConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="channelType")
    def channel_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @channel_type.setter
    def channel_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="disableBargeInControl")
    def disable_barge_in_control(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_barge_in_control.setter
    def disable_barge_in_control(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disableDtmf")
    def disable_dtmf(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disable_dtmf.setter
    def disable_dtmf(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="personaProperty")
    def persona_property(
        self,
    ) -> Optional[pulumi.Input[DeploymentChannelProfilePersonaPropertyArgs]]: ...
    @persona_property.setter
    def persona_property(
        self, value: Optional[pulumi.Input[DeploymentChannelProfilePersonaPropertyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="profileId")
    def profile_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @profile_id.setter
    def profile_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webWidgetConfig")
    def web_widget_config(
        self,
    ) -> Optional[pulumi.Input[DeploymentChannelProfileWebWidgetConfigArgs]]: ...
    @web_widget_config.setter
    def web_widget_config(
        self, value: Optional[pulumi.Input[DeploymentChannelProfileWebWidgetConfigArgs]]
    ): ...

class DeploymentChannelProfilePersonaPropertyArgsDict(TypedDict):
    persona: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DeploymentChannelProfilePersonaPropertyArgs:
    def __init__(
        __self__, *, persona: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def persona(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @persona.setter
    def persona(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class DeploymentChannelProfileWebWidgetConfigArgsDict(TypedDict):
    modality: NotRequired[pulumi.Input[_builtins.str]]
    theme: NotRequired[pulumi.Input[_builtins.str]]
    web_widget_title: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class DeploymentChannelProfileWebWidgetConfigArgs:
    def __init__(
        __self__,
        *,
        modality: Optional[pulumi.Input[_builtins.str]] = ...,
        theme: Optional[pulumi.Input[_builtins.str]] = ...,
        web_widget_title: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def modality(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @modality.setter
    def modality(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def theme(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @theme.setter
    def theme(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="webWidgetTitle")
    def web_widget_title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @web_widget_title.setter
    def web_widget_title(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExampleMessageArgsDict(TypedDict):
    chunks: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ExampleMessageChunkArgsDict]]]
    ]
    role: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ExampleMessageArgs:
    def __init__(
        __self__,
        *,
        chunks: Optional[
            pulumi.Input[Sequence[pulumi.Input[ExampleMessageChunkArgs]]]
        ] = ...,
        role: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def chunks(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ExampleMessageChunkArgs]]]]: ...
    @chunks.setter
    def chunks(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[ExampleMessageChunkArgs]]]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def role(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @role.setter
    def role(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExampleMessageChunkArgsDict(TypedDict):
    agent_transfer: NotRequired[pulumi.Input[ExampleMessageChunkAgentTransferArgsDict]]
    image: NotRequired[pulumi.Input[ExampleMessageChunkImageArgsDict]]
    text: NotRequired[pulumi.Input[_builtins.str]]
    tool_call: NotRequired[pulumi.Input[ExampleMessageChunkToolCallArgsDict]]
    tool_response: NotRequired[pulumi.Input[ExampleMessageChunkToolResponseArgsDict]]
    updated_variables: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ExampleMessageChunkArgs:
    def __init__(
        __self__,
        *,
        agent_transfer: Optional[
            pulumi.Input[ExampleMessageChunkAgentTransferArgs]
        ] = ...,
        image: Optional[pulumi.Input[ExampleMessageChunkImageArgs]] = ...,
        text: Optional[pulumi.Input[_builtins.str]] = ...,
        tool_call: Optional[pulumi.Input[ExampleMessageChunkToolCallArgs]] = ...,
        tool_response: Optional[
            pulumi.Input[ExampleMessageChunkToolResponseArgs]
        ] = ...,
        updated_variables: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentTransfer")
    def agent_transfer(
        self,
    ) -> Optional[pulumi.Input[ExampleMessageChunkAgentTransferArgs]]: ...
    @agent_transfer.setter
    def agent_transfer(
        self, value: Optional[pulumi.Input[ExampleMessageChunkAgentTransferArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> Optional[pulumi.Input[ExampleMessageChunkImageArgs]]: ...
    @image.setter
    def image(self, value: Optional[pulumi.Input[ExampleMessageChunkImageArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @text.setter
    def text(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="toolCall")
    def tool_call(self) -> Optional[pulumi.Input[ExampleMessageChunkToolCallArgs]]: ...
    @tool_call.setter
    def tool_call(
        self, value: Optional[pulumi.Input[ExampleMessageChunkToolCallArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="toolResponse")
    def tool_response(
        self,
    ) -> Optional[pulumi.Input[ExampleMessageChunkToolResponseArgs]]: ...
    @tool_response.setter
    def tool_response(
        self, value: Optional[pulumi.Input[ExampleMessageChunkToolResponseArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="updatedVariables")
    def updated_variables(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @updated_variables.setter
    def updated_variables(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExampleMessageChunkAgentTransferArgsDict(TypedDict):
    target_agent: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ExampleMessageChunkAgentTransferArgs:
    def __init__(
        __self__,
        *,
        target_agent: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetAgent")
    def target_agent(self) -> pulumi.Input[_builtins.str]: ...
    @target_agent.setter
    def target_agent(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExampleMessageChunkImageArgsDict(TypedDict):
    data: pulumi.Input[_builtins.str]
    mime_type: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ExampleMessageChunkImageArgs:
    def __init__(
        __self__,
        *,
        data: pulumi.Input[_builtins.str],
        mime_type: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def data(self) -> pulumi.Input[_builtins.str]: ...
    @data.setter
    def data(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mimeType")
    def mime_type(self) -> pulumi.Input[_builtins.str]: ...
    @mime_type.setter
    def mime_type(self, value: pulumi.Input[_builtins.str]): ...

class ExampleMessageChunkToolCallArgsDict(TypedDict):
    args: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    tool: NotRequired[pulumi.Input[_builtins.str]]
    toolset_tool: NotRequired[
        pulumi.Input[ExampleMessageChunkToolCallToolsetToolArgsDict]
    ]
    ...

@pulumi.input_type
class ExampleMessageChunkToolCallArgs:
    def __init__(
        __self__,
        *,
        args: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        tool: Optional[pulumi.Input[_builtins.str]] = ...,
        toolset_tool: Optional[
            pulumi.Input[ExampleMessageChunkToolCallToolsetToolArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @args.setter
    def args(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tool.setter
    def tool(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="toolsetTool")
    def toolset_tool(
        self,
    ) -> Optional[pulumi.Input[ExampleMessageChunkToolCallToolsetToolArgs]]: ...
    @toolset_tool.setter
    def toolset_tool(
        self, value: Optional[pulumi.Input[ExampleMessageChunkToolCallToolsetToolArgs]]
    ): ...

class ExampleMessageChunkToolCallToolsetToolArgsDict(TypedDict):
    toolset: pulumi.Input[_builtins.str]
    tool_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ExampleMessageChunkToolCallToolsetToolArgs:
    def __init__(
        __self__,
        *,
        toolset: pulumi.Input[_builtins.str],
        tool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def toolset(self) -> pulumi.Input[_builtins.str]: ...
    @toolset.setter
    def toolset(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="toolId")
    def tool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tool_id.setter
    def tool_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ExampleMessageChunkToolResponseArgsDict(TypedDict):
    response: pulumi.Input[_builtins.str]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    id: NotRequired[pulumi.Input[_builtins.str]]
    tool: NotRequired[pulumi.Input[_builtins.str]]
    toolset_tool: NotRequired[
        pulumi.Input[ExampleMessageChunkToolResponseToolsetToolArgsDict]
    ]
    ...

@pulumi.input_type
class ExampleMessageChunkToolResponseArgs:
    def __init__(
        __self__,
        *,
        response: pulumi.Input[_builtins.str],
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        tool: Optional[pulumi.Input[_builtins.str]] = ...,
        toolset_tool: Optional[
            pulumi.Input[ExampleMessageChunkToolResponseToolsetToolArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def response(self) -> pulumi.Input[_builtins.str]: ...
    @response.setter
    def response(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tool.setter
    def tool(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="toolsetTool")
    def toolset_tool(
        self,
    ) -> Optional[pulumi.Input[ExampleMessageChunkToolResponseToolsetToolArgs]]: ...
    @toolset_tool.setter
    def toolset_tool(
        self,
        value: Optional[pulumi.Input[ExampleMessageChunkToolResponseToolsetToolArgs]],
    ): ...

class ExampleMessageChunkToolResponseToolsetToolArgsDict(TypedDict):
    toolset: pulumi.Input[_builtins.str]
    tool_id: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ExampleMessageChunkToolResponseToolsetToolArgs:
    def __init__(
        __self__,
        *,
        toolset: pulumi.Input[_builtins.str],
        tool_id: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def toolset(self) -> pulumi.Input[_builtins.str]: ...
    @toolset.setter
    def toolset(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="toolId")
    def tool_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tool_id.setter
    def tool_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuardrailActionArgsDict(TypedDict):
    generative_answer: NotRequired[
        pulumi.Input[GuardrailActionGenerativeAnswerArgsDict]
    ]
    respond_immediately: NotRequired[
        pulumi.Input[GuardrailActionRespondImmediatelyArgsDict]
    ]
    transfer_agent: NotRequired[pulumi.Input[GuardrailActionTransferAgentArgsDict]]
    ...

@pulumi.input_type
class GuardrailActionArgs:
    def __init__(
        __self__,
        *,
        generative_answer: Optional[
            pulumi.Input[GuardrailActionGenerativeAnswerArgs]
        ] = ...,
        respond_immediately: Optional[
            pulumi.Input[GuardrailActionRespondImmediatelyArgs]
        ] = ...,
        transfer_agent: Optional[pulumi.Input[GuardrailActionTransferAgentArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="generativeAnswer")
    def generative_answer(
        self,
    ) -> Optional[pulumi.Input[GuardrailActionGenerativeAnswerArgs]]: ...
    @generative_answer.setter
    def generative_answer(
        self, value: Optional[pulumi.Input[GuardrailActionGenerativeAnswerArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="respondImmediately")
    def respond_immediately(
        self,
    ) -> Optional[pulumi.Input[GuardrailActionRespondImmediatelyArgs]]: ...
    @respond_immediately.setter
    def respond_immediately(
        self, value: Optional[pulumi.Input[GuardrailActionRespondImmediatelyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="transferAgent")
    def transfer_agent(
        self,
    ) -> Optional[pulumi.Input[GuardrailActionTransferAgentArgs]]: ...
    @transfer_agent.setter
    def transfer_agent(
        self, value: Optional[pulumi.Input[GuardrailActionTransferAgentArgs]]
    ): ...

class GuardrailActionGenerativeAnswerArgsDict(TypedDict):
    prompt: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class GuardrailActionGenerativeAnswerArgs:
    def __init__(__self__, *, prompt: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> pulumi.Input[_builtins.str]: ...
    @prompt.setter
    def prompt(self, value: pulumi.Input[_builtins.str]): ...

class GuardrailActionRespondImmediatelyArgsDict(TypedDict):
    responses: pulumi.Input[
        Sequence[pulumi.Input[GuardrailActionRespondImmediatelyResponseArgsDict]]
    ]
    ...

@pulumi.input_type
class GuardrailActionRespondImmediatelyArgs:
    def __init__(
        __self__,
        *,
        responses: pulumi.Input[
            Sequence[pulumi.Input[GuardrailActionRespondImmediatelyResponseArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def responses(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[GuardrailActionRespondImmediatelyResponseArgs]]
    ]: ...
    @responses.setter
    def responses(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[GuardrailActionRespondImmediatelyResponseArgs]]
        ],
    ): ...

class GuardrailActionRespondImmediatelyResponseArgsDict(TypedDict):
    text: pulumi.Input[_builtins.str]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class GuardrailActionRespondImmediatelyResponseArgs:
    def __init__(
        __self__,
        *,
        text: pulumi.Input[_builtins.str],
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def text(self) -> pulumi.Input[_builtins.str]: ...
    @text.setter
    def text(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class GuardrailActionTransferAgentArgsDict(TypedDict):
    agent: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class GuardrailActionTransferAgentArgs:
    def __init__(__self__, *, agent: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def agent(self) -> pulumi.Input[_builtins.str]: ...
    @agent.setter
    def agent(self, value: pulumi.Input[_builtins.str]): ...

class GuardrailCodeCallbackArgsDict(TypedDict):
    after_agent_callback: NotRequired[
        pulumi.Input[GuardrailCodeCallbackAfterAgentCallbackArgsDict]
    ]
    after_model_callback: NotRequired[
        pulumi.Input[GuardrailCodeCallbackAfterModelCallbackArgsDict]
    ]
    before_agent_callback: NotRequired[
        pulumi.Input[GuardrailCodeCallbackBeforeAgentCallbackArgsDict]
    ]
    before_model_callback: NotRequired[
        pulumi.Input[GuardrailCodeCallbackBeforeModelCallbackArgsDict]
    ]
    ...

@pulumi.input_type
class GuardrailCodeCallbackArgs:
    def __init__(
        __self__,
        *,
        after_agent_callback: Optional[
            pulumi.Input[GuardrailCodeCallbackAfterAgentCallbackArgs]
        ] = ...,
        after_model_callback: Optional[
            pulumi.Input[GuardrailCodeCallbackAfterModelCallbackArgs]
        ] = ...,
        before_agent_callback: Optional[
            pulumi.Input[GuardrailCodeCallbackBeforeAgentCallbackArgs]
        ] = ...,
        before_model_callback: Optional[
            pulumi.Input[GuardrailCodeCallbackBeforeModelCallbackArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="afterAgentCallback")
    def after_agent_callback(
        self,
    ) -> Optional[pulumi.Input[GuardrailCodeCallbackAfterAgentCallbackArgs]]: ...
    @after_agent_callback.setter
    def after_agent_callback(
        self, value: Optional[pulumi.Input[GuardrailCodeCallbackAfterAgentCallbackArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="afterModelCallback")
    def after_model_callback(
        self,
    ) -> Optional[pulumi.Input[GuardrailCodeCallbackAfterModelCallbackArgs]]: ...
    @after_model_callback.setter
    def after_model_callback(
        self, value: Optional[pulumi.Input[GuardrailCodeCallbackAfterModelCallbackArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="beforeAgentCallback")
    def before_agent_callback(
        self,
    ) -> Optional[pulumi.Input[GuardrailCodeCallbackBeforeAgentCallbackArgs]]: ...
    @before_agent_callback.setter
    def before_agent_callback(
        self,
        value: Optional[pulumi.Input[GuardrailCodeCallbackBeforeAgentCallbackArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="beforeModelCallback")
    def before_model_callback(
        self,
    ) -> Optional[pulumi.Input[GuardrailCodeCallbackBeforeModelCallbackArgs]]: ...
    @before_model_callback.setter
    def before_model_callback(
        self,
        value: Optional[pulumi.Input[GuardrailCodeCallbackBeforeModelCallbackArgs]],
    ): ...

class GuardrailCodeCallbackAfterAgentCallbackArgsDict(TypedDict):
    python_code: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class GuardrailCodeCallbackAfterAgentCallbackArgs:
    def __init__(
        __self__,
        *,
        python_code: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> pulumi.Input[_builtins.str]: ...
    @python_code.setter
    def python_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class GuardrailCodeCallbackAfterModelCallbackArgsDict(TypedDict):
    python_code: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class GuardrailCodeCallbackAfterModelCallbackArgs:
    def __init__(
        __self__,
        *,
        python_code: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> pulumi.Input[_builtins.str]: ...
    @python_code.setter
    def python_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class GuardrailCodeCallbackBeforeAgentCallbackArgsDict(TypedDict):
    python_code: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class GuardrailCodeCallbackBeforeAgentCallbackArgs:
    def __init__(
        __self__,
        *,
        python_code: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> pulumi.Input[_builtins.str]: ...
    @python_code.setter
    def python_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class GuardrailCodeCallbackBeforeModelCallbackArgsDict(TypedDict):
    python_code: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class GuardrailCodeCallbackBeforeModelCallbackArgs:
    def __init__(
        __self__,
        *,
        python_code: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> pulumi.Input[_builtins.str]: ...
    @python_code.setter
    def python_code(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class GuardrailContentFilterArgsDict(TypedDict):
    match_type: pulumi.Input[_builtins.str]
    banned_contents: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    banned_contents_in_agent_responses: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    banned_contents_in_user_inputs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ]
    disregard_diacritics: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class GuardrailContentFilterArgs:
    def __init__(
        __self__,
        *,
        match_type: pulumi.Input[_builtins.str],
        banned_contents: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        banned_contents_in_agent_responses: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        banned_contents_in_user_inputs: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        disregard_diacritics: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="matchType")
    def match_type(self) -> pulumi.Input[_builtins.str]: ...
    @match_type.setter
    def match_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="bannedContents")
    def banned_contents(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @banned_contents.setter
    def banned_contents(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bannedContentsInAgentResponses")
    def banned_contents_in_agent_responses(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @banned_contents_in_agent_responses.setter
    def banned_contents_in_agent_responses(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="bannedContentsInUserInputs")
    def banned_contents_in_user_inputs(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @banned_contents_in_user_inputs.setter
    def banned_contents_in_user_inputs(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="disregardDiacritics")
    def disregard_diacritics(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disregard_diacritics.setter
    def disregard_diacritics(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class GuardrailLlmPolicyArgsDict(TypedDict):
    policy_scope: pulumi.Input[_builtins.str]
    prompt: pulumi.Input[_builtins.str]
    allow_short_utterance: NotRequired[pulumi.Input[_builtins.bool]]
    fail_open: NotRequired[pulumi.Input[_builtins.bool]]
    max_conversation_messages: NotRequired[pulumi.Input[_builtins.int]]
    model_settings: NotRequired[pulumi.Input[GuardrailLlmPolicyModelSettingsArgsDict]]
    ...

@pulumi.input_type
class GuardrailLlmPolicyArgs:
    def __init__(
        __self__,
        *,
        policy_scope: pulumi.Input[_builtins.str],
        prompt: pulumi.Input[_builtins.str],
        allow_short_utterance: Optional[pulumi.Input[_builtins.bool]] = ...,
        fail_open: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_conversation_messages: Optional[pulumi.Input[_builtins.int]] = ...,
        model_settings: Optional[
            pulumi.Input[GuardrailLlmPolicyModelSettingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyScope")
    def policy_scope(self) -> pulumi.Input[_builtins.str]: ...
    @policy_scope.setter
    def policy_scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> pulumi.Input[_builtins.str]: ...
    @prompt.setter
    def prompt(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowShortUtterance")
    def allow_short_utterance(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_short_utterance.setter
    def allow_short_utterance(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="failOpen")
    def fail_open(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fail_open.setter
    def fail_open(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxConversationMessages")
    def max_conversation_messages(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_conversation_messages.setter
    def max_conversation_messages(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(
        self,
    ) -> Optional[pulumi.Input[GuardrailLlmPolicyModelSettingsArgs]]: ...
    @model_settings.setter
    def model_settings(
        self, value: Optional[pulumi.Input[GuardrailLlmPolicyModelSettingsArgs]]
    ): ...

class GuardrailLlmPolicyModelSettingsArgsDict(TypedDict):
    model: NotRequired[pulumi.Input[_builtins.str]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class GuardrailLlmPolicyModelSettingsArgs:
    def __init__(
        __self__,
        *,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        temperature: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class GuardrailLlmPromptSecurityArgsDict(TypedDict):
    custom_policy: NotRequired[
        pulumi.Input[GuardrailLlmPromptSecurityCustomPolicyArgsDict]
    ]
    default_settings: NotRequired[
        pulumi.Input[GuardrailLlmPromptSecurityDefaultSettingsArgsDict]
    ]
    ...

@pulumi.input_type
class GuardrailLlmPromptSecurityArgs:
    def __init__(
        __self__,
        *,
        custom_policy: Optional[
            pulumi.Input[GuardrailLlmPromptSecurityCustomPolicyArgs]
        ] = ...,
        default_settings: Optional[
            pulumi.Input[GuardrailLlmPromptSecurityDefaultSettingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="customPolicy")
    def custom_policy(
        self,
    ) -> Optional[pulumi.Input[GuardrailLlmPromptSecurityCustomPolicyArgs]]: ...
    @custom_policy.setter
    def custom_policy(
        self, value: Optional[pulumi.Input[GuardrailLlmPromptSecurityCustomPolicyArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultSettings")
    def default_settings(
        self,
    ) -> Optional[pulumi.Input[GuardrailLlmPromptSecurityDefaultSettingsArgs]]: ...
    @default_settings.setter
    def default_settings(
        self,
        value: Optional[pulumi.Input[GuardrailLlmPromptSecurityDefaultSettingsArgs]],
    ): ...

class GuardrailLlmPromptSecurityCustomPolicyArgsDict(TypedDict):
    policy_scope: pulumi.Input[_builtins.str]
    prompt: pulumi.Input[_builtins.str]
    allow_short_utterance: NotRequired[pulumi.Input[_builtins.bool]]
    fail_open: NotRequired[pulumi.Input[_builtins.bool]]
    max_conversation_messages: NotRequired[pulumi.Input[_builtins.int]]
    model_settings: NotRequired[
        pulumi.Input[GuardrailLlmPromptSecurityCustomPolicyModelSettingsArgsDict]
    ]
    ...

@pulumi.input_type
class GuardrailLlmPromptSecurityCustomPolicyArgs:
    def __init__(
        __self__,
        *,
        policy_scope: pulumi.Input[_builtins.str],
        prompt: pulumi.Input[_builtins.str],
        allow_short_utterance: Optional[pulumi.Input[_builtins.bool]] = ...,
        fail_open: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_conversation_messages: Optional[pulumi.Input[_builtins.int]] = ...,
        model_settings: Optional[
            pulumi.Input[GuardrailLlmPromptSecurityCustomPolicyModelSettingsArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="policyScope")
    def policy_scope(self) -> pulumi.Input[_builtins.str]: ...
    @policy_scope.setter
    def policy_scope(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> pulumi.Input[_builtins.str]: ...
    @prompt.setter
    def prompt(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="allowShortUtterance")
    def allow_short_utterance(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @allow_short_utterance.setter
    def allow_short_utterance(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="failOpen")
    def fail_open(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @fail_open.setter
    def fail_open(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="maxConversationMessages")
    def max_conversation_messages(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_conversation_messages.setter
    def max_conversation_messages(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(
        self,
    ) -> Optional[
        pulumi.Input[GuardrailLlmPromptSecurityCustomPolicyModelSettingsArgs]
    ]: ...
    @model_settings.setter
    def model_settings(
        self,
        value: Optional[
            pulumi.Input[GuardrailLlmPromptSecurityCustomPolicyModelSettingsArgs]
        ],
    ): ...

class GuardrailLlmPromptSecurityCustomPolicyModelSettingsArgsDict(TypedDict):
    model: NotRequired[pulumi.Input[_builtins.str]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class GuardrailLlmPromptSecurityCustomPolicyModelSettingsArgs:
    def __init__(
        __self__,
        *,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        temperature: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class GuardrailLlmPromptSecurityDefaultSettingsArgsDict(TypedDict):
    default_prompt_template: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class GuardrailLlmPromptSecurityDefaultSettingsArgs:
    def __init__(
        __self__,
        *,
        default_prompt_template: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="defaultPromptTemplate")
    def default_prompt_template(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default_prompt_template.setter
    def default_prompt_template(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GuardrailModelSafetyArgsDict(TypedDict):
    safety_settings: pulumi.Input[
        Sequence[pulumi.Input[GuardrailModelSafetySafetySettingArgsDict]]
    ]
    ...

@pulumi.input_type
class GuardrailModelSafetyArgs:
    def __init__(
        __self__,
        *,
        safety_settings: pulumi.Input[
            Sequence[pulumi.Input[GuardrailModelSafetySafetySettingArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="safetySettings")
    def safety_settings(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[GuardrailModelSafetySafetySettingArgs]]
    ]: ...
    @safety_settings.setter
    def safety_settings(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[GuardrailModelSafetySafetySettingArgs]]
        ],
    ): ...

class GuardrailModelSafetySafetySettingArgsDict(TypedDict):
    category: pulumi.Input[_builtins.str]
    threshold: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class GuardrailModelSafetySafetySettingArgs:
    def __init__(
        __self__,
        *,
        category: pulumi.Input[_builtins.str],
        threshold: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def category(self) -> pulumi.Input[_builtins.str]: ...
    @category.setter
    def category(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def threshold(self) -> pulumi.Input[_builtins.str]: ...
    @threshold.setter
    def threshold(self, value: pulumi.Input[_builtins.str]): ...

class ToolClientFunctionArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]
    parameters: NotRequired[pulumi.Input[ToolClientFunctionParametersArgsDict]]
    response: NotRequired[pulumi.Input[ToolClientFunctionResponseArgsDict]]
    ...

@pulumi.input_type
class ToolClientFunctionArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        parameters: Optional[pulumi.Input[ToolClientFunctionParametersArgs]] = ...,
        response: Optional[pulumi.Input[ToolClientFunctionResponseArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(
        self,
    ) -> Optional[pulumi.Input[ToolClientFunctionParametersArgs]]: ...
    @parameters.setter
    def parameters(
        self, value: Optional[pulumi.Input[ToolClientFunctionParametersArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def response(self) -> Optional[pulumi.Input[ToolClientFunctionResponseArgs]]: ...
    @response.setter
    def response(
        self, value: Optional[pulumi.Input[ToolClientFunctionResponseArgs]]
    ): ...

class ToolClientFunctionParametersArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    additional_properties: NotRequired[pulumi.Input[_builtins.str]]
    any_of: NotRequired[pulumi.Input[_builtins.str]]
    default: NotRequired[pulumi.Input[_builtins.str]]
    defs: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    enums: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    items: NotRequired[pulumi.Input[_builtins.str]]
    max_items: NotRequired[pulumi.Input[_builtins.int]]
    maximum: NotRequired[pulumi.Input[_builtins.float]]
    min_items: NotRequired[pulumi.Input[_builtins.int]]
    minimum: NotRequired[pulumi.Input[_builtins.float]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    prefix_items: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[_builtins.str]]
    ref: NotRequired[pulumi.Input[_builtins.str]]
    requireds: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    title: NotRequired[pulumi.Input[_builtins.str]]
    unique_items: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class ToolClientFunctionParametersArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        additional_properties: Optional[pulumi.Input[_builtins.str]] = ...,
        any_of: Optional[pulumi.Input[_builtins.str]] = ...,
        default: Optional[pulumi.Input[_builtins.str]] = ...,
        defs: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enums: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        items: Optional[pulumi.Input[_builtins.str]] = ...,
        max_items: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum: Optional[pulumi.Input[_builtins.float]] = ...,
        min_items: Optional[pulumi.Input[_builtins.int]] = ...,
        minimum: Optional[pulumi.Input[_builtins.float]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        prefix_items: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[_builtins.str]] = ...,
        ref: Optional[pulumi.Input[_builtins.str]] = ...,
        requireds: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
        unique_items: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_properties.setter
    def additional_properties(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @any_of.setter
    def any_of(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default.setter
    def default(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def defs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @defs.setter
    def defs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enums(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enums.setter
    def enums(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items.setter
    def items(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxItems")
    def max_items(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_items.setter
    def max_items(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @maximum.setter
    def maximum(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="minItems")
    def min_items(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_items.setter
    def min_items(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @minimum.setter
    def minimum(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixItems")
    def prefix_items(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix_items.setter
    def prefix_items(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ref.setter
    def ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def requireds(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @requireds.setter
    def requireds(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="uniqueItems")
    def unique_items(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @unique_items.setter
    def unique_items(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ToolClientFunctionResponseArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    additional_properties: NotRequired[pulumi.Input[_builtins.str]]
    any_of: NotRequired[pulumi.Input[_builtins.str]]
    default: NotRequired[pulumi.Input[_builtins.str]]
    defs: NotRequired[pulumi.Input[_builtins.str]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    enums: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    items: NotRequired[pulumi.Input[_builtins.str]]
    max_items: NotRequired[pulumi.Input[_builtins.int]]
    maximum: NotRequired[pulumi.Input[_builtins.float]]
    min_items: NotRequired[pulumi.Input[_builtins.int]]
    minimum: NotRequired[pulumi.Input[_builtins.float]]
    nullable: NotRequired[pulumi.Input[_builtins.bool]]
    prefix_items: NotRequired[pulumi.Input[_builtins.str]]
    properties: NotRequired[pulumi.Input[_builtins.str]]
    ref: NotRequired[pulumi.Input[_builtins.str]]
    requireds: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    title: NotRequired[pulumi.Input[_builtins.str]]
    unique_items: NotRequired[pulumi.Input[_builtins.bool]]
    ...

@pulumi.input_type
class ToolClientFunctionResponseArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        additional_properties: Optional[pulumi.Input[_builtins.str]] = ...,
        any_of: Optional[pulumi.Input[_builtins.str]] = ...,
        default: Optional[pulumi.Input[_builtins.str]] = ...,
        defs: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        enums: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        items: Optional[pulumi.Input[_builtins.str]] = ...,
        max_items: Optional[pulumi.Input[_builtins.int]] = ...,
        maximum: Optional[pulumi.Input[_builtins.float]] = ...,
        min_items: Optional[pulumi.Input[_builtins.int]] = ...,
        minimum: Optional[pulumi.Input[_builtins.float]] = ...,
        nullable: Optional[pulumi.Input[_builtins.bool]] = ...,
        prefix_items: Optional[pulumi.Input[_builtins.str]] = ...,
        properties: Optional[pulumi.Input[_builtins.str]] = ...,
        ref: Optional[pulumi.Input[_builtins.str]] = ...,
        requireds: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        title: Optional[pulumi.Input[_builtins.str]] = ...,
        unique_items: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="additionalProperties")
    def additional_properties(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @additional_properties.setter
    def additional_properties(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="anyOf")
    def any_of(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @any_of.setter
    def any_of(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def default(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @default.setter
    def default(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def defs(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @defs.setter
    def defs(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def enums(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @enums.setter
    def enums(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def items(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @items.setter
    def items(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="maxItems")
    def max_items(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_items.setter
    def max_items(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def maximum(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @maximum.setter
    def maximum(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="minItems")
    def min_items(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_items.setter
    def min_items(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def minimum(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @minimum.setter
    def minimum(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter
    def nullable(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @nullable.setter
    def nullable(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="prefixItems")
    def prefix_items(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prefix_items.setter
    def prefix_items(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @properties.setter
    def properties(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ref(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ref.setter
    def ref(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def requireds(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @requireds.setter
    def requireds(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @title.setter
    def title(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="uniqueItems")
    def unique_items(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @unique_items.setter
    def unique_items(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ToolDataStoreToolArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    boost_specs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ToolDataStoreToolBoostSpecArgsDict]]]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    engine_source: NotRequired[pulumi.Input[ToolDataStoreToolEngineSourceArgsDict]]
    max_results: NotRequired[pulumi.Input[_builtins.int]]
    modality_configs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ToolDataStoreToolModalityConfigArgsDict]]]
    ]
    ...

@pulumi.input_type
class ToolDataStoreToolArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        boost_specs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ToolDataStoreToolBoostSpecArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        engine_source: Optional[pulumi.Input[ToolDataStoreToolEngineSourceArgs]] = ...,
        max_results: Optional[pulumi.Input[_builtins.int]] = ...,
        modality_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ToolDataStoreToolModalityConfigArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="boostSpecs")
    def boost_specs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ToolDataStoreToolBoostSpecArgs]]]
    ]: ...
    @boost_specs.setter
    def boost_specs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ToolDataStoreToolBoostSpecArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="engineSource")
    def engine_source(
        self,
    ) -> Optional[pulumi.Input[ToolDataStoreToolEngineSourceArgs]]: ...
    @engine_source.setter
    def engine_source(
        self, value: Optional[pulumi.Input[ToolDataStoreToolEngineSourceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxResults")
    def max_results(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_results.setter
    def max_results(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="modalityConfigs")
    def modality_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ToolDataStoreToolModalityConfigArgs]]]
    ]: ...
    @modality_configs.setter
    def modality_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ToolDataStoreToolModalityConfigArgs]]]
        ],
    ): ...

class ToolDataStoreToolBoostSpecArgsDict(TypedDict):
    data_stores: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    specs: pulumi.Input[Sequence[pulumi.Input[ToolDataStoreToolBoostSpecSpecArgsDict]]]
    ...

@pulumi.input_type
class ToolDataStoreToolBoostSpecArgs:
    def __init__(
        __self__,
        *,
        data_stores: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        specs: pulumi.Input[Sequence[pulumi.Input[ToolDataStoreToolBoostSpecSpecArgs]]],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStores")
    def data_stores(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @data_stores.setter
    def data_stores(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def specs(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ToolDataStoreToolBoostSpecSpecArgs]]]: ...
    @specs.setter
    def specs(
        self,
        value: pulumi.Input[Sequence[pulumi.Input[ToolDataStoreToolBoostSpecSpecArgs]]],
    ): ...

class ToolDataStoreToolBoostSpecSpecArgsDict(TypedDict):
    condition_boost_specs: pulumi.Input[
        Sequence[pulumi.Input[ToolDataStoreToolBoostSpecSpecConditionBoostSpecArgsDict]]
    ]
    ...

@pulumi.input_type
class ToolDataStoreToolBoostSpecSpecArgs:
    def __init__(
        __self__,
        *,
        condition_boost_specs: pulumi.Input[
            Sequence[pulumi.Input[ToolDataStoreToolBoostSpecSpecConditionBoostSpecArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="conditionBoostSpecs")
    def condition_boost_specs(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ToolDataStoreToolBoostSpecSpecConditionBoostSpecArgs]]
    ]: ...
    @condition_boost_specs.setter
    def condition_boost_specs(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ToolDataStoreToolBoostSpecSpecConditionBoostSpecArgs]]
        ],
    ): ...

class ToolDataStoreToolBoostSpecSpecConditionBoostSpecArgsDict(TypedDict):
    condition: pulumi.Input[_builtins.str]
    boost: NotRequired[pulumi.Input[_builtins.float]]
    boost_control_spec: NotRequired[
        pulumi.Input[
            ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecArgsDict
        ]
    ]
    ...

@pulumi.input_type
class ToolDataStoreToolBoostSpecSpecConditionBoostSpecArgs:
    def __init__(
        __self__,
        *,
        condition: pulumi.Input[_builtins.str],
        boost: Optional[pulumi.Input[_builtins.float]] = ...,
        boost_control_spec: Optional[
            pulumi.Input[
                ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def condition(self) -> pulumi.Input[_builtins.str]: ...
    @condition.setter
    def condition(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def boost(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @boost.setter
    def boost(self, value: Optional[pulumi.Input[_builtins.float]]): ...
    @_builtins.property
    @pulumi.getter(name="boostControlSpec")
    def boost_control_spec(
        self,
    ) -> Optional[
        pulumi.Input[
            ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecArgs
        ]
    ]: ...
    @boost_control_spec.setter
    def boost_control_spec(
        self,
        value: Optional[
            pulumi.Input[
                ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecArgs
            ]
        ],
    ): ...

class ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecArgsDict(
    TypedDict
):
    attribute_type: NotRequired[pulumi.Input[_builtins.str]]
    control_points: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPointArgsDict
                ]
            ]
        ]
    ]
    field_name: NotRequired[pulumi.Input[_builtins.str]]
    interpolation_type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecArgs:
    def __init__(
        __self__,
        *,
        attribute_type: Optional[pulumi.Input[_builtins.str]] = ...,
        control_points: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPointArgs
                    ]
                ]
            ]
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
    @pulumi.getter(name="controlPoints")
    def control_points(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPointArgs
                ]
            ]
        ]
    ]: ...
    @control_points.setter
    def control_points(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPointArgs
                    ]
                ]
            ]
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

class ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPointArgsDict(
    TypedDict
):
    attribute_value: NotRequired[pulumi.Input[_builtins.str]]
    boost_amount: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class ToolDataStoreToolBoostSpecSpecConditionBoostSpecBoostControlSpecControlPointArgs:
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

class ToolDataStoreToolEngineSourceArgsDict(TypedDict):
    engine: pulumi.Input[_builtins.str]
    data_store_sources: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ToolDataStoreToolEngineSourceDataStoreSourceArgsDict]]
        ]
    ]
    filter: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolDataStoreToolEngineSourceArgs:
    def __init__(
        __self__,
        *,
        engine: pulumi.Input[_builtins.str],
        data_store_sources: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ToolDataStoreToolEngineSourceDataStoreSourceArgs]]
            ]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def engine(self) -> pulumi.Input[_builtins.str]: ...
    @engine.setter
    def engine(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="dataStoreSources")
    def data_store_sources(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ToolDataStoreToolEngineSourceDataStoreSourceArgs]]
        ]
    ]: ...
    @data_store_sources.setter
    def data_store_sources(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ToolDataStoreToolEngineSourceDataStoreSourceArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolDataStoreToolEngineSourceDataStoreSourceArgsDict(TypedDict):
    data_store: NotRequired[
        pulumi.Input[ToolDataStoreToolEngineSourceDataStoreSourceDataStoreArgsDict]
    ]
    filter: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolDataStoreToolEngineSourceDataStoreSourceArgs:
    def __init__(
        __self__,
        *,
        data_store: Optional[
            pulumi.Input[ToolDataStoreToolEngineSourceDataStoreSourceDataStoreArgs]
        ] = ...,
        filter: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="dataStore")
    def data_store(
        self,
    ) -> Optional[
        pulumi.Input[ToolDataStoreToolEngineSourceDataStoreSourceDataStoreArgs]
    ]: ...
    @data_store.setter
    def data_store(
        self,
        value: Optional[
            pulumi.Input[ToolDataStoreToolEngineSourceDataStoreSourceDataStoreArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @filter.setter
    def filter(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolDataStoreToolEngineSourceDataStoreSourceDataStoreArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    connector_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfigArgsDict
                ]
            ]
        ]
    ]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    document_processing_mode: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolDataStoreToolEngineSourceDataStoreSourceDataStoreArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        connector_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfigArgs
                    ]
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        document_processing_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="connectorConfigs")
    def connector_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfigArgs
                ]
            ]
        ]
    ]: ...
    @connector_configs.setter
    def connector_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="documentProcessingMode")
    def document_processing_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @document_processing_mode.setter
    def document_processing_mode(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfigArgsDict(
    TypedDict
):
    collection: NotRequired[pulumi.Input[_builtins.str]]
    collection_display_name: NotRequired[pulumi.Input[_builtins.str]]
    data_source: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolDataStoreToolEngineSourceDataStoreSourceDataStoreConnectorConfigArgs:
    def __init__(
        __self__,
        *,
        collection: Optional[pulumi.Input[_builtins.str]] = ...,
        collection_display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        data_source: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def collection(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collection.setter
    def collection(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="collectionDisplayName")
    def collection_display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @collection_display_name.setter
    def collection_display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="dataSource")
    def data_source(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @data_source.setter
    def data_source(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolDataStoreToolModalityConfigArgsDict(TypedDict):
    modality_type: pulumi.Input[_builtins.str]
    grounding_config: NotRequired[
        pulumi.Input[ToolDataStoreToolModalityConfigGroundingConfigArgsDict]
    ]
    rewriter_config: NotRequired[
        pulumi.Input[ToolDataStoreToolModalityConfigRewriterConfigArgsDict]
    ]
    summarization_config: NotRequired[
        pulumi.Input[ToolDataStoreToolModalityConfigSummarizationConfigArgsDict]
    ]
    ...

@pulumi.input_type
class ToolDataStoreToolModalityConfigArgs:
    def __init__(
        __self__,
        *,
        modality_type: pulumi.Input[_builtins.str],
        grounding_config: Optional[
            pulumi.Input[ToolDataStoreToolModalityConfigGroundingConfigArgs]
        ] = ...,
        rewriter_config: Optional[
            pulumi.Input[ToolDataStoreToolModalityConfigRewriterConfigArgs]
        ] = ...,
        summarization_config: Optional[
            pulumi.Input[ToolDataStoreToolModalityConfigSummarizationConfigArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modalityType")
    def modality_type(self) -> pulumi.Input[_builtins.str]: ...
    @modality_type.setter
    def modality_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="groundingConfig")
    def grounding_config(
        self,
    ) -> Optional[pulumi.Input[ToolDataStoreToolModalityConfigGroundingConfigArgs]]: ...
    @grounding_config.setter
    def grounding_config(
        self,
        value: Optional[
            pulumi.Input[ToolDataStoreToolModalityConfigGroundingConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="rewriterConfig")
    def rewriter_config(
        self,
    ) -> Optional[pulumi.Input[ToolDataStoreToolModalityConfigRewriterConfigArgs]]: ...
    @rewriter_config.setter
    def rewriter_config(
        self,
        value: Optional[
            pulumi.Input[ToolDataStoreToolModalityConfigRewriterConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="summarizationConfig")
    def summarization_config(
        self,
    ) -> Optional[
        pulumi.Input[ToolDataStoreToolModalityConfigSummarizationConfigArgs]
    ]: ...
    @summarization_config.setter
    def summarization_config(
        self,
        value: Optional[
            pulumi.Input[ToolDataStoreToolModalityConfigSummarizationConfigArgs]
        ],
    ): ...

class ToolDataStoreToolModalityConfigGroundingConfigArgsDict(TypedDict):
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    grounding_level: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class ToolDataStoreToolModalityConfigGroundingConfigArgs:
    def __init__(
        __self__,
        *,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        grounding_level: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="groundingLevel")
    def grounding_level(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @grounding_level.setter
    def grounding_level(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ToolDataStoreToolModalityConfigRewriterConfigArgsDict(TypedDict):
    model_settings: pulumi.Input[
        ToolDataStoreToolModalityConfigRewriterConfigModelSettingsArgsDict
    ]
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    prompt: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolDataStoreToolModalityConfigRewriterConfigArgs:
    def __init__(
        __self__,
        *,
        model_settings: pulumi.Input[
            ToolDataStoreToolModalityConfigRewriterConfigModelSettingsArgs
        ],
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        prompt: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(
        self,
    ) -> pulumi.Input[
        ToolDataStoreToolModalityConfigRewriterConfigModelSettingsArgs
    ]: ...
    @model_settings.setter
    def model_settings(
        self,
        value: pulumi.Input[
            ToolDataStoreToolModalityConfigRewriterConfigModelSettingsArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prompt.setter
    def prompt(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolDataStoreToolModalityConfigRewriterConfigModelSettingsArgsDict(TypedDict):
    model: NotRequired[pulumi.Input[_builtins.str]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class ToolDataStoreToolModalityConfigRewriterConfigModelSettingsArgs:
    def __init__(
        __self__,
        *,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        temperature: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ToolDataStoreToolModalityConfigSummarizationConfigArgsDict(TypedDict):
    disabled: NotRequired[pulumi.Input[_builtins.bool]]
    model_settings: NotRequired[
        pulumi.Input[
            ToolDataStoreToolModalityConfigSummarizationConfigModelSettingsArgsDict
        ]
    ]
    prompt: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolDataStoreToolModalityConfigSummarizationConfigArgs:
    def __init__(
        __self__,
        *,
        disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        model_settings: Optional[
            pulumi.Input[
                ToolDataStoreToolModalityConfigSummarizationConfigModelSettingsArgs
            ]
        ] = ...,
        prompt: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @disabled.setter
    def disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(
        self,
    ) -> Optional[
        pulumi.Input[
            ToolDataStoreToolModalityConfigSummarizationConfigModelSettingsArgs
        ]
    ]: ...
    @model_settings.setter
    def model_settings(
        self,
        value: Optional[
            pulumi.Input[
                ToolDataStoreToolModalityConfigSummarizationConfigModelSettingsArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def prompt(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @prompt.setter
    def prompt(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolDataStoreToolModalityConfigSummarizationConfigModelSettingsArgsDict(
    TypedDict
):
    model: NotRequired[pulumi.Input[_builtins.str]]
    temperature: NotRequired[pulumi.Input[_builtins.float]]
    ...

@pulumi.input_type
class ToolDataStoreToolModalityConfigSummarizationConfigModelSettingsArgs:
    def __init__(
        __self__,
        *,
        model: Optional[pulumi.Input[_builtins.str]] = ...,
        temperature: Optional[pulumi.Input[_builtins.float]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def model(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @model.setter
    def model(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def temperature(self) -> Optional[pulumi.Input[_builtins.float]]: ...
    @temperature.setter
    def temperature(self, value: Optional[pulumi.Input[_builtins.float]]): ...

class ToolGoogleSearchToolArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    context_urls: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    description: NotRequired[pulumi.Input[_builtins.str]]
    exclude_domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    preferred_domains: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ToolGoogleSearchToolArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        context_urls: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        exclude_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        preferred_domains: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="contextUrls")
    def context_urls(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @context_urls.setter
    def context_urls(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="excludeDomains")
    def exclude_domains(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @exclude_domains.setter
    def exclude_domains(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="preferredDomains")
    def preferred_domains(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @preferred_domains.setter
    def preferred_domains(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ToolOpenApiToolArgsDict(TypedDict):
    api_authentications: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolApiAuthenticationArgsDict]]]
    ]
    description: NotRequired[pulumi.Input[_builtins.str]]
    ignore_unknown_fields: NotRequired[pulumi.Input[_builtins.bool]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    open_api_schema: NotRequired[pulumi.Input[_builtins.str]]
    service_directory_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ToolOpenApiToolServiceDirectoryConfigArgsDict]]
        ]
    ]
    tls_configs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolTlsConfigArgsDict]]]
    ]
    url: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolOpenApiToolArgs:
    def __init__(
        __self__,
        *,
        api_authentications: Optional[
            pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolApiAuthenticationArgs]]]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        ignore_unknown_fields: Optional[pulumi.Input[_builtins.bool]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        open_api_schema: Optional[pulumi.Input[_builtins.str]] = ...,
        service_directory_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ToolOpenApiToolServiceDirectoryConfigArgs]]
            ]
        ] = ...,
        tls_configs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolTlsConfigArgs]]]
        ] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiAuthentications")
    def api_authentications(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolApiAuthenticationArgs]]]
    ]: ...
    @api_authentications.setter
    def api_authentications(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolApiAuthenticationArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ignoreUnknownFields")
    def ignore_unknown_fields(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_unknown_fields.setter
    def ignore_unknown_fields(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="openApiSchema")
    def open_api_schema(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @open_api_schema.setter
    def open_api_schema(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfigs")
    def service_directory_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolServiceDirectoryConfigArgs]]]
    ]: ...
    @service_directory_configs.setter
    def service_directory_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ToolOpenApiToolServiceDirectoryConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tlsConfigs")
    def tls_configs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolTlsConfigArgs]]]
    ]: ...
    @tls_configs.setter
    def tls_configs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolTlsConfigArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolOpenApiToolApiAuthenticationArgsDict(TypedDict):
    api_key_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ToolOpenApiToolApiAuthenticationApiKeyConfigArgsDict]]
        ]
    ]
    bearer_token_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[ToolOpenApiToolApiAuthenticationBearerTokenConfigArgsDict]
            ]
        ]
    ]
    oauth_configs: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ToolOpenApiToolApiAuthenticationOauthConfigArgsDict]]
        ]
    ]
    service_account_auth_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ToolOpenApiToolApiAuthenticationServiceAccountAuthConfigArgsDict
                ]
            ]
        ]
    ]
    service_agent_id_token_auth_configs: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfigArgsDict
                ]
            ]
        ]
    ]
    ...

@pulumi.input_type
class ToolOpenApiToolApiAuthenticationArgs:
    def __init__(
        __self__,
        *,
        api_key_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ToolOpenApiToolApiAuthenticationApiKeyConfigArgs]]
            ]
        ] = ...,
        bearer_token_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ToolOpenApiToolApiAuthenticationBearerTokenConfigArgs]
                ]
            ]
        ] = ...,
        oauth_configs: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ToolOpenApiToolApiAuthenticationOauthConfigArgs]]
            ]
        ] = ...,
        service_account_auth_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ToolOpenApiToolApiAuthenticationServiceAccountAuthConfigArgs
                    ]
                ]
            ]
        ] = ...,
        service_agent_id_token_auth_configs: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfigArgs
                    ]
                ]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyConfigs")
    def api_key_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ToolOpenApiToolApiAuthenticationApiKeyConfigArgs]]
        ]
    ]: ...
    @api_key_configs.setter
    def api_key_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ToolOpenApiToolApiAuthenticationApiKeyConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bearerTokenConfigs")
    def bearer_token_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ToolOpenApiToolApiAuthenticationBearerTokenConfigArgs]
            ]
        ]
    ]: ...
    @bearer_token_configs.setter
    def bearer_token_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[ToolOpenApiToolApiAuthenticationBearerTokenConfigArgs]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="oauthConfigs")
    def oauth_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ToolOpenApiToolApiAuthenticationOauthConfigArgs]]
        ]
    ]: ...
    @oauth_configs.setter
    def oauth_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ToolOpenApiToolApiAuthenticationOauthConfigArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountAuthConfigs")
    def service_account_auth_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ToolOpenApiToolApiAuthenticationServiceAccountAuthConfigArgs
                ]
            ]
        ]
    ]: ...
    @service_account_auth_configs.setter
    def service_account_auth_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ToolOpenApiToolApiAuthenticationServiceAccountAuthConfigArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAgentIdTokenAuthConfigs")
    def service_agent_id_token_auth_configs(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfigArgs
                ]
            ]
        ]
    ]: ...
    @service_agent_id_token_auth_configs.setter
    def service_agent_id_token_auth_configs(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfigArgs
                    ]
                ]
            ]
        ],
    ): ...

class ToolOpenApiToolApiAuthenticationApiKeyConfigArgsDict(TypedDict):
    api_key_secret_version: NotRequired[pulumi.Input[_builtins.str]]
    key_name: NotRequired[pulumi.Input[_builtins.str]]
    request_location: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolOpenApiToolApiAuthenticationApiKeyConfigArgs:
    def __init__(
        __self__,
        *,
        api_key_secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
        key_name: Optional[pulumi.Input[_builtins.str]] = ...,
        request_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeySecretVersion")
    def api_key_secret_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @api_key_secret_version.setter
    def api_key_secret_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @key_name.setter
    def key_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requestLocation")
    def request_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @request_location.setter
    def request_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolOpenApiToolApiAuthenticationBearerTokenConfigArgsDict(TypedDict):
    token: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolOpenApiToolApiAuthenticationBearerTokenConfigArgs:
    def __init__(
        __self__, *, token: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token.setter
    def token(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolOpenApiToolApiAuthenticationOauthConfigArgsDict(TypedDict):
    client_id: NotRequired[pulumi.Input[_builtins.str]]
    client_secret_version: NotRequired[pulumi.Input[_builtins.str]]
    oauth_grant_type: NotRequired[pulumi.Input[_builtins.str]]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    token_endpoint: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolOpenApiToolApiAuthenticationOauthConfigArgs:
    def __init__(
        __self__,
        *,
        client_id: Optional[pulumi.Input[_builtins.str]] = ...,
        client_secret_version: Optional[pulumi.Input[_builtins.str]] = ...,
        oauth_grant_type: Optional[pulumi.Input[_builtins.str]] = ...,
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        token_endpoint: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_id.setter
    def client_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecretVersion")
    def client_secret_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @client_secret_version.setter
    def client_secret_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="oauthGrantType")
    def oauth_grant_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @oauth_grant_type.setter
    def oauth_grant_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scopes.setter
    def scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token_endpoint.setter
    def token_endpoint(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolOpenApiToolApiAuthenticationServiceAccountAuthConfigArgsDict(TypedDict):
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolOpenApiToolApiAuthenticationServiceAccountAuthConfigArgs:
    def __init__(
        __self__, *, service_account: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfigArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ToolOpenApiToolApiAuthenticationServiceAgentIdTokenAuthConfigArgs:
    def __init__(__self__) -> None: ...

class ToolOpenApiToolServiceDirectoryConfigArgsDict(TypedDict):
    service: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolOpenApiToolServiceDirectoryConfigArgs:
    def __init__(
        __self__, *, service: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolOpenApiToolTlsConfigArgsDict(TypedDict):
    ca_certs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolTlsConfigCaCertArgsDict]]]
    ]
    ...

@pulumi.input_type
class ToolOpenApiToolTlsConfigArgs:
    def __init__(
        __self__,
        *,
        ca_certs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolTlsConfigCaCertArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolTlsConfigCaCertArgs]]]
    ]: ...
    @ca_certs.setter
    def ca_certs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ToolOpenApiToolTlsConfigCaCertArgs]]]
        ],
    ): ...

class ToolOpenApiToolTlsConfigCaCertArgsDict(TypedDict):
    cert: NotRequired[pulumi.Input[_builtins.str]]
    display_name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolOpenApiToolTlsConfigCaCertArgs:
    def __init__(
        __self__,
        *,
        cert: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cert.setter
    def cert(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolPythonFunctionArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    python_code: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolPythonFunctionArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        python_code: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pythonCode")
    def python_code(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @python_code.setter
    def python_code(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolSystemToolArgsDict(TypedDict):
    description: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolSystemToolArgs:
    def __init__(
        __self__,
        *,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolsetMcpToolsetArgsDict(TypedDict):
    server_address: pulumi.Input[_builtins.str]
    api_authentication: NotRequired[
        pulumi.Input[ToolsetMcpToolsetApiAuthenticationArgsDict]
    ]
    service_directory_config: NotRequired[
        pulumi.Input[ToolsetMcpToolsetServiceDirectoryConfigArgsDict]
    ]
    tls_config: NotRequired[pulumi.Input[ToolsetMcpToolsetTlsConfigArgsDict]]
    ...

@pulumi.input_type
class ToolsetMcpToolsetArgs:
    def __init__(
        __self__,
        *,
        server_address: pulumi.Input[_builtins.str],
        api_authentication: Optional[
            pulumi.Input[ToolsetMcpToolsetApiAuthenticationArgs]
        ] = ...,
        service_directory_config: Optional[
            pulumi.Input[ToolsetMcpToolsetServiceDirectoryConfigArgs]
        ] = ...,
        tls_config: Optional[pulumi.Input[ToolsetMcpToolsetTlsConfigArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serverAddress")
    def server_address(self) -> pulumi.Input[_builtins.str]: ...
    @server_address.setter
    def server_address(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="apiAuthentication")
    def api_authentication(
        self,
    ) -> Optional[pulumi.Input[ToolsetMcpToolsetApiAuthenticationArgs]]: ...
    @api_authentication.setter
    def api_authentication(
        self, value: Optional[pulumi.Input[ToolsetMcpToolsetApiAuthenticationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(
        self,
    ) -> Optional[pulumi.Input[ToolsetMcpToolsetServiceDirectoryConfigArgs]]: ...
    @service_directory_config.setter
    def service_directory_config(
        self, value: Optional[pulumi.Input[ToolsetMcpToolsetServiceDirectoryConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(self) -> Optional[pulumi.Input[ToolsetMcpToolsetTlsConfigArgs]]: ...
    @tls_config.setter
    def tls_config(
        self, value: Optional[pulumi.Input[ToolsetMcpToolsetTlsConfigArgs]]
    ): ...

class ToolsetMcpToolsetApiAuthenticationArgsDict(TypedDict):
    api_key_config: NotRequired[
        pulumi.Input[ToolsetMcpToolsetApiAuthenticationApiKeyConfigArgsDict]
    ]
    bearer_token_config: NotRequired[
        pulumi.Input[ToolsetMcpToolsetApiAuthenticationBearerTokenConfigArgsDict]
    ]
    oauth_config: NotRequired[
        pulumi.Input[ToolsetMcpToolsetApiAuthenticationOauthConfigArgsDict]
    ]
    service_account_auth_config: NotRequired[
        pulumi.Input[ToolsetMcpToolsetApiAuthenticationServiceAccountAuthConfigArgsDict]
    ]
    service_agent_id_token_auth_config: NotRequired[
        pulumi.Input[
            ToolsetMcpToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgsDict
        ]
    ]
    ...

@pulumi.input_type
class ToolsetMcpToolsetApiAuthenticationArgs:
    def __init__(
        __self__,
        *,
        api_key_config: Optional[
            pulumi.Input[ToolsetMcpToolsetApiAuthenticationApiKeyConfigArgs]
        ] = ...,
        bearer_token_config: Optional[
            pulumi.Input[ToolsetMcpToolsetApiAuthenticationBearerTokenConfigArgs]
        ] = ...,
        oauth_config: Optional[
            pulumi.Input[ToolsetMcpToolsetApiAuthenticationOauthConfigArgs]
        ] = ...,
        service_account_auth_config: Optional[
            pulumi.Input[ToolsetMcpToolsetApiAuthenticationServiceAccountAuthConfigArgs]
        ] = ...,
        service_agent_id_token_auth_config: Optional[
            pulumi.Input[
                ToolsetMcpToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyConfig")
    def api_key_config(
        self,
    ) -> Optional[pulumi.Input[ToolsetMcpToolsetApiAuthenticationApiKeyConfigArgs]]: ...
    @api_key_config.setter
    def api_key_config(
        self,
        value: Optional[
            pulumi.Input[ToolsetMcpToolsetApiAuthenticationApiKeyConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bearerTokenConfig")
    def bearer_token_config(
        self,
    ) -> Optional[
        pulumi.Input[ToolsetMcpToolsetApiAuthenticationBearerTokenConfigArgs]
    ]: ...
    @bearer_token_config.setter
    def bearer_token_config(
        self,
        value: Optional[
            pulumi.Input[ToolsetMcpToolsetApiAuthenticationBearerTokenConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="oauthConfig")
    def oauth_config(
        self,
    ) -> Optional[pulumi.Input[ToolsetMcpToolsetApiAuthenticationOauthConfigArgs]]: ...
    @oauth_config.setter
    def oauth_config(
        self,
        value: Optional[
            pulumi.Input[ToolsetMcpToolsetApiAuthenticationOauthConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountAuthConfig")
    def service_account_auth_config(
        self,
    ) -> Optional[
        pulumi.Input[ToolsetMcpToolsetApiAuthenticationServiceAccountAuthConfigArgs]
    ]: ...
    @service_account_auth_config.setter
    def service_account_auth_config(
        self,
        value: Optional[
            pulumi.Input[ToolsetMcpToolsetApiAuthenticationServiceAccountAuthConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAgentIdTokenAuthConfig")
    def service_agent_id_token_auth_config(
        self,
    ) -> Optional[
        pulumi.Input[
            ToolsetMcpToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgs
        ]
    ]: ...
    @service_agent_id_token_auth_config.setter
    def service_agent_id_token_auth_config(
        self,
        value: Optional[
            pulumi.Input[
                ToolsetMcpToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgs
            ]
        ],
    ): ...

class ToolsetMcpToolsetApiAuthenticationApiKeyConfigArgsDict(TypedDict):
    api_key_secret_version: pulumi.Input[_builtins.str]
    key_name: pulumi.Input[_builtins.str]
    request_location: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ToolsetMcpToolsetApiAuthenticationApiKeyConfigArgs:
    def __init__(
        __self__,
        *,
        api_key_secret_version: pulumi.Input[_builtins.str],
        key_name: pulumi.Input[_builtins.str],
        request_location: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeySecretVersion")
    def api_key_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @api_key_secret_version.setter
    def api_key_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[_builtins.str]: ...
    @key_name.setter
    def key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="requestLocation")
    def request_location(self) -> pulumi.Input[_builtins.str]: ...
    @request_location.setter
    def request_location(self, value: pulumi.Input[_builtins.str]): ...

class ToolsetMcpToolsetApiAuthenticationBearerTokenConfigArgsDict(TypedDict):
    token: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolsetMcpToolsetApiAuthenticationBearerTokenConfigArgs:
    def __init__(
        __self__, *, token: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token.setter
    def token(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolsetMcpToolsetApiAuthenticationOauthConfigArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    client_secret_version: pulumi.Input[_builtins.str]
    oauth_grant_type: pulumi.Input[_builtins.str]
    token_endpoint: pulumi.Input[_builtins.str]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ToolsetMcpToolsetApiAuthenticationOauthConfigArgs:
    def __init__(
        __self__,
        *,
        client_id: pulumi.Input[_builtins.str],
        client_secret_version: pulumi.Input[_builtins.str],
        oauth_grant_type: pulumi.Input[_builtins.str],
        token_endpoint: pulumi.Input[_builtins.str],
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecretVersion")
    def client_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @client_secret_version.setter
    def client_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="oauthGrantType")
    def oauth_grant_type(self) -> pulumi.Input[_builtins.str]: ...
    @oauth_grant_type.setter
    def oauth_grant_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scopes.setter
    def scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ToolsetMcpToolsetApiAuthenticationServiceAccountAuthConfigArgsDict(TypedDict):
    service_account: pulumi.Input[_builtins.str]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ToolsetMcpToolsetApiAuthenticationServiceAccountAuthConfigArgs:
    def __init__(
        __self__,
        *,
        service_account: pulumi.Input[_builtins.str],
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Input[_builtins.str]: ...
    @service_account.setter
    def service_account(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scopes.setter
    def scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ToolsetMcpToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ToolsetMcpToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgs:
    def __init__(__self__) -> None: ...

class ToolsetMcpToolsetServiceDirectoryConfigArgsDict(TypedDict):
    service: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ToolsetMcpToolsetServiceDirectoryConfigArgs:
    def __init__(__self__, *, service: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...

class ToolsetMcpToolsetTlsConfigArgsDict(TypedDict):
    ca_certs: pulumi.Input[
        Sequence[pulumi.Input[ToolsetMcpToolsetTlsConfigCaCertArgsDict]]
    ]
    ...

@pulumi.input_type
class ToolsetMcpToolsetTlsConfigArgs:
    def __init__(
        __self__,
        *,
        ca_certs: pulumi.Input[
            Sequence[pulumi.Input[ToolsetMcpToolsetTlsConfigCaCertArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(
        self,
    ) -> pulumi.Input[Sequence[pulumi.Input[ToolsetMcpToolsetTlsConfigCaCertArgs]]]: ...
    @ca_certs.setter
    def ca_certs(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ToolsetMcpToolsetTlsConfigCaCertArgs]]
        ],
    ): ...

class ToolsetMcpToolsetTlsConfigCaCertArgsDict(TypedDict):
    cert: pulumi.Input[_builtins.str]
    display_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ToolsetMcpToolsetTlsConfigCaCertArgs:
    def __init__(
        __self__,
        *,
        cert: pulumi.Input[_builtins.str],
        display_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> pulumi.Input[_builtins.str]: ...
    @cert.setter
    def cert(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...

class ToolsetOpenApiToolsetArgsDict(TypedDict):
    open_api_schema: pulumi.Input[_builtins.str]
    api_authentication: NotRequired[
        pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationArgsDict]
    ]
    ignore_unknown_fields: NotRequired[pulumi.Input[_builtins.bool]]
    service_directory_config: NotRequired[
        pulumi.Input[ToolsetOpenApiToolsetServiceDirectoryConfigArgsDict]
    ]
    tls_config: NotRequired[pulumi.Input[ToolsetOpenApiToolsetTlsConfigArgsDict]]
    url: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolsetOpenApiToolsetArgs:
    def __init__(
        __self__,
        *,
        open_api_schema: pulumi.Input[_builtins.str],
        api_authentication: Optional[
            pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationArgs]
        ] = ...,
        ignore_unknown_fields: Optional[pulumi.Input[_builtins.bool]] = ...,
        service_directory_config: Optional[
            pulumi.Input[ToolsetOpenApiToolsetServiceDirectoryConfigArgs]
        ] = ...,
        tls_config: Optional[pulumi.Input[ToolsetOpenApiToolsetTlsConfigArgs]] = ...,
        url: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="openApiSchema")
    def open_api_schema(self) -> pulumi.Input[_builtins.str]: ...
    @open_api_schema.setter
    def open_api_schema(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="apiAuthentication")
    def api_authentication(
        self,
    ) -> Optional[pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationArgs]]: ...
    @api_authentication.setter
    def api_authentication(
        self, value: Optional[pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="ignoreUnknownFields")
    def ignore_unknown_fields(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @ignore_unknown_fields.setter
    def ignore_unknown_fields(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceDirectoryConfig")
    def service_directory_config(
        self,
    ) -> Optional[pulumi.Input[ToolsetOpenApiToolsetServiceDirectoryConfigArgs]]: ...
    @service_directory_config.setter
    def service_directory_config(
        self,
        value: Optional[pulumi.Input[ToolsetOpenApiToolsetServiceDirectoryConfigArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="tlsConfig")
    def tls_config(
        self,
    ) -> Optional[pulumi.Input[ToolsetOpenApiToolsetTlsConfigArgs]]: ...
    @tls_config.setter
    def tls_config(
        self, value: Optional[pulumi.Input[ToolsetOpenApiToolsetTlsConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def url(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @url.setter
    def url(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolsetOpenApiToolsetApiAuthenticationArgsDict(TypedDict):
    api_key_config: NotRequired[
        pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationApiKeyConfigArgsDict]
    ]
    bearer_token_config: NotRequired[
        pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationBearerTokenConfigArgsDict]
    ]
    oauth_config: NotRequired[
        pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationOauthConfigArgsDict]
    ]
    service_account_auth_config: NotRequired[
        pulumi.Input[
            ToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfigArgsDict
        ]
    ]
    service_agent_id_token_auth_config: NotRequired[
        pulumi.Input[
            ToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgsDict
        ]
    ]
    ...

@pulumi.input_type
class ToolsetOpenApiToolsetApiAuthenticationArgs:
    def __init__(
        __self__,
        *,
        api_key_config: Optional[
            pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationApiKeyConfigArgs]
        ] = ...,
        bearer_token_config: Optional[
            pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationBearerTokenConfigArgs]
        ] = ...,
        oauth_config: Optional[
            pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationOauthConfigArgs]
        ] = ...,
        service_account_auth_config: Optional[
            pulumi.Input[
                ToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfigArgs
            ]
        ] = ...,
        service_agent_id_token_auth_config: Optional[
            pulumi.Input[
                ToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgs
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeyConfig")
    def api_key_config(
        self,
    ) -> Optional[
        pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationApiKeyConfigArgs]
    ]: ...
    @api_key_config.setter
    def api_key_config(
        self,
        value: Optional[
            pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationApiKeyConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="bearerTokenConfig")
    def bearer_token_config(
        self,
    ) -> Optional[
        pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationBearerTokenConfigArgs]
    ]: ...
    @bearer_token_config.setter
    def bearer_token_config(
        self,
        value: Optional[
            pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationBearerTokenConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="oauthConfig")
    def oauth_config(
        self,
    ) -> Optional[
        pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationOauthConfigArgs]
    ]: ...
    @oauth_config.setter
    def oauth_config(
        self,
        value: Optional[
            pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationOauthConfigArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccountAuthConfig")
    def service_account_auth_config(
        self,
    ) -> Optional[
        pulumi.Input[ToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfigArgs]
    ]: ...
    @service_account_auth_config.setter
    def service_account_auth_config(
        self,
        value: Optional[
            pulumi.Input[
                ToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfigArgs
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAgentIdTokenAuthConfig")
    def service_agent_id_token_auth_config(
        self,
    ) -> Optional[
        pulumi.Input[
            ToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgs
        ]
    ]: ...
    @service_agent_id_token_auth_config.setter
    def service_agent_id_token_auth_config(
        self,
        value: Optional[
            pulumi.Input[
                ToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgs
            ]
        ],
    ): ...

class ToolsetOpenApiToolsetApiAuthenticationApiKeyConfigArgsDict(TypedDict):
    api_key_secret_version: pulumi.Input[_builtins.str]
    key_name: pulumi.Input[_builtins.str]
    request_location: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ToolsetOpenApiToolsetApiAuthenticationApiKeyConfigArgs:
    def __init__(
        __self__,
        *,
        api_key_secret_version: pulumi.Input[_builtins.str],
        key_name: pulumi.Input[_builtins.str],
        request_location: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="apiKeySecretVersion")
    def api_key_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @api_key_secret_version.setter
    def api_key_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[_builtins.str]: ...
    @key_name.setter
    def key_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="requestLocation")
    def request_location(self) -> pulumi.Input[_builtins.str]: ...
    @request_location.setter
    def request_location(self, value: pulumi.Input[_builtins.str]): ...

class ToolsetOpenApiToolsetApiAuthenticationBearerTokenConfigArgsDict(TypedDict):
    token: NotRequired[pulumi.Input[_builtins.str]]
    ...

@pulumi.input_type
class ToolsetOpenApiToolsetApiAuthenticationBearerTokenConfigArgs:
    def __init__(
        __self__, *, token: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def token(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @token.setter
    def token(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ToolsetOpenApiToolsetApiAuthenticationOauthConfigArgsDict(TypedDict):
    client_id: pulumi.Input[_builtins.str]
    client_secret_version: pulumi.Input[_builtins.str]
    oauth_grant_type: pulumi.Input[_builtins.str]
    token_endpoint: pulumi.Input[_builtins.str]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ToolsetOpenApiToolsetApiAuthenticationOauthConfigArgs:
    def __init__(
        __self__,
        *,
        client_id: pulumi.Input[_builtins.str],
        client_secret_version: pulumi.Input[_builtins.str],
        oauth_grant_type: pulumi.Input[_builtins.str],
        token_endpoint: pulumi.Input[_builtins.str],
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[_builtins.str]: ...
    @client_id.setter
    def client_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="clientSecretVersion")
    def client_secret_version(self) -> pulumi.Input[_builtins.str]: ...
    @client_secret_version.setter
    def client_secret_version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="oauthGrantType")
    def oauth_grant_type(self) -> pulumi.Input[_builtins.str]: ...
    @oauth_grant_type.setter
    def oauth_grant_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="tokenEndpoint")
    def token_endpoint(self) -> pulumi.Input[_builtins.str]: ...
    @token_endpoint.setter
    def token_endpoint(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scopes.setter
    def scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfigArgsDict(TypedDict):
    service_account: pulumi.Input[_builtins.str]
    scopes: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ...

@pulumi.input_type
class ToolsetOpenApiToolsetApiAuthenticationServiceAccountAuthConfigArgs:
    def __init__(
        __self__,
        *,
        service_account: pulumi.Input[_builtins.str],
        scopes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> pulumi.Input[_builtins.str]: ...
    @service_account.setter
    def service_account(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def scopes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @scopes.setter
    def scopes(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgsDict(
    TypedDict
): ...

@pulumi.input_type
class ToolsetOpenApiToolsetApiAuthenticationServiceAgentIdTokenAuthConfigArgs:
    def __init__(__self__) -> None: ...

class ToolsetOpenApiToolsetServiceDirectoryConfigArgsDict(TypedDict):
    service: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ToolsetOpenApiToolsetServiceDirectoryConfigArgs:
    def __init__(__self__, *, service: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> pulumi.Input[_builtins.str]: ...
    @service.setter
    def service(self, value: pulumi.Input[_builtins.str]): ...

class ToolsetOpenApiToolsetTlsConfigArgsDict(TypedDict):
    ca_certs: pulumi.Input[
        Sequence[pulumi.Input[ToolsetOpenApiToolsetTlsConfigCaCertArgsDict]]
    ]
    ...

@pulumi.input_type
class ToolsetOpenApiToolsetTlsConfigArgs:
    def __init__(
        __self__,
        *,
        ca_certs: pulumi.Input[
            Sequence[pulumi.Input[ToolsetOpenApiToolsetTlsConfigCaCertArgs]]
        ],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="caCerts")
    def ca_certs(
        self,
    ) -> pulumi.Input[
        Sequence[pulumi.Input[ToolsetOpenApiToolsetTlsConfigCaCertArgs]]
    ]: ...
    @ca_certs.setter
    def ca_certs(
        self,
        value: pulumi.Input[
            Sequence[pulumi.Input[ToolsetOpenApiToolsetTlsConfigCaCertArgs]]
        ],
    ): ...

class ToolsetOpenApiToolsetTlsConfigCaCertArgsDict(TypedDict):
    cert: pulumi.Input[_builtins.str]
    display_name: pulumi.Input[_builtins.str]
    ...

@pulumi.input_type
class ToolsetOpenApiToolsetTlsConfigCaCertArgs:
    def __init__(
        __self__,
        *,
        cert: pulumi.Input[_builtins.str],
        display_name: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def cert(self) -> pulumi.Input[_builtins.str]: ...
    @cert.setter
    def cert(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
