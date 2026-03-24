import builtins as _builtins
import sys
import pulumi
from typing import Mapping, Optional, Sequence, Union, overload
from . import outputs
from ._inputs import *

if sys.version_info >= (3, 11): ...
else: ...
__all__ = ["TaskDefinitionArgs", "TaskDefinition"]

@pulumi.input_type
class TaskDefinitionArgs:
    def __init__(
        __self__,
        *,
        container_definitions: pulumi.Input[_builtins.str],
        family: pulumi.Input[_builtins.str],
        cpu: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_fault_injection: Optional[pulumi.Input[_builtins.bool]] = ...,
        ephemeral_storage: Optional[
            pulumi.Input[TaskDefinitionEphemeralStorageArgs]
        ] = ...,
        execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        ipc_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        memory: Optional[pulumi.Input[_builtins.str]] = ...,
        network_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        pid_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        placement_constraints: Optional[
            pulumi.Input[Sequence[pulumi.Input[TaskDefinitionPlacementConstraintArgs]]]
        ] = ...,
        proxy_configuration: Optional[
            pulumi.Input[TaskDefinitionProxyConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requires_compatibilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        runtime_platform: Optional[
            pulumi.Input[TaskDefinitionRuntimePlatformArgs]
        ] = ...,
        skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        task_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        track_latest: Optional[pulumi.Input[_builtins.bool]] = ...,
        volumes: Optional[
            pulumi.Input[Sequence[pulumi.Input[TaskDefinitionVolumeArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerDefinitions")
    def container_definitions(self) -> pulumi.Input[_builtins.str]: ...
    @container_definitions.setter
    def container_definitions(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> pulumi.Input[_builtins.str]: ...
    @family.setter
    def family(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableFaultInjection")
    def enable_fault_injection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_fault_injection.setter
    def enable_fault_injection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(
        self,
    ) -> Optional[pulumi.Input[TaskDefinitionEphemeralStorageArgs]]: ...
    @ephemeral_storage.setter
    def ephemeral_storage(
        self, value: Optional[pulumi.Input[TaskDefinitionEphemeralStorageArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipcMode")
    def ipc_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipc_mode.setter
    def ipc_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkMode")
    def network_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_mode.setter
    def network_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pidMode")
    def pid_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pid_mode.setter
    def pid_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TaskDefinitionPlacementConstraintArgs]]]
    ]: ...
    @placement_constraints.setter
    def placement_constraints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TaskDefinitionPlacementConstraintArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="proxyConfiguration")
    def proxy_configuration(
        self,
    ) -> Optional[pulumi.Input[TaskDefinitionProxyConfigurationArgs]]: ...
    @proxy_configuration.setter
    def proxy_configuration(
        self, value: Optional[pulumi.Input[TaskDefinitionProxyConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requiresCompatibilities")
    def requires_compatibilities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @requires_compatibilities.setter
    def requires_compatibilities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="runtimePlatform")
    def runtime_platform(
        self,
    ) -> Optional[pulumi.Input[TaskDefinitionRuntimePlatformArgs]]: ...
    @runtime_platform.setter
    def runtime_platform(
        self, value: Optional[pulumi.Input[TaskDefinitionRuntimePlatformArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_destroy.setter
    def skip_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="taskRoleArn")
    def task_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @task_role_arn.setter
    def task_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trackLatest")
    def track_latest(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @track_latest.setter
    def track_latest(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TaskDefinitionVolumeArgs]]]]: ...
    @volumes.setter
    def volumes(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[TaskDefinitionVolumeArgs]]]],
    ): ...

@pulumi.input_type
class _TaskDefinitionState:
    def __init__(
        __self__,
        *,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        arn_without_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        container_definitions: Optional[pulumi.Input[_builtins.str]] = ...,
        cpu: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_fault_injection: Optional[pulumi.Input[_builtins.bool]] = ...,
        ephemeral_storage: Optional[
            pulumi.Input[TaskDefinitionEphemeralStorageArgs]
        ] = ...,
        execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        family: Optional[pulumi.Input[_builtins.str]] = ...,
        ipc_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        memory: Optional[pulumi.Input[_builtins.str]] = ...,
        network_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        pid_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        placement_constraints: Optional[
            pulumi.Input[Sequence[pulumi.Input[TaskDefinitionPlacementConstraintArgs]]]
        ] = ...,
        proxy_configuration: Optional[
            pulumi.Input[TaskDefinitionProxyConfigurationArgs]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requires_compatibilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        revision: Optional[pulumi.Input[_builtins.int]] = ...,
        runtime_platform: Optional[
            pulumi.Input[TaskDefinitionRuntimePlatformArgs]
        ] = ...,
        skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        task_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        track_latest: Optional[pulumi.Input[_builtins.bool]] = ...,
        volumes: Optional[
            pulumi.Input[Sequence[pulumi.Input[TaskDefinitionVolumeArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn.setter
    def arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="arnWithoutRevision")
    def arn_without_revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @arn_without_revision.setter
    def arn_without_revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="containerDefinitions")
    def container_definitions(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @container_definitions.setter
    def container_definitions(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @cpu.setter
    def cpu(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableFaultInjection")
    def enable_fault_injection(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_fault_injection.setter
    def enable_fault_injection(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(
        self,
    ) -> Optional[pulumi.Input[TaskDefinitionEphemeralStorageArgs]]: ...
    @ephemeral_storage.setter
    def ephemeral_storage(
        self, value: Optional[pulumi.Input[TaskDefinitionEphemeralStorageArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_role_arn.setter
    def execution_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @family.setter
    def family(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="ipcMode")
    def ipc_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @ipc_mode.setter
    def ipc_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @memory.setter
    def memory(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkMode")
    def network_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network_mode.setter
    def network_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="pidMode")
    def pid_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @pid_mode.setter
    def pid_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[TaskDefinitionPlacementConstraintArgs]]]
    ]: ...
    @placement_constraints.setter
    def placement_constraints(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[TaskDefinitionPlacementConstraintArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="proxyConfiguration")
    def proxy_configuration(
        self,
    ) -> Optional[pulumi.Input[TaskDefinitionProxyConfigurationArgs]]: ...
    @proxy_configuration.setter
    def proxy_configuration(
        self, value: Optional[pulumi.Input[TaskDefinitionProxyConfigurationArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @region.setter
    def region(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="requiresCompatibilities")
    def requires_compatibilities(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @requires_compatibilities.setter
    def requires_compatibilities(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="runtimePlatform")
    def runtime_platform(
        self,
    ) -> Optional[pulumi.Input[TaskDefinitionRuntimePlatformArgs]]: ...
    @runtime_platform.setter
    def runtime_platform(
        self, value: Optional[pulumi.Input[TaskDefinitionRuntimePlatformArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @skip_destroy.setter
    def skip_destroy(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
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
    @pulumi.getter(name="taskRoleArn")
    def task_role_arn(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @task_role_arn.setter
    def task_role_arn(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="trackLatest")
    def track_latest(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @track_latest.setter
    def track_latest(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[TaskDefinitionVolumeArgs]]]]: ...
    @volumes.setter
    def volumes(
        self,
        value: Optional[pulumi.Input[Sequence[pulumi.Input[TaskDefinitionVolumeArgs]]]],
    ): ...

@pulumi.type_token("aws:ecs/taskDefinition:TaskDefinition")
class TaskDefinition(pulumi.CustomResource):
    @overload
    def __init__(
        __self__,
        resource_name: str,
        opts: Optional[pulumi.ResourceOptions] = ...,
        container_definitions: Optional[pulumi.Input[_builtins.str]] = ...,
        cpu: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_fault_injection: Optional[pulumi.Input[_builtins.bool]] = ...,
        ephemeral_storage: Optional[
            pulumi.Input[
                Union[
                    TaskDefinitionEphemeralStorageArgs,
                    TaskDefinitionEphemeralStorageArgsDict,
                ]
            ]
        ] = ...,
        execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        family: Optional[pulumi.Input[_builtins.str]] = ...,
        ipc_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        memory: Optional[pulumi.Input[_builtins.str]] = ...,
        network_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        pid_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        placement_constraints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            TaskDefinitionPlacementConstraintArgs,
                            TaskDefinitionPlacementConstraintArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        proxy_configuration: Optional[
            pulumi.Input[
                Union[
                    TaskDefinitionProxyConfigurationArgs,
                    TaskDefinitionProxyConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requires_compatibilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        runtime_platform: Optional[
            pulumi.Input[
                Union[
                    TaskDefinitionRuntimePlatformArgs,
                    TaskDefinitionRuntimePlatformArgsDict,
                ]
            ]
        ] = ...,
        skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        task_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        track_latest: Optional[pulumi.Input[_builtins.bool]] = ...,
        volumes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TaskDefinitionVolumeArgs, TaskDefinitionVolumeArgsDict]
                    ]
                ]
            ]
        ] = ...,
        __props__=...,
    ) -> None: ...
    @overload
    def __init__(
        __self__,
        resource_name: str,
        args: TaskDefinitionArgs,
        opts: Optional[pulumi.ResourceOptions] = ...,
    ) -> None: ...
    def __init__(__self__, resource_name: str, *args, **kwargs) -> None: ...
    @staticmethod
    def get(
        resource_name: str,
        id: pulumi.Input[str],
        opts: Optional[pulumi.ResourceOptions] = ...,
        arn: Optional[pulumi.Input[_builtins.str]] = ...,
        arn_without_revision: Optional[pulumi.Input[_builtins.str]] = ...,
        container_definitions: Optional[pulumi.Input[_builtins.str]] = ...,
        cpu: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_fault_injection: Optional[pulumi.Input[_builtins.bool]] = ...,
        ephemeral_storage: Optional[
            pulumi.Input[
                Union[
                    TaskDefinitionEphemeralStorageArgs,
                    TaskDefinitionEphemeralStorageArgsDict,
                ]
            ]
        ] = ...,
        execution_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        family: Optional[pulumi.Input[_builtins.str]] = ...,
        ipc_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        memory: Optional[pulumi.Input[_builtins.str]] = ...,
        network_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        pid_mode: Optional[pulumi.Input[_builtins.str]] = ...,
        placement_constraints: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[
                            TaskDefinitionPlacementConstraintArgs,
                            TaskDefinitionPlacementConstraintArgsDict,
                        ]
                    ]
                ]
            ]
        ] = ...,
        proxy_configuration: Optional[
            pulumi.Input[
                Union[
                    TaskDefinitionProxyConfigurationArgs,
                    TaskDefinitionProxyConfigurationArgsDict,
                ]
            ]
        ] = ...,
        region: Optional[pulumi.Input[_builtins.str]] = ...,
        requires_compatibilities: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        revision: Optional[pulumi.Input[_builtins.int]] = ...,
        runtime_platform: Optional[
            pulumi.Input[
                Union[
                    TaskDefinitionRuntimePlatformArgs,
                    TaskDefinitionRuntimePlatformArgsDict,
                ]
            ]
        ] = ...,
        skip_destroy: Optional[pulumi.Input[_builtins.bool]] = ...,
        tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        tags_all: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        task_role_arn: Optional[pulumi.Input[_builtins.str]] = ...,
        track_latest: Optional[pulumi.Input[_builtins.bool]] = ...,
        volumes: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        Union[TaskDefinitionVolumeArgs, TaskDefinitionVolumeArgsDict]
                    ]
                ]
            ]
        ] = ...,
    ) -> TaskDefinition: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="arnWithoutRevision")
    def arn_without_revision(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="containerDefinitions")
    def container_definitions(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="enableFaultInjection")
    def enable_fault_injection(self) -> pulumi.Output[_builtins.bool]: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorage")
    def ephemeral_storage(
        self,
    ) -> pulumi.Output[Optional[outputs.TaskDefinitionEphemeralStorage]]: ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="ipcMode")
    def ipc_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="networkMode")
    def network_mode(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="pidMode")
    def pid_mode(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(
        self,
    ) -> pulumi.Output[
        Optional[Sequence[outputs.TaskDefinitionPlacementConstraint]]
    ]: ...
    @_builtins.property
    @pulumi.getter(name="proxyConfiguration")
    def proxy_configuration(
        self,
    ) -> pulumi.Output[Optional[outputs.TaskDefinitionProxyConfiguration]]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> pulumi.Output[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter(name="requiresCompatibilities")
    def requires_compatibilities(
        self,
    ) -> pulumi.Output[Optional[Sequence[_builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> pulumi.Output[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="runtimePlatform")
    def runtime_platform(
        self,
    ) -> pulumi.Output[Optional[outputs.TaskDefinitionRuntimePlatform]]: ...
    @_builtins.property
    @pulumi.getter(name="skipDestroy")
    def skip_destroy(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, _builtins.str]]]: ...
    @_builtins.property
    @pulumi.getter(name="tagsAll")
    def tags_all(self) -> pulumi.Output[Mapping[str, _builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="taskRoleArn")
    def task_role_arn(self) -> pulumi.Output[Optional[_builtins.str]]: ...
    @_builtins.property
    @pulumi.getter(name="trackLatest")
    def track_latest(self) -> pulumi.Output[Optional[_builtins.bool]]: ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> pulumi.Output[Optional[Sequence[outputs.TaskDefinitionVolume]]]: ...
