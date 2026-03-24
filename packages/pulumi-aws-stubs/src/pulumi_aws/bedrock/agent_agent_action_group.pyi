

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
__all__ = ['AgentAgentActionGroupArgs', 'AgentAgentActionGroup']
@pulumi.input_type
class AgentAgentActionGroupArgs:
    def __init__(__self__, *, action_group_name: pulumi.Input[_builtins.str], agent_id: pulumi.Input[_builtins.str], agent_version: pulumi.Input[_builtins.str], action_group_executor: Optional[pulumi.Input[AgentAgentActionGroupActionGroupExecutorArgs]] = ..., action_group_state: Optional[pulumi.Input[_builtins.str]] = ..., api_schema: Optional[pulumi.Input[AgentAgentActionGroupApiSchemaArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., function_schema: Optional[pulumi.Input[AgentAgentActionGroupFunctionSchemaArgs]] = ..., parent_action_group_signature: Optional[pulumi.Input[_builtins.str]] = ..., prepare_agent: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., skip_resource_in_use_check: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[AgentAgentActionGroupTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionGroupName")
    def action_group_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @action_group_name.setter
    def action_group_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @agent_id.setter
    def agent_id(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @agent_version.setter
    def agent_version(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionGroupExecutor")
    def action_group_executor(self) -> Optional[pulumi.Input[AgentAgentActionGroupActionGroupExecutorArgs]]:
        
        ...
    
    @action_group_executor.setter
    def action_group_executor(self, value: Optional[pulumi.Input[AgentAgentActionGroupActionGroupExecutorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionGroupState")
    def action_group_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action_group_state.setter
    def action_group_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="apiSchema")
    def api_schema(self) -> Optional[pulumi.Input[AgentAgentActionGroupApiSchemaArgs]]:
        
        ...
    
    @api_schema.setter
    def api_schema(self, value: Optional[pulumi.Input[AgentAgentActionGroupApiSchemaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionSchema")
    def function_schema(self) -> Optional[pulumi.Input[AgentAgentActionGroupFunctionSchemaArgs]]:
        
        ...
    
    @function_schema.setter
    def function_schema(self, value: Optional[pulumi.Input[AgentAgentActionGroupFunctionSchemaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentActionGroupSignature")
    def parent_action_group_signature(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent_action_group_signature.setter
    def parent_action_group_signature(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="skipResourceInUseCheck")
    def skip_resource_in_use_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_resource_in_use_check.setter
    def skip_resource_in_use_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AgentAgentActionGroupTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentAgentActionGroupTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AgentAgentActionGroupState:
    def __init__(__self__, *, action_group_executor: Optional[pulumi.Input[AgentAgentActionGroupActionGroupExecutorArgs]] = ..., action_group_id: Optional[pulumi.Input[_builtins.str]] = ..., action_group_name: Optional[pulumi.Input[_builtins.str]] = ..., action_group_state: Optional[pulumi.Input[_builtins.str]] = ..., agent_id: Optional[pulumi.Input[_builtins.str]] = ..., agent_version: Optional[pulumi.Input[_builtins.str]] = ..., api_schema: Optional[pulumi.Input[AgentAgentActionGroupApiSchemaArgs]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., function_schema: Optional[pulumi.Input[AgentAgentActionGroupFunctionSchemaArgs]] = ..., parent_action_group_signature: Optional[pulumi.Input[_builtins.str]] = ..., prepare_agent: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., skip_resource_in_use_check: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[AgentAgentActionGroupTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionGroupExecutor")
    def action_group_executor(self) -> Optional[pulumi.Input[AgentAgentActionGroupActionGroupExecutorArgs]]:
        
        ...
    
    @action_group_executor.setter
    def action_group_executor(self, value: Optional[pulumi.Input[AgentAgentActionGroupActionGroupExecutorArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionGroupId")
    def action_group_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action_group_id.setter
    def action_group_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionGroupName")
    def action_group_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action_group_name.setter
    def action_group_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionGroupState")
    def action_group_state(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @action_group_state.setter
    def action_group_state(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="apiSchema")
    def api_schema(self) -> Optional[pulumi.Input[AgentAgentActionGroupApiSchemaArgs]]:
        
        ...
    
    @api_schema.setter
    def api_schema(self, value: Optional[pulumi.Input[AgentAgentActionGroupApiSchemaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionSchema")
    def function_schema(self) -> Optional[pulumi.Input[AgentAgentActionGroupFunctionSchemaArgs]]:
        
        ...
    
    @function_schema.setter
    def function_schema(self, value: Optional[pulumi.Input[AgentAgentActionGroupFunctionSchemaArgs]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentActionGroupSignature")
    def parent_action_group_signature(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @parent_action_group_signature.setter
    def parent_action_group_signature(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
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
    @pulumi.getter(name="skipResourceInUseCheck")
    def skip_resource_in_use_check(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @skip_resource_in_use_check.setter
    def skip_resource_in_use_check(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AgentAgentActionGroupTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentAgentActionGroupTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token(...)
class AgentAgentActionGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., action_group_executor: Optional[pulumi.Input[Union[AgentAgentActionGroupActionGroupExecutorArgs, AgentAgentActionGroupActionGroupExecutorArgsDict]]] = ..., action_group_name: Optional[pulumi.Input[_builtins.str]] = ..., action_group_state: Optional[pulumi.Input[_builtins.str]] = ..., agent_id: Optional[pulumi.Input[_builtins.str]] = ..., agent_version: Optional[pulumi.Input[_builtins.str]] = ..., api_schema: Optional[pulumi.Input[Union[AgentAgentActionGroupApiSchemaArgs, AgentAgentActionGroupApiSchemaArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., function_schema: Optional[pulumi.Input[Union[AgentAgentActionGroupFunctionSchemaArgs, AgentAgentActionGroupFunctionSchemaArgsDict]]] = ..., parent_action_group_signature: Optional[pulumi.Input[_builtins.str]] = ..., prepare_agent: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., skip_resource_in_use_check: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[Union[AgentAgentActionGroupTimeoutsArgs, AgentAgentActionGroupTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AgentAgentActionGroupArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., action_group_executor: Optional[pulumi.Input[Union[AgentAgentActionGroupActionGroupExecutorArgs, AgentAgentActionGroupActionGroupExecutorArgsDict]]] = ..., action_group_id: Optional[pulumi.Input[_builtins.str]] = ..., action_group_name: Optional[pulumi.Input[_builtins.str]] = ..., action_group_state: Optional[pulumi.Input[_builtins.str]] = ..., agent_id: Optional[pulumi.Input[_builtins.str]] = ..., agent_version: Optional[pulumi.Input[_builtins.str]] = ..., api_schema: Optional[pulumi.Input[Union[AgentAgentActionGroupApiSchemaArgs, AgentAgentActionGroupApiSchemaArgsDict]]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., function_schema: Optional[pulumi.Input[Union[AgentAgentActionGroupFunctionSchemaArgs, AgentAgentActionGroupFunctionSchemaArgsDict]]] = ..., parent_action_group_signature: Optional[pulumi.Input[_builtins.str]] = ..., prepare_agent: Optional[pulumi.Input[_builtins.bool]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., skip_resource_in_use_check: Optional[pulumi.Input[_builtins.bool]] = ..., timeouts: Optional[pulumi.Input[Union[AgentAgentActionGroupTimeoutsArgs, AgentAgentActionGroupTimeoutsArgsDict]]] = ...) -> AgentAgentActionGroup:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionGroupExecutor")
    def action_group_executor(self) -> pulumi.Output[Optional[outputs.AgentAgentActionGroupActionGroupExecutor]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionGroupId")
    def action_group_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionGroupName")
    def action_group_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="actionGroupState")
    def action_group_state(self) -> pulumi.Output[_builtins.str]:
        
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
    @pulumi.getter(name="apiSchema")
    def api_schema(self) -> pulumi.Output[Optional[outputs.AgentAgentActionGroupApiSchema]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="functionSchema")
    def function_schema(self) -> pulumi.Output[Optional[outputs.AgentAgentActionGroupFunctionSchema]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="parentActionGroupSignature")
    def parent_action_group_signature(self) -> pulumi.Output[Optional[_builtins.str]]:
        
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
    @pulumi.getter(name="skipResourceInUseCheck")
    def skip_resource_in_use_check(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.AgentAgentActionGroupTimeouts]]:
        ...
    


