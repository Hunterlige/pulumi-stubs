

import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['BotArgs', 'Bot']
@pulumi.input_type
class BotArgs:
    def __init__(__self__, *, abort_statement: pulumi.Input[BotAbortStatementArgs], child_directed: pulumi.Input[_builtins.bool], intents: pulumi.Input[Sequence[pulumi.Input[BotIntentArgs]]], clarification_prompt: Optional[pulumi.Input[BotClarificationPromptArgs]] = ..., create_version: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., detect_sentiment: Optional[pulumi.Input[_builtins.bool]] = ..., enable_model_improvements: Optional[pulumi.Input[_builtins.bool]] = ..., idle_session_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., locale: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nlu_intent_confidence_threshold: Optional[pulumi.Input[_builtins.float]] = ..., process_behavior: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., voice_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="abortStatement")
    def abort_statement(self) -> pulumi.Input[BotAbortStatementArgs]:
        
        ...
    
    @abort_statement.setter
    def abort_statement(self, value: pulumi.Input[BotAbortStatementArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="childDirected")
    def child_directed(self) -> pulumi.Input[_builtins.bool]:
        
        ...
    
    @child_directed.setter
    def child_directed(self, value: pulumi.Input[_builtins.bool]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def intents(self) -> pulumi.Input[Sequence[pulumi.Input[BotIntentArgs]]]:
        
        ...
    
    @intents.setter
    def intents(self, value: pulumi.Input[Sequence[pulumi.Input[BotIntentArgs]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clarificationPrompt")
    def clarification_prompt(self) -> Optional[pulumi.Input[BotClarificationPromptArgs]]:
        
        ...
    
    @clarification_prompt.setter
    def clarification_prompt(self, value: Optional[pulumi.Input[BotClarificationPromptArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createVersion")
    def create_version(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @create_version.setter
    def create_version(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="detectSentiment")
    def detect_sentiment(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @detect_sentiment.setter
    def detect_sentiment(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableModelImprovements")
    def enable_model_improvements(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_model_improvements.setter
    def enable_model_improvements(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleSessionTtlInSeconds")
    def idle_session_ttl_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @idle_session_ttl_in_seconds.setter
    def idle_session_ttl_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locale(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @locale.setter
    def locale(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nluIntentConfidenceThreshold")
    def nlu_intent_confidence_threshold(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @nlu_intent_confidence_threshold.setter
    def nlu_intent_confidence_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processBehavior")
    def process_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @process_behavior.setter
    def process_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceId")
    def voice_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @voice_id.setter
    def voice_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _BotState:
    def __init__(__self__, *, abort_statement: Optional[pulumi.Input[BotAbortStatementArgs]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., checksum: Optional[pulumi.Input[_builtins.str]] = ..., child_directed: Optional[pulumi.Input[_builtins.bool]] = ..., clarification_prompt: Optional[pulumi.Input[BotClarificationPromptArgs]] = ..., create_version: Optional[pulumi.Input[_builtins.bool]] = ..., created_date: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., detect_sentiment: Optional[pulumi.Input[_builtins.bool]] = ..., enable_model_improvements: Optional[pulumi.Input[_builtins.bool]] = ..., failure_reason: Optional[pulumi.Input[_builtins.str]] = ..., idle_session_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., intents: Optional[pulumi.Input[Sequence[pulumi.Input[BotIntentArgs]]]] = ..., last_updated_date: Optional[pulumi.Input[_builtins.str]] = ..., locale: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nlu_intent_confidence_threshold: Optional[pulumi.Input[_builtins.float]] = ..., process_behavior: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., voice_id: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="abortStatement")
    def abort_statement(self) -> Optional[pulumi.Input[BotAbortStatementArgs]]:
        
        ...
    
    @abort_statement.setter
    def abort_statement(self, value: Optional[pulumi.Input[BotAbortStatementArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def checksum(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @checksum.setter
    def checksum(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="childDirected")
    def child_directed(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @child_directed.setter
    def child_directed(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="clarificationPrompt")
    def clarification_prompt(self) -> Optional[pulumi.Input[BotClarificationPromptArgs]]:
        
        ...
    
    @clarification_prompt.setter
    def clarification_prompt(self, value: Optional[pulumi.Input[BotClarificationPromptArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createVersion")
    def create_version(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @create_version.setter
    def create_version(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="detectSentiment")
    def detect_sentiment(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @detect_sentiment.setter
    def detect_sentiment(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableModelImprovements")
    def enable_model_improvements(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enable_model_improvements.setter
    def enable_model_improvements(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @failure_reason.setter
    def failure_reason(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleSessionTtlInSeconds")
    def idle_session_ttl_in_seconds(self) -> Optional[pulumi.Input[_builtins.int]]:
        
        ...
    
    @idle_session_ttl_in_seconds.setter
    def idle_session_ttl_in_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def intents(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[BotIntentArgs]]]]:
        
        ...
    
    @intents.setter
    def intents(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[BotIntentArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @last_updated_date.setter
    def last_updated_date(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def locale(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @locale.setter
    def locale(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="nluIntentConfidenceThreshold")
    def nlu_intent_confidence_threshold(self) -> Optional[pulumi.Input[_builtins.float]]:
        
        ...
    
    @nlu_intent_confidence_threshold.setter
    def nlu_intent_confidence_threshold(self, value: Optional[pulumi.Input[_builtins.float]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="processBehavior")
    def process_behavior(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @process_behavior.setter
    def process_behavior(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @status.setter
    def status(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceId")
    def voice_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @voice_id.setter
    def voice_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("aws:lex/bot:Bot")
class Bot(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., abort_statement: Optional[pulumi.Input[Union[BotAbortStatementArgs, BotAbortStatementArgsDict]]] = ..., child_directed: Optional[pulumi.Input[_builtins.bool]] = ..., clarification_prompt: Optional[pulumi.Input[Union[BotClarificationPromptArgs, BotClarificationPromptArgsDict]]] = ..., create_version: Optional[pulumi.Input[_builtins.bool]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., detect_sentiment: Optional[pulumi.Input[_builtins.bool]] = ..., enable_model_improvements: Optional[pulumi.Input[_builtins.bool]] = ..., idle_session_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., intents: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BotIntentArgs, BotIntentArgsDict]]]]] = ..., locale: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nlu_intent_confidence_threshold: Optional[pulumi.Input[_builtins.float]] = ..., process_behavior: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., voice_id: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: BotArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., abort_statement: Optional[pulumi.Input[Union[BotAbortStatementArgs, BotAbortStatementArgsDict]]] = ..., arn: Optional[pulumi.Input[_builtins.str]] = ..., checksum: Optional[pulumi.Input[_builtins.str]] = ..., child_directed: Optional[pulumi.Input[_builtins.bool]] = ..., clarification_prompt: Optional[pulumi.Input[Union[BotClarificationPromptArgs, BotClarificationPromptArgsDict]]] = ..., create_version: Optional[pulumi.Input[_builtins.bool]] = ..., created_date: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., detect_sentiment: Optional[pulumi.Input[_builtins.bool]] = ..., enable_model_improvements: Optional[pulumi.Input[_builtins.bool]] = ..., failure_reason: Optional[pulumi.Input[_builtins.str]] = ..., idle_session_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., intents: Optional[pulumi.Input[Sequence[pulumi.Input[Union[BotIntentArgs, BotIntentArgsDict]]]]] = ..., last_updated_date: Optional[pulumi.Input[_builtins.str]] = ..., locale: Optional[pulumi.Input[_builtins.str]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., nlu_intent_confidence_threshold: Optional[pulumi.Input[_builtins.float]] = ..., process_behavior: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., status: Optional[pulumi.Input[_builtins.str]] = ..., version: Optional[pulumi.Input[_builtins.str]] = ..., voice_id: Optional[pulumi.Input[_builtins.str]] = ...) -> Bot:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="abortStatement")
    def abort_statement(self) -> pulumi.Output[outputs.BotAbortStatement]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter
    def checksum(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="childDirected")
    def child_directed(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="clarificationPrompt")
    def clarification_prompt(self) -> pulumi.Output[Optional[outputs.BotClarificationPrompt]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createVersion")
    def create_version(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="detectSentiment")
    def detect_sentiment(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="enableModelImprovements")
    def enable_model_improvements(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="failureReason")
    def failure_reason(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleSessionTtlInSeconds")
    def idle_session_ttl_in_seconds(self) -> pulumi.Output[Optional[_builtins.int]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def intents(self) -> pulumi.Output[Sequence[outputs.BotIntent]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="lastUpdatedDate")
    def last_updated_date(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def locale(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="nluIntentConfidenceThreshold")
    def nlu_intent_confidence_threshold(self) -> pulumi.Output[Optional[_builtins.float]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="processBehavior")
    def process_behavior(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def status(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="voiceId")
    def voice_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


