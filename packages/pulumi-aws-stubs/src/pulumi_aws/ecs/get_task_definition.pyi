import builtins as _builtins
import sys
import pulumi
from typing import Optional, Sequence, Union
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "GetTaskDefinitionResult",
    "AwaitableGetTaskDefinitionResult",
    "get_task_definition",
    "get_task_definition_output",
]

@pulumi.output_type
class GetTaskDefinitionResult:
    def __init__(
        __self__,
        arn=...,
        arn_without_revision=...,
        container_definitions=...,
        cpu=...,
        enable_fault_injection=...,
        ephemeral_storages=...,
        execution_role_arn=...,
        family=...,
        id=...,
        ipc_mode=...,
        memory=...,
        network_mode=...,
        pid_mode=...,
        placement_constraints=...,
        proxy_configurations=...,
        region=...,
        requires_compatibilities=...,
        revision=...,
        runtime_platforms=...,
        status=...,
        task_definition=...,
        task_role_arn=...,
        volumes=...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="arnWithoutRevision")
    def arn_without_revision(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="containerDefinitions")
    def container_definitions(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def cpu(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="enableFaultInjection")
    def enable_fault_injection(self) -> _builtins.bool: ...
    @_builtins.property
    @pulumi.getter(name="ephemeralStorages")
    def ephemeral_storages(
        self,
    ) -> Sequence[outputs.GetTaskDefinitionEphemeralStorageResult]: ...
    @_builtins.property
    @pulumi.getter(name="executionRoleArn")
    def execution_role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def family(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="ipcMode")
    def ipc_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def memory(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="networkMode")
    def network_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="pidMode")
    def pid_mode(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="placementConstraints")
    def placement_constraints(
        self,
    ) -> Sequence[outputs.GetTaskDefinitionPlacementConstraintResult]: ...
    @_builtins.property
    @pulumi.getter(name="proxyConfigurations")
    def proxy_configurations(
        self,
    ) -> Sequence[outputs.GetTaskDefinitionProxyConfigurationResult]: ...
    @_builtins.property
    @pulumi.getter
    def region(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="requiresCompatibilities")
    def requires_compatibilities(self) -> Sequence[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="runtimePlatforms")
    def runtime_platforms(
        self,
    ) -> Sequence[outputs.GetTaskDefinitionRuntimePlatformResult]: ...
    @_builtins.property
    @pulumi.getter
    def status(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="taskDefinition")
    def task_definition(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="taskRoleArn")
    def task_role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def volumes(self) -> Sequence[outputs.GetTaskDefinitionVolumeResult]: ...

class AwaitableGetTaskDefinitionResult(GetTaskDefinitionResult):
    def __await__(self): ...

def get_task_definition(
    region: Optional[_builtins.str] = ...,
    task_definition: Optional[_builtins.str] = ...,
    opts: Optional[pulumi.InvokeOptions] = ...,
) -> AwaitableGetTaskDefinitionResult: ...
def get_task_definition_output(
    region: Optional[pulumi.Input[Optional[_builtins.str]]] = ...,
    task_definition: Optional[pulumi.Input[_builtins.str]] = ...,
    opts: Optional[Union[pulumi.InvokeOptions, pulumi.InvokeOutputOptions]] = ...,
) -> pulumi.Output[GetTaskDefinitionResult]: ...
