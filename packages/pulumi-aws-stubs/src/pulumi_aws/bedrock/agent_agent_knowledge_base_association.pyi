

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
__all__ = ['AgentAgentKnowledgeBaseAssociationArgs', 'AgentAgentKnowledgeBaseAssociation']
@pulumi.input_type
class AgentAgentKnowledgeBaseAssociationArgs:
    def __init__(__self__, *, agent_id: pulumi.Input[_builtins.str], description: pulumi.Input[_builtins.str], knowledge_base_id: pulumi.Input[_builtins.str], knowledge_base_state: pulumi.Input[_builtins.str], agent_version: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[AgentAgentKnowledgeBaseAssociationTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @agent_id.setter
    def agent_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @description.setter
    def description(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeBaseId")
    def knowledge_base_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @knowledge_base_id.setter
    def knowledge_base_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeBaseState")
    def knowledge_base_state(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @knowledge_base_state.setter
    def knowledge_base_state(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_version.setter
    def agent_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[AgentAgentKnowledgeBaseAssociationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentAgentKnowledgeBaseAssociationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AgentAgentKnowledgeBaseAssociationState:
    def __init__(__self__, *, agent_id: Optional[pulumi.Input[_builtins.str]] = ..., agent_version: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., knowledge_base_id: Optional[pulumi.Input[_builtins.str]] = ..., knowledge_base_state: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[AgentAgentKnowledgeBaseAssociationTimeoutsArgs]] = ...) -> None:
        
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
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeBaseId")
    def knowledge_base_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @knowledge_base_id.setter
    def knowledge_base_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeBaseState")
    def knowledge_base_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @knowledge_base_state.setter
    def knowledge_base_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    def timeouts(self) -> Optional[pulumi.Input[AgentAgentKnowledgeBaseAssociationTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentAgentKnowledgeBaseAssociationTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AgentAgentKnowledgeBaseAssociation(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., agent_id: Optional[pulumi.Input[_builtins.str]] = ..., agent_version: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., knowledge_base_id: Optional[pulumi.Input[_builtins.str]] = ..., knowledge_base_state: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[AgentAgentKnowledgeBaseAssociationTimeoutsArgs, AgentAgentKnowledgeBaseAssociationTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AgentAgentKnowledgeBaseAssociationArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., agent_id: Optional[pulumi.Input[_builtins.str]] = ..., agent_version: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., knowledge_base_id: Optional[pulumi.Input[_builtins.str]] = ..., knowledge_base_state: Optional[pulumi.Input[_builtins.str]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., timeouts: Optional[pulumi.Input[Union[AgentAgentKnowledgeBaseAssociationTimeoutsArgs, AgentAgentKnowledgeBaseAssociationTimeoutsArgsDict]]] = ...) -> AgentAgentKnowledgeBaseAssociation:
        
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
    @pulumi.getter
    def description(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeBaseId")
    def knowledge_base_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="knowledgeBaseState")
    def knowledge_base_state(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.AgentAgentKnowledgeBaseAssociationTimeouts]]:
        ...
    


