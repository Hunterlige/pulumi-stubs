import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AppArgs", "App"]

@pulumi.input_type
class AppArgs:
    def __init__(
        __self__,
        *,
        app_id: pulumi.Input[_builtins.str],
        display_name: pulumi.Input[_builtins.str],
        location: pulumi.Input[_builtins.str],
        audio_processing_config: Optional[
            pulumi.Input[AppAudioProcessingConfigArgs]
        ] = ...,
        client_certificate_settings: Optional[
            pulumi.Input[AppClientCertificateSettingsArgs]
        ] = ...,
        data_store_settings: Optional[pulumi.Input[AppDataStoreSettingsArgs]] = ...,
        default_channel_profile: Optional[
            pulumi.Input[AppDefaultChannelProfileArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        evaluation_metrics_thresholds: Optional[
            pulumi.Input[AppEvaluationMetricsThresholdsArgs]
        ] = ...,
        global_instruction: Optional[pulumi.Input[_builtins.str]] = ...,
        guardrails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        language_settings: Optional[pulumi.Input[AppLanguageSettingsArgs]] = ...,
        logging_settings: Optional[pulumi.Input[AppLoggingSettingsArgs]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        model_settings: Optional[pulumi.Input[AppModelSettingsArgs]] = ...,
        pinned: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        root_agent: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone_settings: Optional[pulumi.Input[AppTimeZoneSettingsArgs]] = ...,
        variable_declarations: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVariableDeclarationArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Input[_builtins.str]: ...
    @app_id.setter
    def app_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]: ...
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]: ...
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="audioProcessingConfig")
    def audio_processing_config(
        self,
    ) -> Optional[pulumi.Input[AppAudioProcessingConfigArgs]]: ...
    @audio_processing_config.setter
    def audio_processing_config(
        self, value: Optional[pulumi.Input[AppAudioProcessingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientCertificateSettings")
    def client_certificate_settings(
        self,
    ) -> Optional[pulumi.Input[AppClientCertificateSettingsArgs]]: ...
    @client_certificate_settings.setter
    def client_certificate_settings(
        self, value: Optional[pulumi.Input[AppClientCertificateSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dataStoreSettings")
    def data_store_settings(
        self,
    ) -> Optional[pulumi.Input[AppDataStoreSettingsArgs]]: ...
    @data_store_settings.setter
    def data_store_settings(
        self, value: Optional[pulumi.Input[AppDataStoreSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultChannelProfile")
    def default_channel_profile(
        self,
    ) -> Optional[pulumi.Input[AppDefaultChannelProfileArgs]]: ...
    @default_channel_profile.setter
    def default_channel_profile(
        self, value: Optional[pulumi.Input[AppDefaultChannelProfileArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="evaluationMetricsThresholds")
    def evaluation_metrics_thresholds(
        self,
    ) -> Optional[pulumi.Input[AppEvaluationMetricsThresholdsArgs]]: ...
    @evaluation_metrics_thresholds.setter
    def evaluation_metrics_thresholds(
        self, value: Optional[pulumi.Input[AppEvaluationMetricsThresholdsArgs]]
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
    def language_settings(self) -> Optional[pulumi.Input[AppLanguageSettingsArgs]]: ...
    @language_settings.setter
    def language_settings(
        self, value: Optional[pulumi.Input[AppLanguageSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="loggingSettings")
    def logging_settings(self) -> Optional[pulumi.Input[AppLoggingSettingsArgs]]: ...
    @logging_settings.setter
    def logging_settings(
        self, value: Optional[pulumi.Input[AppLoggingSettingsArgs]]
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
    def model_settings(self) -> Optional[pulumi.Input[AppModelSettingsArgs]]: ...
    @model_settings.setter
    def model_settings(self, value: Optional[pulumi.Input[AppModelSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def pinned(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @pinned.setter
    def pinned(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootAgent")
    def root_agent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_agent.setter
    def root_agent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZoneSettings")
    def time_zone_settings(self) -> Optional[pulumi.Input[AppTimeZoneSettingsArgs]]: ...
    @time_zone_settings.setter
    def time_zone_settings(
        self, value: Optional[pulumi.Input[AppTimeZoneSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="variableDeclarations")
    def variable_declarations(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AppVariableDeclarationArgs]]]]: ...
    @variable_declarations.setter
    def variable_declarations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVariableDeclarationArgs]]]
        ],
    ): ...

@pulumi.input_type
class _AppState:
    def __init__(
        __self__,
        *,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        audio_processing_config: Optional[
            pulumi.Input[AppAudioProcessingConfigArgs]
        ] = ...,
        client_certificate_settings: Optional[
            pulumi.Input[AppClientCertificateSettingsArgs]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        data_store_settings: Optional[pulumi.Input[AppDataStoreSettingsArgs]] = ...,
        default_channel_profile: Optional[
            pulumi.Input[AppDefaultChannelProfileArgs]
        ] = ...,
        deployment_count: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        evaluation_metrics_thresholds: Optional[
            pulumi.Input[AppEvaluationMetricsThresholdsArgs]
        ] = ...,
        global_instruction: Optional[pulumi.Input[_builtins.str]] = ...,
        guardrails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        language_settings: Optional[pulumi.Input[AppLanguageSettingsArgs]] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_settings: Optional[pulumi.Input[AppLoggingSettingsArgs]] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        model_settings: Optional[pulumi.Input[AppModelSettingsArgs]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        pinned: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        root_agent: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone_settings: Optional[pulumi.Input[AppTimeZoneSettingsArgs]] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        variable_declarations: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVariableDeclarationArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @app_id.setter
    def app_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="audioProcessingConfig")
    def audio_processing_config(
        self,
    ) -> Optional[pulumi.Input[AppAudioProcessingConfigArgs]]: ...
    @audio_processing_config.setter
    def audio_processing_config(
        self, value: Optional[pulumi.Input[AppAudioProcessingConfigArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="clientCertificateSettings")
    def client_certificate_settings(
        self,
    ) -> Optional[pulumi.Input[AppClientCertificateSettingsArgs]]: ...
    @client_certificate_settings.setter
    def client_certificate_settings(
        self, value: Optional[pulumi.Input[AppClientCertificateSettingsArgs]]
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
    ) -> Optional[pulumi.Input[AppDataStoreSettingsArgs]]: ...
    @data_store_settings.setter
    def data_store_settings(
        self, value: Optional[pulumi.Input[AppDataStoreSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="defaultChannelProfile")
    def default_channel_profile(
        self,
    ) -> Optional[pulumi.Input[AppDefaultChannelProfileArgs]]: ...
    @default_channel_profile.setter
    def default_channel_profile(
        self, value: Optional[pulumi.Input[AppDefaultChannelProfileArgs]]
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
    ) -> Optional[pulumi.Input[AppEvaluationMetricsThresholdsArgs]]: ...
    @evaluation_metrics_thresholds.setter
    def evaluation_metrics_thresholds(
        self, value: Optional[pulumi.Input[AppEvaluationMetricsThresholdsArgs]]
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
    def language_settings(self) -> Optional[pulumi.Input[AppLanguageSettingsArgs]]: ...
    @language_settings.setter
    def language_settings(
        self, value: Optional[pulumi.Input[AppLanguageSettingsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="loggingSettings")
    def logging_settings(self) -> Optional[pulumi.Input[AppLoggingSettingsArgs]]: ...
    @logging_settings.setter
    def logging_settings(
        self, value: Optional[pulumi.Input[AppLoggingSettingsArgs]]
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
    def model_settings(self) -> Optional[pulumi.Input[AppModelSettingsArgs]]: ...
    @model_settings.setter
    def model_settings(self, value: Optional[pulumi.Input[AppModelSettingsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def pinned(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @pinned.setter
    def pinned(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="rootAgent")
    def root_agent(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @root_agent.setter
    def root_agent(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="timeZoneSettings")
    def time_zone_settings(self) -> Optional[pulumi.Input[AppTimeZoneSettingsArgs]]: ...
    @time_zone_settings.setter
    def time_zone_settings(
        self, value: Optional[pulumi.Input[AppTimeZoneSettingsArgs]]
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
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[AppVariableDeclarationArgs]]]]: ...
    @variable_declarations.setter
    def variable_declarations(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[AppVariableDeclarationArgs]]]
        ],
    ): ...

@pulumi.type_token("gcp:ces/app:App")
class App(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        audio_processing_config: Optional[
            pulumi.Input[
                Union[AppAudioProcessingConfigArgs, AppAudioProcessingConfigArgsDict]
            ]
        ] = ...,
        client_certificate_settings: Optional[
            pulumi.Input[
                Union[
                    AppClientCertificateSettingsArgs,
                    AppClientCertificateSettingsArgsDict,
                ]
            ]
        ] = ...,
        data_store_settings: Optional[
            pulumi.Input[Union[AppDataStoreSettingsArgs, AppDataStoreSettingsArgsDict]]
        ] = ...,
        default_channel_profile: Optional[
            pulumi.Input[
                Union[AppDefaultChannelProfileArgs, AppDefaultChannelProfileArgsDict]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        evaluation_metrics_thresholds: Optional[
            pulumi.Input[
                Union[
                    AppEvaluationMetricsThresholdsArgs,
                    AppEvaluationMetricsThresholdsArgsDict,
                ]
            ]
        ] = ...,
        global_instruction: Optional[pulumi.Input[_builtins.str]] = ...,
        guardrails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        language_settings: Optional[
            pulumi.Input[Union[AppLanguageSettingsArgs, AppLanguageSettingsArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_settings: Optional[
            pulumi.Input[Union[AppLoggingSettingsArgs, AppLoggingSettingsArgsDict]]
        ] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        model_settings: Optional[
            pulumi.Input[Union[AppModelSettingsArgs, AppModelSettingsArgsDict]]
        ] = ...,
        pinned: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        root_agent: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone_settings: Optional[
            pulumi.Input[Union[AppTimeZoneSettingsArgs, AppTimeZoneSettingsArgsDict]]
        ] = ...,
        variable_declarations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AppVariableDeclarationArgs, AppVariableDeclarationArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AppArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        app_id: Optional[pulumi.Input[_builtins.str]] = ...,
        audio_processing_config: Optional[
            pulumi.Input[
                Union[AppAudioProcessingConfigArgs, AppAudioProcessingConfigArgsDict]
            ]
        ] = ...,
        client_certificate_settings: Optional[
            pulumi.Input[
                Union[
                    AppClientCertificateSettingsArgs,
                    AppClientCertificateSettingsArgsDict,
                ]
            ]
        ] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        data_store_settings: Optional[
            pulumi.Input[Union[AppDataStoreSettingsArgs, AppDataStoreSettingsArgsDict]]
        ] = ...,
        default_channel_profile: Optional[
            pulumi.Input[
                Union[AppDefaultChannelProfileArgs, AppDefaultChannelProfileArgsDict]
            ]
        ] = ...,
        deployment_count: Optional[pulumi.Input[_builtins.int]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        display_name: Optional[pulumi.Input[_builtins.str]] = ...,
        etag: Optional[pulumi.Input[_builtins.str]] = ...,
        evaluation_metrics_thresholds: Optional[
            pulumi.Input[
                Union[
                    AppEvaluationMetricsThresholdsArgs,
                    AppEvaluationMetricsThresholdsArgsDict,
                ]
            ]
        ] = ...,
        global_instruction: Optional[pulumi.Input[_builtins.str]] = ...,
        guardrails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        language_settings: Optional[
            pulumi.Input[Union[AppLanguageSettingsArgs, AppLanguageSettingsArgsDict]]
        ] = ...,
        location: Optional[pulumi.Input[_builtins.str]] = ...,
        logging_settings: Optional[
            pulumi.Input[Union[AppLoggingSettingsArgs, AppLoggingSettingsArgsDict]]
        ] = ...,
        metadata: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        model_settings: Optional[
            pulumi.Input[Union[AppModelSettingsArgs, AppModelSettingsArgsDict]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        pinned: Optional[pulumi.Input[_builtins.bool]] = ...,
        project: Optional[pulumi.Input[_builtins.str]] = ...,
        root_agent: Optional[pulumi.Input[_builtins.str]] = ...,
        time_zone_settings: Optional[
            pulumi.Input[Union[AppTimeZoneSettingsArgs, AppTimeZoneSettingsArgsDict]]
        ] = ...,
        update_time: Optional[pulumi.Input[_builtins.str]] = ...,
        variable_declarations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AppVariableDeclarationArgs, AppVariableDeclarationArgsDict
                        ]
                    ]
                ]
            ]
        ] = ...,
    ) -> App: ...
    @_builtins.property
    @pulumi.getter(name="appId")
    def app_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="audioProcessingConfig")
    def audio_processing_config(
        self,
    ) -> pulumi.Output[Optional[outputs.AppAudioProcessingConfig]]: ...
    @_builtins.property
    @pulumi.getter(name="clientCertificateSettings")
    def client_certificate_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.AppClientCertificateSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="dataStoreSettings")
    def data_store_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.AppDataStoreSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="defaultChannelProfile")
    def default_channel_profile(
        self,
    ) -> pulumi.Output[Optional[outputs.AppDefaultChannelProfile]]: ...
    @_builtins.property
    @pulumi.getter(name="deploymentCount")
    def deployment_count(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="evaluationMetricsThresholds")
    def evaluation_metrics_thresholds(
        self,
    ) -> pulumi.Output[Optional[outputs.AppEvaluationMetricsThresholds]]: ...
    @_builtins.property
    @pulumi.getter(name="globalInstruction")
    def global_instruction(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def guardrails(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="languageSettings")
    def language_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.AppLanguageSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="loggingSettings")
    def logging_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.AppLoggingSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(self) -> pulumi.Output[Optional[outputs.AppModelSettings]]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def pinned(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="rootAgent")
    def root_agent(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="timeZoneSettings")
    def time_zone_settings(
        self,
    ) -> pulumi.Output[Optional[outputs.AppTimeZoneSettings]]: ...
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="variableDeclarations")
    def variable_declarations(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.AppVariableDeclaration]]]: ...
