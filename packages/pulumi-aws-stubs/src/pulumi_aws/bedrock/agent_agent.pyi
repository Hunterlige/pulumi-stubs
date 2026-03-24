

import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11):
    ...
else:
    ...
__all__ = ['AgentAgentArgs', 'AgentAgent']
@pulumi.input_type
class AgentAgentArgs:
    def __init__(__self__, *, agent_name: pulumi.Input[_builtins.str], agent_resource_role_arn: pulumi.Input[_builtins.str], foundation_model: pulumi.Input[_builtins.str], agent_collaboration: Optional[pulumi.Input[_builtins.str]] = ..., customer_encryption_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., guardrail_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentGuardrailConfigurationArgs]]]] = ..., idle_session_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., instruction: Optional[pulumi.Input[_builtins.str]] = ..., memory_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentMemoryConfigurationArgs]]]] = ..., prepare_agent: Optional[pulumi.Input[_builtins.bool]] = ..., prompt_override_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentPromptOverrideConfigurationArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., skip_resource_in_use_check: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[AgentAgentTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentName")
    def agent_name(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @agent_name.setter
    def agent_name(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentResourceRoleArn")
    def agent_resource_role_arn(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @agent_resource_role_arn.setter
    def agent_resource_role_arn(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="foundationModel")
    def foundation_model(self) -> pulumi.Input[_builtins.str]:
        
        ...
    
    @foundation_model.setter
    def foundation_model(self, value: pulumi.Input[_builtins.str]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentCollaboration")
    def agent_collaboration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_collaboration.setter
    def agent_collaboration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerEncryptionKeyArn")
    def customer_encryption_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_encryption_key_arn.setter
    def customer_encryption_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guardrailConfigurations")
    def guardrail_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentGuardrailConfigurationArgs]]]]:
        
        ...
    
    @guardrail_configurations.setter
    def guardrail_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentGuardrailConfigurationArgs]]]]): # -> None:
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
    def instruction(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instruction.setter
    def instruction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryConfigurations")
    def memory_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentMemoryConfigurationArgs]]]]:
        
        ...
    
    @memory_configurations.setter
    def memory_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentMemoryConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prepareAgent")
    def prepare_agent(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @prepare_agent.setter
    def prepare_agent(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="promptOverrideConfigurations")
    def prompt_override_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentPromptOverrideConfigurationArgs]]]]:
        
        ...
    
    @prompt_override_configurations.setter
    def prompt_override_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentPromptOverrideConfigurationArgs]]]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AgentAgentTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentAgentTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.input_type
class _AgentAgentState:
    def __init__(__self__, *, agent_arn: Optional[pulumi.Input[_builtins.str]] = ..., agent_collaboration: Optional[pulumi.Input[_builtins.str]] = ..., agent_id: Optional[pulumi.Input[_builtins.str]] = ..., agent_name: Optional[pulumi.Input[_builtins.str]] = ..., agent_resource_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., agent_version: Optional[pulumi.Input[_builtins.str]] = ..., customer_encryption_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., foundation_model: Optional[pulumi.Input[_builtins.str]] = ..., guardrail_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentGuardrailConfigurationArgs]]]] = ..., idle_session_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., instruction: Optional[pulumi.Input[_builtins.str]] = ..., memory_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentMemoryConfigurationArgs]]]] = ..., prepare_agent: Optional[pulumi.Input[_builtins.bool]] = ..., prepared_at: Optional[pulumi.Input[_builtins.str]] = ..., prompt_override_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentPromptOverrideConfigurationArgs]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., skip_resource_in_use_check: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[AgentAgentTimeoutsArgs]] = ...) -> None:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentArn")
    def agent_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_arn.setter
    def agent_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentCollaboration")
    def agent_collaboration(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_collaboration.setter
    def agent_collaboration(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_id.setter
    def agent_id(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentName")
    def agent_name(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_name.setter
    def agent_name(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentResourceRoleArn")
    def agent_resource_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_resource_role_arn.setter
    def agent_resource_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @agent_version.setter
    def agent_version(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerEncryptionKeyArn")
    def customer_encryption_key_arn(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @customer_encryption_key_arn.setter
    def customer_encryption_key_arn(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="foundationModel")
    def foundation_model(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @foundation_model.setter
    def foundation_model(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="guardrailConfigurations")
    def guardrail_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentGuardrailConfigurationArgs]]]]:
        
        ...
    
    @guardrail_configurations.setter
    def guardrail_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentGuardrailConfigurationArgs]]]]): # -> None:
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
    def instruction(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @instruction.setter
    def instruction(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryConfigurations")
    def memory_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentMemoryConfigurationArgs]]]]:
        
        ...
    
    @memory_configurations.setter
    def memory_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentMemoryConfigurationArgs]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="prepareAgent")
    def prepare_agent(self) -> Optional[pulumi.Input[_builtins.bool]]:
        
        ...
    
    @prepare_agent.setter
    def prepare_agent(self, value: Optional[pulumi.Input[_builtins.bool]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="preparedAt")
    def prepared_at(self) -> Optional[pulumi.Input[_builtins.str]]:
        
        ...
    
    @prepared_at.setter
    def prepared_at(self, value: Optional[pulumi.Input[_builtins.str]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="promptOverrideConfigurations")
    def prompt_override_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentPromptOverrideConfigurationArgs]]]]:
        
        ...
    
    @prompt_override_configurations.setter
    def prompt_override_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[AgentAgentPromptOverrideConfigurationArgs]]]]): # -> None:
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
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]:
        
        ...
    
    @tags_all.setter
    def tags_all(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]): # -> None:
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AgentAgentTimeoutsArgs]]:
        ...
    
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentAgentTimeoutsArgs]]): # -> None:
        ...
    


@pulumi.type_token("aws:bedrock/agentAgent:AgentAgent")
class AgentAgent(pulumi.CustomResource):
    @overload
    def __init__(__self__, resource_name: str, opts: Optional[pulumi.ResourceOptions] = ..., agent_collaboration: Optional[pulumi.Input[_builtins.str]] = ..., agent_name: Optional[pulumi.Input[_builtins.str]] = ..., agent_resource_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., customer_encryption_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., foundation_model: Optional[pulumi.Input[_builtins.str]] = ..., guardrail_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentAgentGuardrailConfigurationArgs, AgentAgentGuardrailConfigurationArgsDict]]]]] = ..., idle_session_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., instruction: Optional[pulumi.Input[_builtins.str]] = ..., memory_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentAgentMemoryConfigurationArgs, AgentAgentMemoryConfigurationArgsDict]]]]] = ..., prepare_agent: Optional[pulumi.Input[_builtins.bool]] = ..., prompt_override_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentAgentPromptOverrideConfigurationArgs, AgentAgentPromptOverrideConfigurationArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., skip_resource_in_use_check: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[AgentAgentTimeoutsArgs, AgentAgentTimeoutsArgsDict]]] = ..., __props__=...) -> None:
        
        ...
    
    @overload
    def __init__(__self__, resource_name: str, args: AgentAgentArgs, opts: Optional[pulumi.ResourceOptions] = ...) -> None:
        
        ...
    
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None:
        ...
    
    @staticmethod
    def get(resource_name: str, id: pulumi.Input[str], opts: Optional[pulumi.ResourceOptions] = ..., agent_arn: Optional[pulumi.Input[_builtins.str]] = ..., agent_collaboration: Optional[pulumi.Input[_builtins.str]] = ..., agent_id: Optional[pulumi.Input[_builtins.str]] = ..., agent_name: Optional[pulumi.Input[_builtins.str]] = ..., agent_resource_role_arn: Optional[pulumi.Input[_builtins.str]] = ..., agent_version: Optional[pulumi.Input[_builtins.str]] = ..., customer_encryption_key_arn: Optional[pulumi.Input[_builtins.str]] = ..., description: Optional[pulumi.Input[_builtins.str]] = ..., foundation_model: Optional[pulumi.Input[_builtins.str]] = ..., guardrail_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentAgentGuardrailConfigurationArgs, AgentAgentGuardrailConfigurationArgsDict]]]]] = ..., idle_session_ttl_in_seconds: Optional[pulumi.Input[_builtins.int]] = ..., instruction: Optional[pulumi.Input[_builtins.str]] = ..., memory_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentAgentMemoryConfigurationArgs, AgentAgentMemoryConfigurationArgsDict]]]]] = ..., prepare_agent: Optional[pulumi.Input[_builtins.bool]] = ..., prepared_at: Optional[pulumi.Input[_builtins.str]] = ..., prompt_override_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[Union[AgentAgentPromptOverrideConfigurationArgs, AgentAgentPromptOverrideConfigurationArgsDict]]]]] = ..., region: Optional[pulumi.Input[_builtins.str]] = ..., skip_resource_in_use_check: Optional[pulumi.Input[_builtins.bool]] = ..., tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., tags_all: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ..., timeouts: Optional[pulumi.Input[Union[AgentAgentTimeoutsArgs, AgentAgentTimeoutsArgsDict]]] = ...) -> AgentAgent:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentArn")
    def agent_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentCollaboration")
    def agent_collaboration(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentName")
    def agent_name(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentResourceRoleArn")
    def agent_resource_role_arn(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="agentVersion")
    def agent_version(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="customerEncryptionKeyArn")
    def customer_encryption_key_arn(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="foundationModel")
    def foundation_model(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="guardrailConfigurations")
    def guardrail_configurations(self) -> pulumi.Output[Optional[Sequence[outputs.AgentAgentGuardrailConfiguration]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="idleSessionTtlInSeconds")
    def idle_session_ttl_in_seconds(self) -> pulumi.Output[_builtins.int]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def instruction(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="memoryConfigurations")
    def memory_configurations(self) -> pulumi.Output[Sequence[outputs.AgentAgentMemoryConfiguration]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="prepareAgent")
    def prepare_agent(self) -> pulumi.Output[_builtins.bool]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="preparedAt")
    def prepared_at(self) -> pulumi.Output[_builtins.str]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="promptOverrideConfigurations")
    def prompt_override_configurations(self) -> pulumi.Output[Sequence[outputs.AgentAgentPromptOverrideConfiguration]]:
        
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
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]:
        
        ...
    
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.AgentAgentTimeouts]]:
        ...
    


