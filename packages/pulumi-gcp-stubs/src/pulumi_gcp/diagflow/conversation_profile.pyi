

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['ConversationProfileArgs', 'ConversationProfile']
@pulumi.input_type
class ConversationProfileArgs:
    def __init__(__self__, *, display_name: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], automated_agent_config: Optional[pulumi.Input[ConversationProfileAutomatedAgentConfigArgs]] = ..., human_agent_assistant_config: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigArgs]] = ..., human_agent_handoff_config: Optional[pulumi.Input[ConversationProfileHumanAgentHandoffConfigArgs]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[ConversationProfileLoggingConfigArgs]] = ..., new_message_event_notification_config: Optional[pulumi.Input[ConversationProfileNewMessageEventNotificationConfigArgs]] = ..., new_recognition_result_notification_config: Optional[pulumi.Input[ConversationProfileNewRecognitionResultNotificationConfigArgs]] = ..., notification_config: Optional[pulumi.Input[ConversationProfileNotificationConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., security_settings: Optional[pulumi.Input[_builtins.str]] = ..., stt_config: Optional[pulumi.Input[ConversationProfileSttConfigArgs]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., tts_config: Optional[pulumi.Input[ConversationProfileTtsConfigArgs]] = ...) -> None:
        
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
    @pulumi.getter(name="automatedAgentConfig")
    def automated_agent_config(self) -> Optional[pulumi.Input[ConversationProfileAutomatedAgentConfigArgs]]:
        
        ...
    
    @automated_agent_config.setter
    def automated_agent_config(self, value: Optional[pulumi.Input[ConversationProfileAutomatedAgentConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanAgentAssistantConfig")
    def human_agent_assistant_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigArgs]]:
        
        ...
    
    @human_agent_assistant_config.setter
    def human_agent_assistant_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanAgentHandoffConfig")
    def human_agent_handoff_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentHandoffConfigArgs]]:
        
        ...
    
    @human_agent_handoff_config.setter
    def human_agent_handoff_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentHandoffConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @language_code.setter
    def language_code(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input[ConversationProfileLoggingConfigArgs]]:
        
        ...
    
    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input[ConversationProfileLoggingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="newMessageEventNotificationConfig")
    def new_message_event_notification_config(self) -> Optional[pulumi.Input[ConversationProfileNewMessageEventNotificationConfigArgs]]:
        
        ...
    
    @new_message_event_notification_config.setter
    def new_message_event_notification_config(self, value: Optional[pulumi.Input[ConversationProfileNewMessageEventNotificationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="newRecognitionResultNotificationConfig")
    def new_recognition_result_notification_config(self) -> Optional[pulumi.Input[ConversationProfileNewRecognitionResultNotificationConfigArgs]]:
        
        ...
    
    @new_recognition_result_notification_config.setter
    def new_recognition_result_notification_config(self, value: Optional[pulumi.Input[ConversationProfileNewRecognitionResultNotificationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> Optional[pulumi.Input[ConversationProfileNotificationConfigArgs]]:
        
        ...
    
    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input[ConversationProfileNotificationConfigArgs]]): # -> None:
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
    @pulumi.getter(name="sttConfig")
    def stt_config(self) -> Optional[pulumi.Input[ConversationProfileSttConfigArgs]]:
        
        ...
    
    @stt_config.setter
    def stt_config(self, value: Optional[pulumi.Input[ConversationProfileSttConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ttsConfig")
    def tts_config(self) -> Optional[pulumi.Input[ConversationProfileTtsConfigArgs]]:
        
        ...
    
    @tts_config.setter
    def tts_config(self, value: Optional[pulumi.Input[ConversationProfileTtsConfigArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _ConversationProfileState:
    def __init__(__self__, *, automated_agent_config: Optional[pulumi.Input[ConversationProfileAutomatedAgentConfigArgs]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., human_agent_assistant_config: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigArgs]] = ..., human_agent_handoff_config: Optional[pulumi.Input[ConversationProfileHumanAgentHandoffConfigArgs]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[ConversationProfileLoggingConfigArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., new_message_event_notification_config: Optional[pulumi.Input[ConversationProfileNewMessageEventNotificationConfigArgs]] = ..., new_recognition_result_notification_config: Optional[pulumi.Input[ConversationProfileNewRecognitionResultNotificationConfigArgs]] = ..., notification_config: Optional[pulumi.Input[ConversationProfileNotificationConfigArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., security_settings: Optional[pulumi.Input[_builtins.str]] = ..., stt_config: Optional[pulumi.Input[ConversationProfileSttConfigArgs]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., tts_config: Optional[pulumi.Input[ConversationProfileTtsConfigArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automatedAgentConfig")
    def automated_agent_config(self) -> Optional[pulumi.Input[ConversationProfileAutomatedAgentConfigArgs]]:
        
        ...
    
    @automated_agent_config.setter
    def automated_agent_config(self, value: Optional[pulumi.Input[ConversationProfileAutomatedAgentConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanAgentAssistantConfig")
    def human_agent_assistant_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigArgs]]:
        
        ...
    
    @human_agent_assistant_config.setter
    def human_agent_assistant_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentAssistantConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanAgentHandoffConfig")
    def human_agent_handoff_config(self) -> Optional[pulumi.Input[ConversationProfileHumanAgentHandoffConfigArgs]]:
        
        ...
    
    @human_agent_handoff_config.setter
    def human_agent_handoff_config(self, value: Optional[pulumi.Input[ConversationProfileHumanAgentHandoffConfigArgs]]): # -> None:
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
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> Optional[pulumi.Input[ConversationProfileLoggingConfigArgs]]:
        
        ...
    
    @logging_config.setter
    def logging_config(self, value: Optional[pulumi.Input[ConversationProfileLoggingConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="newMessageEventNotificationConfig")
    def new_message_event_notification_config(self) -> Optional[pulumi.Input[ConversationProfileNewMessageEventNotificationConfigArgs]]:
        
        ...
    
    @new_message_event_notification_config.setter
    def new_message_event_notification_config(self, value: Optional[pulumi.Input[ConversationProfileNewMessageEventNotificationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="newRecognitionResultNotificationConfig")
    def new_recognition_result_notification_config(self) -> Optional[pulumi.Input[ConversationProfileNewRecognitionResultNotificationConfigArgs]]:
        
        ...
    
    @new_recognition_result_notification_config.setter
    def new_recognition_result_notification_config(self, value: Optional[pulumi.Input[ConversationProfileNewRecognitionResultNotificationConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> Optional[pulumi.Input[ConversationProfileNotificationConfigArgs]]:
        
        ...
    
    @notification_config.setter
    def notification_config(self, value: Optional[pulumi.Input[ConversationProfileNotificationConfigArgs]]): # -> None:
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
    @pulumi.getter(name="sttConfig")
    def stt_config(self) -> Optional[pulumi.Input[ConversationProfileSttConfigArgs]]:
        
        ...
    
    @stt_config.setter
    def stt_config(self, value: Optional[pulumi.Input[ConversationProfileSttConfigArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @time_zone.setter
    def time_zone(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="ttsConfig")
    def tts_config(self) -> Optional[pulumi.Input[ConversationProfileTtsConfigArgs]]:
        
        ...
    
    @tts_config.setter
    def tts_config(self, value: Optional[pulumi.Input[ConversationProfileTtsConfigArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class ConversationProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., automated_agent_config: Optional[pulumi.Input[Union[ConversationProfileAutomatedAgentConfigArgs, ConversationProfileAutomatedAgentConfigArgsDict]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., human_agent_assistant_config: Optional[pulumi.Input[Union[ConversationProfileHumanAgentAssistantConfigArgs, ConversationProfileHumanAgentAssistantConfigArgsDict]]] = ..., human_agent_handoff_config: Optional[pulumi.Input[Union[ConversationProfileHumanAgentHandoffConfigArgs, ConversationProfileHumanAgentHandoffConfigArgsDict]]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[Union[ConversationProfileLoggingConfigArgs, ConversationProfileLoggingConfigArgsDict]]] = ..., new_message_event_notification_config: Optional[pulumi.Input[Union[ConversationProfileNewMessageEventNotificationConfigArgs, ConversationProfileNewMessageEventNotificationConfigArgsDict]]] = ..., new_recognition_result_notification_config: Optional[pulumi.Input[Union[ConversationProfileNewRecognitionResultNotificationConfigArgs, ConversationProfileNewRecognitionResultNotificationConfigArgsDict]]] = ..., notification_config: Optional[pulumi.Input[Union[ConversationProfileNotificationConfigArgs, ConversationProfileNotificationConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., security_settings: Optional[pulumi.Input[_builtins.str]] = ..., stt_config: Optional[pulumi.Input[Union[ConversationProfileSttConfigArgs, ConversationProfileSttConfigArgsDict]]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., tts_config: Optional[pulumi.Input[Union[ConversationProfileTtsConfigArgs, ConversationProfileTtsConfigArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: ConversationProfileArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., automated_agent_config: Optional[pulumi.Input[Union[ConversationProfileAutomatedAgentConfigArgs, ConversationProfileAutomatedAgentConfigArgsDict]]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., human_agent_assistant_config: Optional[pulumi.Input[Union[ConversationProfileHumanAgentAssistantConfigArgs, ConversationProfileHumanAgentAssistantConfigArgsDict]]] = ..., human_agent_handoff_config: Optional[pulumi.Input[Union[ConversationProfileHumanAgentHandoffConfigArgs, ConversationProfileHumanAgentHandoffConfigArgsDict]]] = ..., language_code: Optional[pulumi.Input[_builtins.str]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., logging_config: Optional[pulumi.Input[Union[ConversationProfileLoggingConfigArgs, ConversationProfileLoggingConfigArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., new_message_event_notification_config: Optional[pulumi.Input[Union[ConversationProfileNewMessageEventNotificationConfigArgs, ConversationProfileNewMessageEventNotificationConfigArgsDict]]] = ..., new_recognition_result_notification_config: Optional[pulumi.Input[Union[ConversationProfileNewRecognitionResultNotificationConfigArgs, ConversationProfileNewRecognitionResultNotificationConfigArgsDict]]] = ..., notification_config: Optional[pulumi.Input[Union[ConversationProfileNotificationConfigArgs, ConversationProfileNotificationConfigArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., security_settings: Optional[pulumi.Input[_builtins.str]] = ..., stt_config: Optional[pulumi.Input[Union[ConversationProfileSttConfigArgs, ConversationProfileSttConfigArgsDict]]] = ..., time_zone: Optional[pulumi.Input[_builtins.str]] = ..., tts_config: Optional[pulumi.Input[Union[ConversationProfileTtsConfigArgs, ConversationProfileTtsConfigArgsDict]]] = ...) -> ConversationProfile:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="automatedAgentConfig")
    def automated_agent_config(self) -> pulumi.Output[Optional[outputs.ConversationProfileAutomatedAgentConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanAgentAssistantConfig")
    def human_agent_assistant_config(self) -> pulumi.Output[Optional[outputs.ConversationProfileHumanAgentAssistantConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="humanAgentHandoffConfig")
    def human_agent_handoff_config(self) -> pulumi.Output[Optional[outputs.ConversationProfileHumanAgentHandoffConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="languageCode")
    def language_code(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="loggingConfig")
    def logging_config(self) -> pulumi.Output[Optional[outputs.ConversationProfileLoggingConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="newMessageEventNotificationConfig")
    def new_message_event_notification_config(self) -> pulumi.Output[Optional[outputs.ConversationProfileNewMessageEventNotificationConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="newRecognitionResultNotificationConfig")
    def new_recognition_result_notification_config(self) -> pulumi.Output[Optional[outputs.ConversationProfileNewRecognitionResultNotificationConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="notificationConfig")
    def notification_config(self) -> pulumi.Output[Optional[outputs.ConversationProfileNotificationConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="securitySettings")
    def security_settings(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="sttConfig")
    def stt_config(self) -> pulumi.Output[Optional[outputs.ConversationProfileSttConfig]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="ttsConfig")
    def tts_config(self) -> pulumi.Output[Optional[outputs.ConversationProfileTtsConfig]]:
        
        ...
    


