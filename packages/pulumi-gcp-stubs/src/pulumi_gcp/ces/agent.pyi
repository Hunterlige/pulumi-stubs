

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
__all__ = ['AgentArgs', 'Agent']
@pulumi.input_type
class AgentArgs:
    def __init__(__self__, *, app: pulumi.Input[_builtins.str], display_name: pulumi.Input[_builtins.str], location: pulumi.Input[_builtins.str], after_agent_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterAgentCallbackArgs]]]] = ..., after_model_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterModelCallbackArgs]]]] = ..., after_tool_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterToolCallbackArgs]]]] = ..., agent_id: Optional[pulumi.Input[_builtins.str]] = ..., before_agent_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeAgentCallbackArgs]]]] = ..., before_model_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeModelCallbackArgs]]]] = ..., before_tool_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeToolCallbackArgs]]]] = ..., child_agents: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., guardrails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., instruction: Optional[pulumi.Input[_builtins.str]] = ..., llm_agent: Optional[pulumi.Input[AgentLlmAgentArgs]] = ..., model_settings: Optional[pulumi.Input[AgentModelSettingsArgs]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., remote_dialogflow_agent: Optional[pulumi.Input[AgentRemoteDialogflowAgentArgs]] = ..., tools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., toolsets: Optional[pulumi.Input[Sequence[pulumi.Input[AgentToolsetArgs]]]] = ...) -> None:
        
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
    @pulumi.getter
    def location(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @location.setter
    def location(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterAgentCallbacks")
    def after_agent_callbacks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterAgentCallbackArgs]]]]:
        
        ...
    
    @after_agent_callbacks.setter
    def after_agent_callbacks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterAgentCallbackArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterModelCallbacks")
    def after_model_callbacks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterModelCallbackArgs]]]]:
        
        ...
    
    @after_model_callbacks.setter
    def after_model_callbacks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterModelCallbackArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterToolCallbacks")
    def after_tool_callbacks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterToolCallbackArgs]]]]:
        
        ...
    
    @after_tool_callbacks.setter
    def after_tool_callbacks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterToolCallbackArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_id.setter
    def agent_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeAgentCallbacks")
    def before_agent_callbacks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeAgentCallbackArgs]]]]:
        
        ...
    
    @before_agent_callbacks.setter
    def before_agent_callbacks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeAgentCallbackArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeModelCallbacks")
    def before_model_callbacks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeModelCallbackArgs]]]]:
        
        ...
    
    @before_model_callbacks.setter
    def before_model_callbacks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeModelCallbackArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeToolCallbacks")
    def before_tool_callbacks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeToolCallbackArgs]]]]:
        
        ...
    
    @before_tool_callbacks.setter
    def before_tool_callbacks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeToolCallbackArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="childAgents")
    def child_agents(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @child_agents.setter
    def child_agents(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    def guardrails(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @guardrails.setter
    def guardrails(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instruction(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instruction.setter
    def instruction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="llmAgent")
    def llm_agent(self) -> Optional[pulumi.Input[AgentLlmAgentArgs]]:
        
        ...
    
    @llm_agent.setter
    def llm_agent(self, value: Optional[pulumi.Input[AgentLlmAgentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(self) -> Optional[pulumi.Input[AgentModelSettingsArgs]]:
        
        ...
    
    @model_settings.setter
    def model_settings(self, value: Optional[pulumi.Input[AgentModelSettingsArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def project(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @project.setter
    def project(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="remoteDialogflowAgent")
    def remote_dialogflow_agent(self) -> Optional[pulumi.Input[AgentRemoteDialogflowAgentArgs]]:
        
        ...
    
    @remote_dialogflow_agent.setter
    def remote_dialogflow_agent(self, value: Optional[pulumi.Input[AgentRemoteDialogflowAgentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tools.setter
    def tools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def toolsets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentToolsetArgs]]]]:
        
        ...
    
    @toolsets.setter
    def toolsets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentToolsetArgs]]]]): # -> None:
        ...
    


@pulumi.input_type
class _AgentState:
    def __init__(__self__, *, after_agent_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterAgentCallbackArgs]]]] = ..., after_model_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterModelCallbackArgs]]]] = ..., after_tool_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterToolCallbackArgs]]]] = ..., agent_id: Optional[pulumi.Input[_builtins.str]] = ..., app: Optional[pulumi.Input[_builtins.str]] = ..., before_agent_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeAgentCallbackArgs]]]] = ..., before_model_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeModelCallbackArgs]]]] = ..., before_tool_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeToolCallbackArgs]]]] = ..., child_agents: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., generated_summary: Optional[pulumi.Input[_builtins.str]] = ..., guardrails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., instruction: Optional[pulumi.Input[_builtins.str]] = ..., llm_agent: Optional[pulumi.Input[AgentLlmAgentArgs]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., model_settings: Optional[pulumi.Input[AgentModelSettingsArgs]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., remote_dialogflow_agent: Optional[pulumi.Input[AgentRemoteDialogflowAgentArgs]] = ..., tools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., toolsets: Optional[pulumi.Input[Sequence[pulumi.Input[AgentToolsetArgs]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterAgentCallbacks")
    def after_agent_callbacks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterAgentCallbackArgs]]]]:
        
        ...
    
    @after_agent_callbacks.setter
    def after_agent_callbacks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterAgentCallbackArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterModelCallbacks")
    def after_model_callbacks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterModelCallbackArgs]]]]:
        
        ...
    
    @after_model_callbacks.setter
    def after_model_callbacks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterModelCallbackArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterToolCallbacks")
    def after_tool_callbacks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterToolCallbackArgs]]]]:
        
        ...
    
    @after_tool_callbacks.setter
    def after_tool_callbacks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAfterToolCallbackArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_id.setter
    def agent_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def app(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @app.setter
    def app(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeAgentCallbacks")
    def before_agent_callbacks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeAgentCallbackArgs]]]]:
        
        ...
    
    @before_agent_callbacks.setter
    def before_agent_callbacks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeAgentCallbackArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeModelCallbacks")
    def before_model_callbacks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeModelCallbackArgs]]]]:
        
        ...
    
    @before_model_callbacks.setter
    def before_model_callbacks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeModelCallbackArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeToolCallbacks")
    def before_tool_callbacks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeToolCallbackArgs]]]]:
        
        ...
    
    @before_tool_callbacks.setter
    def before_tool_callbacks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentBeforeToolCallbackArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="childAgents")
    def child_agents(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @child_agents.setter
    def child_agents(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
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
    def etag(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @etag.setter
    def etag(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatedSummary")
    def generated_summary(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @generated_summary.setter
    def generated_summary(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def guardrails(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @guardrails.setter
    def guardrails(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def instruction(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instruction.setter
    def instruction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="llmAgent")
    def llm_agent(self) -> Optional[pulumi.Input[AgentLlmAgentArgs]]:
        
        ...
    
    @llm_agent.setter
    def llm_agent(self, value: Optional[pulumi.Input[AgentLlmAgentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @location.setter
    def location(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(self) -> Optional[pulumi.Input[AgentModelSettingsArgs]]:
        
        ...
    
    @model_settings.setter
    def model_settings(self, value: Optional[pulumi.Input[AgentModelSettingsArgs]]): # -> None:
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
    @pulumi.getter(name="remoteDialogflowAgent")
    def remote_dialogflow_agent(self) -> Optional[pulumi.Input[AgentRemoteDialogflowAgentArgs]]:
        
        ...
    
    @remote_dialogflow_agent.setter
    def remote_dialogflow_agent(self, value: Optional[pulumi.Input[AgentRemoteDialogflowAgentArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def tools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tools.setter
    def tools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def toolsets(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentToolsetArgs]]]]:
        
        ...
    
    @toolsets.setter
    def toolsets(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentToolsetArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @update_time.setter
    def update_time(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    


@pulumi.type_token("gcp:ces/agent:Agent")
class Agent(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., after_agent_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentAfterAgentCallbackArgs, AgentAfterAgentCallbackArgsDict]]]]] = ..., after_model_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentAfterModelCallbackArgs, AgentAfterModelCallbackArgsDict]]]]] = ..., after_tool_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentAfterToolCallbackArgs, AgentAfterToolCallbackArgsDict]]]]] = ..., agent_id: Optional[pulumi.Input[_builtins.str]] = ..., app: Optional[pulumi.Input[_builtins.str]] = ..., before_agent_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentBeforeAgentCallbackArgs, AgentBeforeAgentCallbackArgsDict]]]]] = ..., before_model_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentBeforeModelCallbackArgs, AgentBeforeModelCallbackArgsDict]]]]] = ..., before_tool_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentBeforeToolCallbackArgs, AgentBeforeToolCallbackArgsDict]]]]] = ..., child_agents: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., guardrails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., instruction: Optional[pulumi.Input[_builtins.str]] = ..., llm_agent: Optional[pulumi.Input[Union[AgentLlmAgentArgs, AgentLlmAgentArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., model_settings: Optional[pulumi.Input[Union[AgentModelSettingsArgs, AgentModelSettingsArgsDict]]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., remote_dialogflow_agent: Optional[pulumi.Input[Union[AgentRemoteDialogflowAgentArgs, AgentRemoteDialogflowAgentArgsDict]]] = ..., tools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., toolsets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentToolsetArgs, AgentToolsetArgsDict]]]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AgentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., after_agent_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentAfterAgentCallbackArgs, AgentAfterAgentCallbackArgsDict]]]]] = ..., after_model_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentAfterModelCallbackArgs, AgentAfterModelCallbackArgsDict]]]]] = ..., after_tool_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentAfterToolCallbackArgs, AgentAfterToolCallbackArgsDict]]]]] = ..., agent_id: Optional[pulumi.Input[_builtins.str]] = ..., app: Optional[pulumi.Input[_builtins.str]] = ..., before_agent_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentBeforeAgentCallbackArgs, AgentBeforeAgentCallbackArgsDict]]]]] = ..., before_model_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentBeforeModelCallbackArgs, AgentBeforeModelCallbackArgsDict]]]]] = ..., before_tool_callbacks: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentBeforeToolCallbackArgs, AgentBeforeToolCallbackArgsDict]]]]] = ..., child_agents: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., create_time: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., display_name: Optional[pulumi.Input[_builtins.str]] = ..., etag: Optional[pulumi.Input[_builtins.str]] = ..., generated_summary: Optional[pulumi.Input[_builtins.str]] = ..., guardrails: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., instruction: Optional[pulumi.Input[_builtins.str]] = ..., llm_agent: Optional[pulumi.Input[Union[AgentLlmAgentArgs, AgentLlmAgentArgsDict]]] = ..., location: Optional[pulumi.Input[_builtins.str]] = ..., model_settings: Optional[pulumi.Input[Union[AgentModelSettingsArgs, AgentModelSettingsArgsDict]]] = ..., name: Optional[pulumi.Input[_builtins.str]] = ..., project: Optional[pulumi.Input[_builtins.str]] = ..., remote_dialogflow_agent: Optional[pulumi.Input[Union[AgentRemoteDialogflowAgentArgs, AgentRemoteDialogflowAgentArgsDict]]] = ..., tools: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ..., toolsets: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentToolsetArgs, AgentToolsetArgsDict]]]]] = ..., update_time: Optional[pulumi.Input[_builtins.str]] = ...) -> Agent:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterAgentCallbacks")
    def after_agent_callbacks(self) -> pulumi.Output[Optional[Sequence[outputs.AgentAfterAgentCallback]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterModelCallbacks")
    def after_model_callbacks(self) -> pulumi.Output[Optional[Sequence[outputs.AgentAfterModelCallback]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="afterToolCallbacks")
    def after_tool_callbacks(self) -> pulumi.Output[Optional[Sequence[outputs.AgentAfterToolCallback]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def app(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeAgentCallbacks")
    def before_agent_callbacks(self) -> pulumi.Output[Optional[Sequence[outputs.AgentBeforeAgentCallback]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeModelCallbacks")
    def before_model_callbacks(self) -> pulumi.Output[Optional[Sequence[outputs.AgentBeforeModelCallback]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="beforeToolCallbacks")
    def before_tool_callbacks(self) -> pulumi.Output[Optional[Sequence[outputs.AgentBeforeToolCallback]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="childAgents")
    def child_agents(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
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
    def etag(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="generatedSummary")
    def generated_summary(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def guardrails(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instruction(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="llmAgent")
    def llm_agent(self) -> pulumi.Output[Optional[outputs.AgentLlmAgent]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def location(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="modelSettings")
    def model_settings(self) -> pulumi.Output[Optional[outputs.AgentModelSettings]]:
        
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
    @pulumi.getter(name="remoteDialogflowAgent")
    def remote_dialogflow_agent(self) -> pulumi.Output[Optional[outputs.AgentRemoteDialogflowAgent]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def tools(self) -> pulumi.Output[Optional[Sequence[_builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def toolsets(self) -> pulumi.Output[Optional[Sequence[outputs.AgentToolset]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="updateTime")
    def update_time(self) -> pulumi.Output[_builtins.str]:
        
        ...
    


