import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["AgentcoreMemoryStrategyArgs", "AgentcoreMemoryStrategy"]

@pulumi.input_type
class AgentcoreMemoryStrategyArgs:
    def __init__(
        __self__,
        *,
        memory_id: pulumi.Input[_builtins.str],
        namespaces: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]],
        type: pulumi.Input[_builtins.str],
        configuration: Optional[
            pulumi.Input[AgentcoreMemoryStrategyConfigurationArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[AgentcoreMemoryStrategyTimeoutsArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="memoryId")
    def memory_id(self) -> pulumi.Input[_builtins.str]: ...
    @memory_id.setter
    def memory_id(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def namespaces(self) -> pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]: ...
    @namespaces.setter
    def namespaces(
        self, value: pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[pulumi.Input[AgentcoreMemoryStrategyConfigurationArgs]]: ...
    @configuration.setter
    def configuration(
        self, value: Optional[pulumi.Input[AgentcoreMemoryStrategyConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryExecutionRoleArn")
    def memory_execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory_execution_role_arn.setter
    def memory_execution_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[AgentcoreMemoryStrategyTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[AgentcoreMemoryStrategyTimeoutsArgs]]
    ): ...

@pulumi.input_type
class _AgentcoreMemoryStrategyState:
    def __init__(
        __self__,
        *,
        configuration: Optional[
            pulumi.Input[AgentcoreMemoryStrategyConfigurationArgs]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_strategy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespaces: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[pulumi.Input[AgentcoreMemoryStrategyTimeoutsArgs]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> Optional[pulumi.Input[AgentcoreMemoryStrategyConfigurationArgs]]: ...
    @configuration.setter
    def configuration(
        self, value: Optional[pulumi.Input[AgentcoreMemoryStrategyConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryExecutionRoleArn")
    def memory_execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory_execution_role_arn.setter
    def memory_execution_role_arn(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="memoryId")
    def memory_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory_id.setter
    def memory_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="memoryStrategyId")
    def memory_strategy_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory_strategy_id.setter
    def memory_strategy_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def namespaces(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @namespaces.setter
    def namespaces(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> Optional[pulumi.Input[AgentcoreMemoryStrategyTimeoutsArgs]]: ...
    @timeouts.setter
    def timeouts(
        self, value: Optional[pulumi.Input[AgentcoreMemoryStrategyTimeoutsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

@pulumi.type_token(...)
class AgentcoreMemoryStrategy(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        configuration: Optional[
            pulumi.Input[
                Union[
                    AgentcoreMemoryStrategyConfigurationArgs,
                    AgentcoreMemoryStrategyConfigurationArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespaces: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    AgentcoreMemoryStrategyTimeoutsArgs,
                    AgentcoreMemoryStrategyTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: AgentcoreMemoryStrategyArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        configuration: Optional[
            pulumi.Input[
                Union[
                    AgentcoreMemoryStrategyConfigurationArgs,
                    AgentcoreMemoryStrategyConfigurationArgsDict,
                ]
            ]
        ] = ...,
        description: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_id: Optional[pulumi.Input[_builtins.str]] = ...,
        memory_strategy_id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        namespaces: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        timeouts: Optional[
            pulumi.Input[
                Union[
                    AgentcoreMemoryStrategyTimeoutsArgs,
                    AgentcoreMemoryStrategyTimeoutsArgsDict,
                ]
            ]
        ] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> AgentcoreMemoryStrategy: ...
    @_builtins.property
    @pulumi.getter
    def configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.AgentcoreMemoryStrategyConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="memoryExecutionRoleArn")
    def memory_execution_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="memoryId")
    def memory_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="memoryStrategyId")
    def memory_strategy_id(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def namespaces(self) -> pulumi.Output[Sequence[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def timeouts(
        self,
    ) -> pulumi.Output[Optional[outputs.AgentcoreMemoryStrategyTimeouts]]: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Output[_builtins.str]: ...
