import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTaskExecutionResult",
    "AwaitableGetTaskExecutionResult",
    "get_task_execution",
    "get_task_execution_output",
]

@pulumi.output_type
class GetTaskExecutionResult:
    def __init__(
        __self__,
        capacity_provider_strategies=...,
        client_token=...,
        cluster=...,
        desired_count=...,
        enable_ecs_managed_tags=...,
        enable_execute_command=...,
        group=...,
        id=...,
        launch_type=...,
        network_configuration=...,
        overrides=...,
        placement_constraints=...,
        placement_strategies=...,
        platform_version=...,
        propagate_tags=...,
        reference_id=...,
        region=...,
        started_by=...,
        tags=...,
        task_arns=...,
        task_definition=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="capacityProviderStrategies")
    def capacity_provider_strategies(
        self,
    ) -> Optional[Sequence[outputs.GetTaskExecutionCapacityProviderStrategyResult]]: ...
    @_builtins.property
    @pulumi.getter(name="clientToken")
    def client_token(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cluster(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="desiredCount")
    def desired_count(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="enableEcsManagedTags")
    def enable_ecs_managed_tags(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="enableExecuteCommand")
    def enable_execute_command(self) -> Optional[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter
    def group(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="launchType")
    def launch_type(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="networkConfiguration")
    def network_configuration(
        self,
    ) -> Optional[outputs.GetTaskExecutionNetworkConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter
    def overrides(self) -> Optional[outputs.GetTaskExecutionOverridesResult]: ...
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(
        self,
    ) -> Optional[Sequence[outputs.GetTaskExecutionPlacementConstraintResult]]: ...
    @_builtins.property
    @pulumi.getter(name="placementStrategies")
    def placement_strategies(
        self,
    ) -> Optional[Sequence[outputs.GetTaskExecutionPlacementStrategyResult]]: ...
    @_builtins.property
    @pulumi.getter(name="platformVersion")
    def platform_version(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="propagateTags")
    def propagate_tags(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="referenceId")
    def reference_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="startedBy")
    def started_by(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="taskArns")
    def task_arns(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="taskDefinition")
    def task_definition(self) -> _builtins.str: ...

class AwaitableGetTaskExecutionResult(GetTaskExecutionResult):
    def __await__(self): ...

def get_task_execution(
    capacity_provider_strategies: Optional[
        Sequence[
            Union[
                GetTaskExecutionCapacityProviderStrategyArgs,
                GetTaskExecutionCapacityProviderStrategyArgsDict,
            ]
        ]
    ] = ...,
    client_token: Optional[_builtins.str] = ...,
    cluster: Optional[_builtins.str] = ...,
    desired_count: Optional[_builtins.int] = ...,
    enable_ecs_managed_tags: Optional[_builtins.bool] = ...,
    enable_execute_command: Optional[_builtins.bool] = ...,
    group: Optional[_builtins.str] = ...,
    launch_type: Optional[_builtins.str] = ...,
    network_configuration: Optional[
        Union[
            GetTaskExecutionNetworkConfigurationArgs,
            GetTaskExecutionNetworkConfigurationArgsDict,
        ]
    ] = ...,
    overrides: Optional[
        Union[GetTaskExecutionOverridesArgs, GetTaskExecutionOverridesArgsDict]
    ] = ...,
    placement_constraints: Optional[
        Sequence[
            Union[
                GetTaskExecutionPlacementConstraintArgs,
                GetTaskExecutionPlacementConstraintArgsDict,
            ]
        ]
    ] = ...,
    placement_strategies: Optional[
        Sequence[
            Union[
                GetTaskExecutionPlacementStrategyArgs,
                GetTaskExecutionPlacementStrategyArgsDict,
            ]
        ]
    ] = ...,
    platform_version: Optional[_builtins.str] = ...,
    propagate_tags: Optional[_builtins.str] = ...,
    reference_id: Optional[_builtins.str] = ...,
    region: Optional[_builtins.str] = ...,
    started_by: Optional[_builtins.str] = ...,
    tags: Optional[Mapping[str, _builtins.str]] = ...,
    task_definition: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTaskExecutionResult: ...
def get_task_execution_output(
    capacity_provider_strategies: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetTaskExecutionCapacityProviderStrategyArgs,
                        GetTaskExecutionCapacityProviderStrategyArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    client_token: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    cluster: Optional[pulumi.Input[_builtins.str]] = ...,
    desired_count: Optional[pulumi.Input[Optional[_builtins.int]]] = ...,
    enable_ecs_managed_tags: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    enable_execute_command: Optional[pulumi.Input[Optional[_builtins.bool]]] = ...,
    group: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    launch_type: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    network_configuration: Optional[
        pulumi.Input[
            Optional[
                Union[
                    GetTaskExecutionNetworkConfigurationArgs,
                    GetTaskExecutionNetworkConfigurationArgsDict,
                ]
            ]
        ]
    ] = ...,
    overrides: Optional[
        pulumi.Input[
            Optional[
                Union[GetTaskExecutionOverridesArgs, GetTaskExecutionOverridesArgsDict]
            ]
        ]
    ] = ...,
    placement_constraints: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetTaskExecutionPlacementConstraintArgs,
                        GetTaskExecutionPlacementConstraintArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    placement_strategies: Optional[
        pulumi.Input[
            Optional[
                Sequence[
                    Union[
                        GetTaskExecutionPlacementStrategyArgs,
                        GetTaskExecutionPlacementStrategyArgsDict,
                    ]
                ]
            ]
        ]
    ] = ...,
    platform_version: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    propagate_tags: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    reference_id: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    started_by: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    tags: Optional[pulumi.Input[Optional[Mapping[str, _builtins.str]]]] = ...,
    task_definition: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTaskExecutionResult]: ...
