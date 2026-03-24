

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
__all__ = ['GuardrailArgs', 'Guardrail']
@pulumi.input_type
class GuardrailArgs:
    def __init__(__self__, *, app: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], guardrail_id: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], action: Optional[pulumi.Input[GuardrailActionArgs]] = ..., code_callback: Optional[pulumi.Input[GuardrailCodeCallbackArgs]] = ..., content_filter: Optional[pulumi.Input[GuardrailContentFilterArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., llm_policy: Optional[pulumi.Input[GuardrailLlmPolicyArgs]] = ..., llm_prompt_security: Optional[pulumi.Input[GuardrailLlmPromptSecurityArgs]] = ..., model_safety: Optional[pulumi.Input[GuardrailModelSafetyArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def app(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @app.setter
    def app(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @display_name.setter
    def display_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guardrailId")
    def guardrail_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @guardrail_id.setter
    def guardrail_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[GuardrailActionArgs]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[GuardrailActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeCallback")
    def code_callback(self) -> Optional[pulumi.Input[GuardrailCodeCallbackArgs]]:
        
        ...
    
    @code_callback.setter
    def code_callback(self, value: Optional[pulumi.Input[GuardrailCodeCallbackArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentFilter")
    def content_filter(self) -> Optional[pulumi.Input[GuardrailContentFilterArgs]]:
        
        ...
    
    @content_filter.setter
    def content_filter(self, value: Optional[pulumi.Input[GuardrailContentFilterArgs]]): # -> None:
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
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="llmPolicy")
    def llm_policy(self) -> Optional[pulumi.Input[GuardrailLlmPolicyArgs]]:
        
        ...
    
    @llm_policy.setter
    def llm_policy(self, value: Optional[pulumi.Input[GuardrailLlmPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="llmPromptSecurity")
    def llm_prompt_security(self) -> Optional[pulumi.Input[GuardrailLlmPromptSecurityArgs]]:
        
        ...
    
    @llm_prompt_security.setter
    def llm_prompt_security(self, value: Optional[pulumi.Input[GuardrailLlmPromptSecurityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSafety")
    def model_safety(self) -> Optional[pulumi.Input[GuardrailModelSafetyArgs]]:
        
        ...
    
    @model_safety.setter
    def model_safety(self, value: Optional[pulumi.Input[GuardrailModelSafetyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.input_type
class _GuardrailState:
    def __init__(__self__, *, action: Optional[pulumi.Input[GuardrailActionArgs]] = ..., app: Optional[pulumi.Input[_builtins.str]] = ..., code_callback: Optional[pulumi.Input[GuardrailCodeCallbackArgs]] = ..., content_filter: Optional[pulumi.Input[GuardrailContentFilterArgs]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., guardrail_id: Optional[pulumi.Input[_builtins.str]] = ..., llm_policy: Optional[pulumi.Input[GuardrailLlmPolicyArgs]] = ..., llm_prompt_security: Optional[pulumi.Input[GuardrailLlmPromptSecurityArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., model_safety: Optional[pulumi.Input[GuardrailModelSafetyArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> Optional[pulumi.Input[GuardrailActionArgs]]:
        
        ...
    
    @action.setter
    def action(self, value: Optional[pulumi.Input[GuardrailActionArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def app(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app.setter
    def app(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeCallback")
    def code_callback(self) -> Optional[pulumi.Input[GuardrailCodeCallbackArgs]]:
        
        ...
    
    @code_callback.setter
    def code_callback(self, value: Optional[pulumi.Input[GuardrailCodeCallbackArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentFilter")
    def content_filter(self) -> Optional[pulumi.Input[GuardrailContentFilterArgs]]:
        
        ...
    
    @content_filter.setter
    def content_filter(self, value: Optional[pulumi.Input[GuardrailContentFilterArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter
    def enabled(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @enabled.setter
    def enabled(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guardrailId")
    def guardrail_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @guardrail_id.setter
    def guardrail_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="llmPolicy")
    def llm_policy(self) -> Optional[pulumi.Input[GuardrailLlmPolicyArgs]]:
        
        ...
    
    @llm_policy.setter
    def llm_policy(self, value: Optional[pulumi.Input[GuardrailLlmPolicyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="llmPromptSecurity")
    def llm_prompt_security(self) -> Optional[pulumi.Input[GuardrailLlmPromptSecurityArgs]]:
        
        ...
    
    @llm_prompt_security.setter
    def llm_prompt_security(self, value: Optional[pulumi.Input[GuardrailLlmPromptSecurityArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSafety")
    def model_safety(self) -> Optional[pulumi.Input[GuardrailModelSafetyArgs]]:
        
        ...
    
    @model_safety.setter
    def model_safety(self, value: Optional[pulumi.Input[GuardrailModelSafetyArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:ces/guardrail:Guardrail")
class Guardrail(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., action: Optional[pulumi.Input[Union[GuardrailActionArgs, GuardrailActionArgsDict]]] = ..., app: Optional[pulumi.Input[_builtins.str]] = ..., code_callback: Optional[pulumi.Input[Union[GuardrailCodeCallbackArgs, GuardrailCodeCallbackArgsDict]]] = ..., content_filter: Optional[pulumi.Input[Union[GuardrailContentFilterArgs, GuardrailContentFilterArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., guardrail_id: Optional[pulumi.Input[_builtins.str]] = ..., llm_policy: Optional[pulumi.Input[Union[GuardrailLlmPolicyArgs, GuardrailLlmPolicyArgsDict]]] = ..., llm_prompt_security: Optional[pulumi.Input[Union[GuardrailLlmPromptSecurityArgs, GuardrailLlmPromptSecurityArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., model_safety: Optional[pulumi.Input[Union[GuardrailModelSafetyArgs, GuardrailModelSafetyArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: GuardrailArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., action: Optional[pulumi.Input[Union[GuardrailActionArgs, GuardrailActionArgsDict]]] = ..., app: Optional[pulumi.Input[_builtins.str]] = ..., code_callback: Optional[pulumi.Input[Union[GuardrailCodeCallbackArgs, GuardrailCodeCallbackArgsDict]]] = ..., content_filter: Optional[pulumi.Input[Union[GuardrailContentFilterArgs, GuardrailContentFilterArgsDict]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., enabled: Optional[pulumi.Input[_builtins.bool]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., guardrail_id: Optional[pulumi.Input[_builtins.str]] = ..., llm_policy: Optional[pulumi.Input[Union[GuardrailLlmPolicyArgs, GuardrailLlmPolicyArgsDict]]] = ..., llm_prompt_security: Optional[pulumi.Input[Union[GuardrailLlmPromptSecurityArgs, GuardrailLlmPromptSecurityArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., model_safety: Optional[pulumi.Input[Union[GuardrailModelSafetyArgs, GuardrailModelSafetyArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Guardrail:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def action(self) -> pulumi.Output[Optional[outputs.GuardrailAction]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def app(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="codeCallback")
    def code_callback(self) -> pulumi.Output[Optional[outputs.GuardrailCodeCallback]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="contentFilter")
    def content_filter(self) -> pulumi.Output[Optional[outputs.GuardrailContentFilter]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter
    def enabled(self) -> pulumi.Output[Optional[_builtins.bool]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guardrailId")
    def guardrail_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="llmPolicy")
    def llm_policy(self) -> pulumi.Output[Optional[outputs.GuardrailLlmPolicy]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="llmPromptSecurity")
    def llm_prompt_security(self) -> pulumi.Output[Optional[outputs.GuardrailLlmPromptSecurity]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSafety")
    def model_safety(self) -> pulumi.Output[Optional[outputs.GuardrailModelSafety]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


