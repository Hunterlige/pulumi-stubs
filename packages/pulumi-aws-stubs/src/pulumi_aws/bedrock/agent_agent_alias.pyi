import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AgentAgentAliasArgs", "AgentAgentAlias"]

@pulumi.input_type
class AgentAgentAliasArgs:
    def __init__(
        __self__,
        *,
        agent_alias_name: pulumi.Input[_builtins.str],
        agent_id: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AgentAgentAliasRoutingConfigurationArgs]]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[pulumi.Input[AgentAgentAliasTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentAliasName")
    def agent_alias_name(self) -> pulumi.Input[_builtins.str]: ...
    @agent_alias_name.setter
    def agent_alias_name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Input[_builtins.str]: ...
    @agent_id.setter
    def agent_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingConfigurations")
    def routing_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AgentAgentAliasRoutingConfigurationArgs]]]
    ]: ...
    @routing_configurations.setter
    def routing_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AgentAgentAliasRoutingConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AgentAgentAliasTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentAgentAliasTimeoutsArgs]]): ...

@pulumi.input_type
class _AgentAgentAliasState:
    def __init__(
        __self__,
        *,
        agent_alias_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        agent_alias_id: Optional[pulumi.Input[_builtins.str]] = ...,
        agent_alias_name: Optional[pulumi.Input[_builtins.str]] = ...,
        agent_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_configurations: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AgentAgentAliasRoutingConfigurationArgs]]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[pulumi.Input[AgentAgentAliasTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="agentAliasArn")
    def agent_alias_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_alias_arn.setter
    def agent_alias_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="agentAliasId")
    def agent_alias_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_alias_id.setter
    def agent_alias_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="agentAliasName")
    def agent_alias_name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_alias_name.setter
    def agent_alias_name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @agent_id.setter
    def agent_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="routingConfigurations")
    def routing_configurations(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[AgentAgentAliasRoutingConfigurationArgs]]]
    ]: ...
    @routing_configurations.setter
    def routing_configurations(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[AgentAgentAliasRoutingConfigurationArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def tags(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @tags_all.setter
    def tags_all(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> Optional[pulumi.Input[AgentAgentAliasTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(self, value: Optional[pulumi.Input[AgentAgentAliasTimeoutsArgs]]): ...

@pulumi.type_token("aws:bedrock/agentAgentAlias:AgentAgentAlias")
class AgentAgentAlias(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        agent_alias_name: Optional[pulumi.Input[_builtins.str]] = ...,
        agent_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AgentAgentAliasRoutingConfigurationArgs,
                            AgentAgentAliasRoutingConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[AgentAgentAliasTimeoutsArgs, AgentAgentAliasTimeoutsArgsDict]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AgentAgentAliasArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        agent_alias_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        agent_alias_id: Optional[pulumi.Input[_builtins.str]] = ...,
        agent_alias_name: Optional[pulumi.Input[_builtins.str]] = ...,
        agent_id: Optional[pulumi.Input[_builtins.str]] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        routing_configurations: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            AgentAgentAliasRoutingConfigurationArgs,
                            AgentAgentAliasRoutingConfigurationArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[AgentAgentAliasTimeoutsArgs, AgentAgentAliasTimeoutsArgsDict]
            ]
        ] = ...,
    ) -> AgentAgentAlias: ...
    @_builtins.property
    @pulumi.getter(name="agentAliasArn")
    def agent_alias_arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="agentAliasId")
    def agent_alias_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="agentAliasName")
    def agent_alias_name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="agentId")
    def agent_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="routingConfigurations")
    def routing_configurations(
        self,
    ) -> pulumi.Output[Sequence[outputs.AgentAgentAliasRoutingConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(self) -> pulumi.Output[Optional[outputs.AgentAgentAliasTimeouts]]: ...
