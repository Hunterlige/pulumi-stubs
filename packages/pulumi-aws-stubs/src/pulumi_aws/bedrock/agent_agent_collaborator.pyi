

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
__all__ = ['AgentAgentCollaboratorArgs', 'AgentAgentCollaborator']
@pulumi.input_type
class AgentAgentCollaboratorArgs:
    def __init__(__self__, *, agent_descriptor: pulumi.Input[AgentAgentCollaboratorAgentDescriptorArgs], agent_id: pulumi.Input[_builtins.str], collaboration_instruction: pulumi.Input[_builtins.str], collaborator_name: pulumi.Input[_builtins.str], agent_version: Optional[pulumi.Input[_builtins.str]] = ..., prepare_agent: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., relay_conversation_history: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[AgentAgentCollaboratorTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentDescriptor")
    def agent_descriptor(self) -> pulumi.Input[AgentAgentCollaboratorAgentDescriptorArgs]:
        ...
    
    @agent_descriptor.setter
    def agent_descriptor(self, value: pulumi.Input[AgentAgentCollaboratorAgentDescriptorArgs]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @agent_id.setter
    def agent_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collaborationInstruction")
    def collaboration_instruction(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @collaboration_instruction.setter
    def collaboration_instruction(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collaboratorName")
    def collaborator_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @collaborator_name.setter
    def collaborator_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @agent_version.setter
    def agent_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prepareAgent")
    def prepare_agent(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @prepare_agent.setter
    def prepare_agent(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relayConversationHistory")
    def relay_conversation_history(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @relay_conversation_history.setter
    def relay_conversation_history(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AgentAgentCollaboratorTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentAgentCollaboratorTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AgentAgentCollaboratorState:
    def __init__(__self__, *, agent_descriptor: Optional[pulumi.Input[AgentAgentCollaboratorAgentDescriptorArgs]] = ..., agent_id: Optional[pulumi.Input[_builtins.str]] = ..., agent_version: Optional[pulumi.Input[_builtins.str]] = ..., collaboration_instruction: Optional[pulumi.Input[_builtins.str]] = ..., collaborator_id: Optional[pulumi.Input[_builtins.str]] = ..., collaborator_name: Optional[pulumi.Input[_builtins.str]] = ..., prepare_agent: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., relay_conversation_history: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[AgentAgentCollaboratorTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentDescriptor")
    def agent_descriptor(self) -> Optional[pulumi.Input[AgentAgentCollaboratorAgentDescriptorArgs]]:
        ...
    
    @agent_descriptor.setter
    def agent_descriptor(self, value: Optional[pulumi.Input[AgentAgentCollaboratorAgentDescriptorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_id.setter
    def agent_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        ...
    
    @agent_version.setter
    def agent_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collaborationInstruction")
    def collaboration_instruction(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collaboration_instruction.setter
    def collaboration_instruction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collaboratorId")
    def collaborator_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collaborator_id.setter
    def collaborator_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collaboratorName")
    def collaborator_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @collaborator_name.setter
    def collaborator_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prepareAgent")
    def prepare_agent(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @prepare_agent.setter
    def prepare_agent(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="relayConversationHistory")
    def relay_conversation_history(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @relay_conversation_history.setter
    def relay_conversation_history(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AgentAgentCollaboratorTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentAgentCollaboratorTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AgentAgentCollaborator(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., agent_descriptor: Optional[pulumi.Input[Union[AgentAgentCollaboratorAgentDescriptorArgs, AgentAgentCollaboratorAgentDescriptorArgsDict]]] = ..., agent_id: Optional[pulumi.Input[_builtins.str]] = ..., agent_version: Optional[pulumi.Input[_builtins.str]] = ..., collaboration_instruction: Optional[pulumi.Input[_builtins.str]] = ..., collaborator_name: Optional[pulumi.Input[_builtins.str]] = ..., prepare_agent: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., relay_conversation_history: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[AgentAgentCollaboratorTimeoutsArgs, AgentAgentCollaboratorTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AgentAgentCollaboratorArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., agent_descriptor: Optional[pulumi.Input[Union[AgentAgentCollaboratorAgentDescriptorArgs, AgentAgentCollaboratorAgentDescriptorArgsDict]]] = ..., agent_id: Optional[pulumi.Input[_builtins.str]] = ..., agent_version: Optional[pulumi.Input[_builtins.str]] = ..., collaboration_instruction: Optional[pulumi.Input[_builtins.str]] = ..., collaborator_id: Optional[pulumi.Input[_builtins.str]] = ..., collaborator_name: Optional[pulumi.Input[_builtins.str]] = ..., prepare_agent: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., relay_conversation_history: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[AgentAgentCollaboratorTimeoutsArgs, AgentAgentCollaboratorTimeoutsArgsDict]]] = ...) -> AgentAgentCollaborator:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentDescriptor")
    def agent_descriptor(self) -> pulumi.Output[outputs.AgentAgentCollaboratorAgentDescriptor]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> pulumi.Output[_builtins.str]:
        ...
    
    @_builtins.property
    @pulumi.getter(name="collaborationInstruction")
    def collaboration_instruction(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collaboratorId")
    def collaborator_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="collaboratorName")
    def collaborator_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prepareAgent")
    def prepare_agent(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="relayConversationHistory")
    def relay_conversation_history(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.AgentAgentCollaboratorTimeouts]]:
        ...
    


