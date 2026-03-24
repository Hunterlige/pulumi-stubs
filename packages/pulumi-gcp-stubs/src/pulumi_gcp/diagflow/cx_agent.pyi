

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['CxAgentArgs', 'CxAgent']
@pulumi.input_type
class CxAgentArgs:
    def __init__(__self__, *, default_language_code: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], time_zone: pulumi.Input[_builtins.str], advanced_settings: Optional[pulumi.Input[CxAgentAdvancedSettingsArgs]] = ..., answer_feedback_settings: Optional[pulumi.Input[CxAgentAnswerFeedbackSettingsArgs]] = ..., avatar_uri: Optional[pulumi.Input[_builtins.str]] = ..., client_certificate_settings: Optional[pulumi.Input[CxAgentClientCertificateSettingsArgs]] = ..., delete_chat_engine_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enable_multi_language_training: Optional[pulumi.Input[_builtins.bool]] = ..., enable_spell_correction: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ..., gen_app_builder_settings: Optional[pulumi.Input[CxAgentGenAppBuilderSettingsArgs]] = ..., git_integration_settings: Optional[pulumi.Input[CxAgentGitIntegrationSettingsArgs]] = ..., locked: Optional[pulumi.Input[_builtins.bool]] = ..., personalization_settings: Optional[pulumi.Input[CxAgentPersonalizationSettingsArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., security_settings: Optional[pulumi.Input[_builtins.str]] = ..., speech_to_text_settings: Optional[pulumi.Input[CxAgentSpeechToTextSettingsArgs]] = ..., start_playbook: Optional[pulumi.Input[_builtins.str]] = ..., supported_language_codes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., text_to_speech_settings: Optional[pulumi.Input[CxAgentTextToSpeechSettingsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLanguageCode")
    def default_language_code(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @default_language_code.setter
    def default_language_code(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(self) -> Optional[pulumi.Input[CxAgentAdvancedSettingsArgs]]:
        
        ...
    
    @advanced_settings.setter
    def advanced_settings(self, value: Optional[pulumi.Input[CxAgentAdvancedSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="answerFeedbackSettings")
    def answer_feedback_settings(self) -> Optional[pulumi.Input[CxAgentAnswerFeedbackSettingsArgs]]:
        
        ...
    
    @answer_feedback_settings.setter
    def answer_feedback_settings(self, value: Optional[pulumi.Input[CxAgentAnswerFeedbackSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="avatarUri")
    def avatar_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @avatar_uri.setter
    def avatar_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificateSettings")
    def client_certificate_settings(self) -> Optional[pulumi.Input[CxAgentClientCertificateSettingsArgs]]:
        
        ...
    
    @client_certificate_settings.setter
    def client_certificate_settings(self, value: Optional[pulumi.Input[CxAgentClientCertificateSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteChatEngineOnDestroy")
    def delete_chat_engine_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_chat_engine_on_destroy.setter
    def delete_chat_engine_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMultiLanguageTraining")
    def enable_multi_language_training(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_multi_language_training.setter
    def enable_multi_language_training(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSpellCorrection")
    def enable_spell_correction(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_spell_correction.setter
    def enable_spell_correction(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    @_utilities.deprecated(...)
    def enable_stackdriver_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_stackdriver_logging.setter
    def enable_stackdriver_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="genAppBuilderSettings")
    def gen_app_builder_settings(self) -> Optional[pulumi.Input[CxAgentGenAppBuilderSettingsArgs]]:
        
        ...
    
    @gen_app_builder_settings.setter
    def gen_app_builder_settings(self, value: Optional[pulumi.Input[CxAgentGenAppBuilderSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitIntegrationSettings")
    def git_integration_settings(self) -> Optional[pulumi.Input[CxAgentGitIntegrationSettingsArgs]]:
        
        ...
    
    @git_integration_settings.setter
    def git_integration_settings(self, value: Optional[pulumi.Input[CxAgentGitIntegrationSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locked(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @locked.setter
    def locked(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="personalizationSettings")
    def personalization_settings(self) -> Optional[pulumi.Input[CxAgentPersonalizationSettingsArgs]]:
        
        ...
    
    @personalization_settings.setter
    def personalization_settings(self, value: Optional[pulumi.Input[CxAgentPersonalizationSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_settings.setter
    def security_settings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="speechToTextSettings")
    def speech_to_text_settings(self) -> Optional[pulumi.Input[CxAgentSpeechToTextSettingsArgs]]:
        
        ...
    
    @speech_to_text_settings.setter
    def speech_to_text_settings(self, value: Optional[pulumi.Input[CxAgentSpeechToTextSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startPlaybook")
    def start_playbook(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_playbook.setter
    def start_playbook(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedLanguageCodes")
    def supported_language_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @supported_language_codes.setter
    def supported_language_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="textToSpeechSettings")
    def text_to_speech_settings(self) -> Optional[pulumi.Input[CxAgentTextToSpeechSettingsArgs]]:
        
        ...
    
    @text_to_speech_settings.setter
    def text_to_speech_settings(self, value: Optional[pulumi.Input[CxAgentTextToSpeechSettingsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _CxAgentState:
    def __init__(__self__, *, advanced_settings: Optional[pulumi.Input[CxAgentAdvancedSettingsArgs]] = ..., answer_feedback_settings: Optional[pulumi.Input[CxAgentAnswerFeedbackSettingsArgs]] = ..., avatar_uri: Optional[pulumi.Input[_builtins.str]] = ..., client_certificate_settings: Optional[pulumi.Input[CxAgentClientCertificateSettingsArgs]] = ..., default_language_code: Optional[pulumi.Input[_builtins.str]] = ..., delete_chat_engine_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_multi_language_training: Optional[pulumi.Input[_builtins.bool]] = ..., enable_spell_correction: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ..., gen_app_builder_settings: Optional[pulumi.Input[CxAgentGenAppBuilderSettingsArgs]] = ..., git_integration_settings: Optional[pulumi.Input[CxAgentGitIntegrationSettingsArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., locked: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., personalization_settings: Optional[pulumi.Input[CxAgentPersonalizationSettingsArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., satisfies_pzi: Optional[pulumi.Input[_builtins.bool]] = ..., satisfies_pzs: Optional[pulumi.Input[_builtins.bool]] = ..., security_settings: Optional[pulumi.Input[_builtins.str]] = ..., speech_to_text_settings: Optional[pulumi.Input[CxAgentSpeechToTextSettingsArgs]] = ..., start_flow: Optional[pulumi.Input[_builtins.str]] = ..., start_playbook: Optional[pulumi.Input[_builtins.str]] = ..., supported_language_codes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., text_to_speech_settings: Optional[pulumi.Input[CxAgentTextToSpeechSettingsArgs]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(self) -> Optional[pulumi.Input[CxAgentAdvancedSettingsArgs]]:
        
        ...
    
    @advanced_settings.setter
    def advanced_settings(self, value: Optional[pulumi.Input[CxAgentAdvancedSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="answerFeedbackSettings")
    def answer_feedback_settings(self) -> Optional[pulumi.Input[CxAgentAnswerFeedbackSettingsArgs]]:
        
        ...
    
    @answer_feedback_settings.setter
    def answer_feedback_settings(self, value: Optional[pulumi.Input[CxAgentAnswerFeedbackSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="avatarUri")
    def avatar_uri(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @avatar_uri.setter
    def avatar_uri(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificateSettings")
    def client_certificate_settings(self) -> Optional[pulumi.Input[CxAgentClientCertificateSettingsArgs]]:
        
        ...
    
    @client_certificate_settings.setter
    def client_certificate_settings(self, value: Optional[pulumi.Input[CxAgentClientCertificateSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLanguageCode")
    def default_language_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @default_language_code.setter
    def default_language_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteChatEngineOnDestroy")
    def delete_chat_engine_on_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @delete_chat_engine_on_destroy.setter
    def delete_chat_engine_on_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMultiLanguageTraining")
    def enable_multi_language_training(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_multi_language_training.setter
    def enable_multi_language_training(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSpellCorrection")
    def enable_spell_correction(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_spell_correction.setter
    def enable_spell_correction(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    @_utilities.deprecated(...)
    def enable_stackdriver_logging(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_stackdriver_logging.setter
    def enable_stackdriver_logging(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="genAppBuilderSettings")
    def gen_app_builder_settings(self) -> Optional[pulumi.Input[CxAgentGenAppBuilderSettingsArgs]]:
        
        ...
    
    @gen_app_builder_settings.setter
    def gen_app_builder_settings(self, value: Optional[pulumi.Input[CxAgentGenAppBuilderSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitIntegrationSettings")
    def git_integration_settings(self) -> Optional[pulumi.Input[CxAgentGitIntegrationSettingsArgs]]:
        
        ...
    
    @git_integration_settings.setter
    def git_integration_settings(self, value: Optional[pulumi.Input[CxAgentGitIntegrationSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locked(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @locked.setter
    def locked(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="personalizationSettings")
    def personalization_settings(self) -> Optional[pulumi.Input[CxAgentPersonalizationSettingsArgs]]:
        
        ...
    
    @personalization_settings.setter
    def personalization_settings(self, value: Optional[pulumi.Input[CxAgentPersonalizationSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="satisfiesPzi")
    def satisfies_pzi(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @satisfies_pzi.setter
    def satisfies_pzi(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="satisfiesPzs")
    def satisfies_pzs(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @satisfies_pzs.setter
    def satisfies_pzs(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @security_settings.setter
    def security_settings(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="speechToTextSettings")
    def speech_to_text_settings(self) -> Optional[pulumi.Input[CxAgentSpeechToTextSettingsArgs]]:
        
        ...
    
    @speech_to_text_settings.setter
    def speech_to_text_settings(self, value: Optional[pulumi.Input[CxAgentSpeechToTextSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startFlow")
    def start_flow(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_flow.setter
    def start_flow(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="startPlaybook")
    def start_playbook(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @start_playbook.setter
    def start_playbook(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedLanguageCodes")
    def supported_language_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @supported_language_codes.setter
    def supported_language_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="textToSpeechSettings")
    def text_to_speech_settings(self) -> Optional[pulumi.Input[CxAgentTextToSpeechSettingsArgs]]:
        
        ...
    
    @text_to_speech_settings.setter
    def text_to_speech_settings(self, value: Optional[pulumi.Input[CxAgentTextToSpeechSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:diagflow/cxAgent:CxAgent")
class CxAgent(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., advanced_settings: Optional[pulumi.Input[Union[CxAgentAdvancedSettingsArgs, CxAgentAdvancedSettingsArgsDict]]] = ..., answer_feedback_settings: Optional[pulumi.Input[Union[CxAgentAnswerFeedbackSettingsArgs, CxAgentAnswerFeedbackSettingsArgsDict]]] = ..., avatar_uri: Optional[pulumi.Input[_builtins.str]] = ..., client_certificate_settings: Optional[pulumi.Input[Union[CxAgentClientCertificateSettingsArgs, CxAgentClientCertificateSettingsArgsDict]]] = ..., default_language_code: Optional[pulumi.Input[_builtins.str]] = ..., delete_chat_engine_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_multi_language_training: Optional[pulumi.Input[_builtins.bool]] = ..., enable_spell_correction: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ..., gen_app_builder_settings: Optional[pulumi.Input[Union[CxAgentGenAppBuilderSettingsArgs, CxAgentGenAppBuilderSettingsArgsDict]]] = ..., git_integration_settings: Optional[pulumi.Input[Union[CxAgentGitIntegrationSettingsArgs, CxAgentGitIntegrationSettingsArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., locked: Optional[pulumi.Input[_builtins.bool]] = ..., personalization_settings: Optional[pulumi.Input[Union[CxAgentPersonalizationSettingsArgs, CxAgentPersonalizationSettingsArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., security_settings: Optional[pulumi.Input[_builtins.str]] = ..., speech_to_text_settings: Optional[pulumi.Input[Union[CxAgentSpeechToTextSettingsArgs, CxAgentSpeechToTextSettingsArgsDict]]] = ..., start_playbook: Optional[pulumi.Input[_builtins.str]] = ..., supported_language_codes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., text_to_speech_settings: Optional[pulumi.Input[Union[CxAgentTextToSpeechSettingsArgs, CxAgentTextToSpeechSettingsArgsDict]]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: CxAgentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., advanced_settings: Optional[pulumi.Input[Union[CxAgentAdvancedSettingsArgs, CxAgentAdvancedSettingsArgsDict]]] = ..., answer_feedback_settings: Optional[pulumi.Input[Union[CxAgentAnswerFeedbackSettingsArgs, CxAgentAnswerFeedbackSettingsArgsDict]]] = ..., avatar_uri: Optional[pulumi.Input[_builtins.str]] = ..., client_certificate_settings: Optional[pulumi.Input[Union[CxAgentClientCertificateSettingsArgs, CxAgentClientCertificateSettingsArgsDict]]] = ..., default_language_code: Optional[pulumi.Input[_builtins.str]] = ..., delete_chat_engine_on_destroy: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enable_multi_language_training: Optional[pulumi.Input[_builtins.bool]] = ..., enable_spell_correction: Optional[pulumi.Input[_builtins.bool]] = ..., enable_stackdriver_logging: Optional[pulumi.Input[_builtins.bool]] = ..., gen_app_builder_settings: Optional[pulumi.Input[Union[CxAgentGenAppBuilderSettingsArgs, CxAgentGenAppBuilderSettingsArgsDict]]] = ..., git_integration_settings: Optional[pulumi.Input[Union[CxAgentGitIntegrationSettingsArgs, CxAgentGitIntegrationSettingsArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., locked: Optional[pulumi.Input[_builtins.bool]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., personalization_settings: Optional[pulumi.Input[Union[CxAgentPersonalizationSettingsArgs, CxAgentPersonalizationSettingsArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., satisfies_pzi: Optional[pulumi.Input[_builtins.bool]] = ..., satisfies_pzs: Optional[pulumi.Input[_builtins.bool]] = ..., security_settings: Optional[pulumi.Input[_builtins.str]] = ..., speech_to_text_settings: Optional[pulumi.Input[Union[CxAgentSpeechToTextSettingsArgs, CxAgentSpeechToTextSettingsArgsDict]]] = ..., start_flow: Optional[pulumi.Input[_builtins.str]] = ..., start_playbook: Optional[pulumi.Input[_builtins.str]] = ..., supported_language_codes: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., text_to_speech_settings: Optional[pulumi.Input[Union[CxAgentTextToSpeechSettingsArgs, CxAgentTextToSpeechSettingsArgsDict]]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ...) -> CxAgent:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="advancedSettings")
    def advanced_settings(self) -> pulumi.Output[outputs.CxAgentAdvancedSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="answerFeedbackSettings")
    def answer_feedback_settings(self) -> pulumi.Output[Optional[outputs.CxAgentAnswerFeedbackSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="avatarUri")
    def avatar_uri(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clientCertificateSettings")
    def client_certificate_settings(self) -> pulumi.Output[Optional[outputs.CxAgentClientCertificateSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="defaultLanguageCode")
    def default_language_code(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="deleteChatEngineOnDestroy")
    def delete_chat_engine_on_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableMultiLanguageTraining")
    def enable_multi_language_training(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableSpellCorrection")
    def enable_spell_correction(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableStackdriverLogging")
    @_utilities.deprecated(...)
    def enable_stackdriver_logging(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="genAppBuilderSettings")
    def gen_app_builder_settings(self) -> pulumi.Output[outputs.CxAgentGenAppBuilderSettings]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="gitIntegrationSettings")
    def git_integration_settings(self) -> pulumi.Output[Optional[outputs.CxAgentGitIntegrationSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locked(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="personalizationSettings")
    def personalization_settings(self) -> pulumi.Output[Optional[outputs.CxAgentPersonalizationSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="satisfiesPzi")
    def satisfies_pzi(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="satisfiesPzs")
    def satisfies_pzs(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="speechToTextSettings")
    def speech_to_text_settings(self) -> pulumi.Output[Optional[outputs.CxAgentSpeechToTextSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startFlow")
    def start_flow(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="startPlaybook")
    def start_playbook(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="supportedLanguageCodes")
    def supported_language_codes(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="textToSpeechSettings")
    def text_to_speech_settings(self) -> pulumi.Output[Optional[outputs.CxAgentTextToSpeechSettings]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


