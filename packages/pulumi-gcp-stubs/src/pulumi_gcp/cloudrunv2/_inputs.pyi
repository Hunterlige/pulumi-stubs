import builtins as _builtins
import sys
import pulumi
from typing import Mapping, NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "JobBinaryAuthorizationArgs",
    "JobBinaryAuthorizationArgsDict",
    "JobConditionArgs",
    "JobConditionArgsDict",
    "JobIamBindingConditionArgs",
    "JobIamBindingConditionArgsDict",
    "JobIamMemberConditionArgs",
    "JobIamMemberConditionArgsDict",
    "JobLatestCreatedExecutionArgs",
    "JobLatestCreatedExecutionArgsDict",
    "JobTemplateArgs",
    "JobTemplateArgsDict",
    "JobTemplateTemplateArgs",
    "JobTemplateTemplateArgsDict",
    "JobTemplateTemplateContainerArgs",
    "JobTemplateTemplateContainerArgsDict",
    "JobTemplateTemplateContainerEnvArgs",
    "JobTemplateTemplateContainerEnvArgsDict",
    "JobTemplateTemplateContainerEnvValueSourceArgs",
    "JobTemplateTemplateContainerEnvValueSourceArgsDict",
    ...,
    ...,
    "JobTemplateTemplateContainerPortArgs",
    "JobTemplateTemplateContainerPortArgsDict",
    "JobTemplateTemplateContainerResourcesArgs",
    "JobTemplateTemplateContainerResourcesArgsDict",
    "JobTemplateTemplateContainerStartupProbeArgs",
    "JobTemplateTemplateContainerStartupProbeArgsDict",
    "JobTemplateTemplateContainerStartupProbeGrpcArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "JobTemplateTemplateContainerVolumeMountArgs",
    "JobTemplateTemplateContainerVolumeMountArgsDict",
    "JobTemplateTemplateNodeSelectorArgs",
    "JobTemplateTemplateNodeSelectorArgsDict",
    "JobTemplateTemplateVolumeArgs",
    "JobTemplateTemplateVolumeArgsDict",
    "JobTemplateTemplateVolumeCloudSqlInstanceArgs",
    "JobTemplateTemplateVolumeCloudSqlInstanceArgsDict",
    "JobTemplateTemplateVolumeEmptyDirArgs",
    "JobTemplateTemplateVolumeEmptyDirArgsDict",
    "JobTemplateTemplateVolumeGcsArgs",
    "JobTemplateTemplateVolumeGcsArgsDict",
    "JobTemplateTemplateVolumeNfsArgs",
    "JobTemplateTemplateVolumeNfsArgsDict",
    "JobTemplateTemplateVolumeSecretArgs",
    "JobTemplateTemplateVolumeSecretArgsDict",
    "JobTemplateTemplateVolumeSecretItemArgs",
    "JobTemplateTemplateVolumeSecretItemArgsDict",
    "JobTemplateTemplateVpcAccessArgs",
    "JobTemplateTemplateVpcAccessArgsDict",
    "JobTemplateTemplateVpcAccessNetworkInterfaceArgs",
    ...,
    "JobTerminalConditionArgs",
    "JobTerminalConditionArgsDict",
    "ServiceBinaryAuthorizationArgs",
    "ServiceBinaryAuthorizationArgsDict",
    "ServiceBuildConfigArgs",
    "ServiceBuildConfigArgsDict",
    "ServiceConditionArgs",
    "ServiceConditionArgsDict",
    "ServiceIamBindingConditionArgs",
    "ServiceIamBindingConditionArgsDict",
    "ServiceIamMemberConditionArgs",
    "ServiceIamMemberConditionArgsDict",
    "ServiceMultiRegionSettingsArgs",
    "ServiceMultiRegionSettingsArgsDict",
    "ServiceScalingArgs",
    "ServiceScalingArgsDict",
    "ServiceTemplateArgs",
    "ServiceTemplateArgsDict",
    "ServiceTemplateContainerArgs",
    "ServiceTemplateContainerArgsDict",
    "ServiceTemplateContainerBuildInfoArgs",
    "ServiceTemplateContainerBuildInfoArgsDict",
    "ServiceTemplateContainerEnvArgs",
    "ServiceTemplateContainerEnvArgsDict",
    "ServiceTemplateContainerEnvValueSourceArgs",
    "ServiceTemplateContainerEnvValueSourceArgsDict",
    ...,
    ...,
    "ServiceTemplateContainerLivenessProbeArgs",
    "ServiceTemplateContainerLivenessProbeArgsDict",
    "ServiceTemplateContainerLivenessProbeGrpcArgs",
    "ServiceTemplateContainerLivenessProbeGrpcArgsDict",
    "ServiceTemplateContainerLivenessProbeHttpGetArgs",
    ...,
    ...,
    ...,
    "ServiceTemplateContainerLivenessProbeTcpSocketArgs",
    ...,
    "ServiceTemplateContainerPortsArgs",
    "ServiceTemplateContainerPortsArgsDict",
    "ServiceTemplateContainerReadinessProbeArgs",
    "ServiceTemplateContainerReadinessProbeArgsDict",
    "ServiceTemplateContainerReadinessProbeGrpcArgs",
    "ServiceTemplateContainerReadinessProbeGrpcArgsDict",
    "ServiceTemplateContainerReadinessProbeHttpGetArgs",
    ...,
    "ServiceTemplateContainerResourcesArgs",
    "ServiceTemplateContainerResourcesArgsDict",
    "ServiceTemplateContainerSourceCodeArgs",
    "ServiceTemplateContainerSourceCodeArgsDict",
    ...,
    ...,
    "ServiceTemplateContainerStartupProbeArgs",
    "ServiceTemplateContainerStartupProbeArgsDict",
    "ServiceTemplateContainerStartupProbeGrpcArgs",
    "ServiceTemplateContainerStartupProbeGrpcArgsDict",
    "ServiceTemplateContainerStartupProbeHttpGetArgs",
    ...,
    ...,
    ...,
    "ServiceTemplateContainerStartupProbeTcpSocketArgs",
    ...,
    "ServiceTemplateContainerVolumeMountArgs",
    "ServiceTemplateContainerVolumeMountArgsDict",
    "ServiceTemplateNodeSelectorArgs",
    "ServiceTemplateNodeSelectorArgsDict",
    "ServiceTemplateScalingArgs",
    "ServiceTemplateScalingArgsDict",
    "ServiceTemplateServiceMeshArgs",
    "ServiceTemplateServiceMeshArgsDict",
    "ServiceTemplateVolumeArgs",
    "ServiceTemplateVolumeArgsDict",
    "ServiceTemplateVolumeCloudSqlInstanceArgs",
    "ServiceTemplateVolumeCloudSqlInstanceArgsDict",
    "ServiceTemplateVolumeEmptyDirArgs",
    "ServiceTemplateVolumeEmptyDirArgsDict",
    "ServiceTemplateVolumeGcsArgs",
    "ServiceTemplateVolumeGcsArgsDict",
    "ServiceTemplateVolumeNfsArgs",
    "ServiceTemplateVolumeNfsArgsDict",
    "ServiceTemplateVolumeSecretArgs",
    "ServiceTemplateVolumeSecretArgsDict",
    "ServiceTemplateVolumeSecretItemArgs",
    "ServiceTemplateVolumeSecretItemArgsDict",
    "ServiceTemplateVpcAccessArgs",
    "ServiceTemplateVpcAccessArgsDict",
    "ServiceTemplateVpcAccessNetworkInterfaceArgs",
    "ServiceTemplateVpcAccessNetworkInterfaceArgsDict",
    "ServiceTerminalConditionArgs",
    "ServiceTerminalConditionArgsDict",
    "ServiceTrafficArgs",
    "ServiceTrafficArgsDict",
    "ServiceTrafficStatusArgs",
    "ServiceTrafficStatusArgsDict",
    "WorkerPoolBinaryAuthorizationArgs",
    "WorkerPoolBinaryAuthorizationArgsDict",
    "WorkerPoolConditionArgs",
    "WorkerPoolConditionArgsDict",
    "WorkerPoolIamBindingConditionArgs",
    "WorkerPoolIamBindingConditionArgsDict",
    "WorkerPoolIamMemberConditionArgs",
    "WorkerPoolIamMemberConditionArgsDict",
    "WorkerPoolInstanceSplitArgs",
    "WorkerPoolInstanceSplitArgsDict",
    "WorkerPoolInstanceSplitStatusArgs",
    "WorkerPoolInstanceSplitStatusArgsDict",
    "WorkerPoolScalingArgs",
    "WorkerPoolScalingArgsDict",
    "WorkerPoolTemplateArgs",
    "WorkerPoolTemplateArgsDict",
    "WorkerPoolTemplateContainerArgs",
    "WorkerPoolTemplateContainerArgsDict",
    "WorkerPoolTemplateContainerEnvArgs",
    "WorkerPoolTemplateContainerEnvArgsDict",
    "WorkerPoolTemplateContainerEnvValueSourceArgs",
    "WorkerPoolTemplateContainerEnvValueSourceArgsDict",
    ...,
    ...,
    "WorkerPoolTemplateContainerLivenessProbeArgs",
    "WorkerPoolTemplateContainerLivenessProbeArgsDict",
    "WorkerPoolTemplateContainerLivenessProbeGrpcArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    ...,
    "WorkerPoolTemplateContainerResourcesArgs",
    "WorkerPoolTemplateContainerResourcesArgsDict",
    "WorkerPoolTemplateContainerStartupProbeArgs",
    "WorkerPoolTemplateContainerStartupProbeArgsDict",
    "WorkerPoolTemplateContainerStartupProbeGrpcArgs",
    ...,
    "WorkerPoolTemplateContainerStartupProbeHttpGetArgs",
    ...,
    ...,
    ...,
    ...,
    ...,
    "WorkerPoolTemplateContainerVolumeMountArgs",
    "WorkerPoolTemplateContainerVolumeMountArgsDict",
    "WorkerPoolTemplateNodeSelectorArgs",
    "WorkerPoolTemplateNodeSelectorArgsDict",
    "WorkerPoolTemplateVolumeArgs",
    "WorkerPoolTemplateVolumeArgsDict",
    "WorkerPoolTemplateVolumeCloudSqlInstanceArgs",
    "WorkerPoolTemplateVolumeCloudSqlInstanceArgsDict",
    "WorkerPoolTemplateVolumeEmptyDirArgs",
    "WorkerPoolTemplateVolumeEmptyDirArgsDict",
    "WorkerPoolTemplateVolumeGcsArgs",
    "WorkerPoolTemplateVolumeGcsArgsDict",
    "WorkerPoolTemplateVolumeNfsArgs",
    "WorkerPoolTemplateVolumeNfsArgsDict",
    "WorkerPoolTemplateVolumeSecretArgs",
    "WorkerPoolTemplateVolumeSecretArgsDict",
    "WorkerPoolTemplateVolumeSecretItemArgs",
    "WorkerPoolTemplateVolumeSecretItemArgsDict",
    "WorkerPoolTemplateVpcAccessArgs",
    "WorkerPoolTemplateVpcAccessArgsDict",
    "WorkerPoolTemplateVpcAccessNetworkInterfaceArgs",
    ...,
    "WorkerPoolTerminalConditionArgs",
    "WorkerPoolTerminalConditionArgsDict",
]

class JobBinaryAuthorizationArgsDict(TypedDict):
    breakglass_justification: NotRequired[pulumi.Input[_builtins.str]]
    policy: NotRequired[pulumi.Input[_builtins.str]]
    use_default: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class JobBinaryAuthorizationArgs:
    def __init__(
        __self__,
        *,
        breakglass_justification: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        use_default: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="breakglassJustification")
    def breakglass_justification(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @breakglass_justification.setter
    def breakglass_justification(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useDefault")
    def use_default(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_default.setter
    def use_default(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class JobConditionArgsDict(TypedDict):
    execution_reason: NotRequired[pulumi.Input[_builtins.str]]
    last_transition_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    revision_reason: NotRequired[pulumi.Input[_builtins.str]]
    severity: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobConditionArgs:
    def __init__(
        __self__,
        *,
        execution_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        last_transition_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        revision_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        severity: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_reason.setter
    def execution_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_transition_time.setter
    def last_transition_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_reason.setter
    def revision_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobLatestCreatedExecutionArgsDict(TypedDict):
    completion_time: NotRequired[pulumi.Input[_builtins.str]]
    create_time: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobLatestCreatedExecutionArgs:
    def __init__(
        __self__,
        *,
        completion_time: Optional[pulumi.Input[_builtins.str]] = ...,
        create_time: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="completionTime")
    def completion_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @completion_time.setter
    def completion_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="createTime")
    def create_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @create_time.setter
    def create_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobTemplateArgsDict(TypedDict):
    template: pulumi.Input[JobTemplateTemplateArgsDict]
    annotations: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    parallelism: NotRequired[pulumi.Input[_builtins.int]]
    task_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class JobTemplateArgs:
    def __init__(
        __self__,
        *,
        template: pulumi.Input[JobTemplateTemplateArgs],
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        parallelism: Optional[pulumi.Input[_builtins.int]] = ...,
        task_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def template(self) -> pulumi.Input[JobTemplateTemplateArgs]: ...
    @template.setter
    def template(self, value: pulumi.Input[JobTemplateTemplateArgs]): ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def parallelism(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @parallelism.setter
    def parallelism(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="taskCount")
    def task_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @task_count.setter
    def task_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class JobTemplateTemplateArgsDict(TypedDict):
    containers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateContainerArgsDict]]]
    ]
    encryption_key: NotRequired[pulumi.Input[_builtins.str]]
    execution_environment: NotRequired[pulumi.Input[_builtins.str]]
    gpu_zonal_redundancy_disabled: NotRequired[pulumi.Input[_builtins.bool]]
    max_retries: NotRequired[pulumi.Input[_builtins.int]]
    node_selector: NotRequired[pulumi.Input[JobTemplateTemplateNodeSelectorArgsDict]]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]
    volumes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateVolumeArgsDict]]]
    ]
    vpc_access: NotRequired[pulumi.Input[JobTemplateTemplateVpcAccessArgsDict]]

@pulumi.input_type
class JobTemplateTemplateArgs:
    def __init__(
        __self__,
        *,
        containers: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateContainerArgs]]]
        ] = ...,
        encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_environment: Optional[pulumi.Input[_builtins.str]] = ...,
        gpu_zonal_redundancy_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        max_retries: Optional[pulumi.Input[_builtins.int]] = ...,
        node_selector: Optional[
            pulumi.Input[JobTemplateTemplateNodeSelectorArgs]
        ] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        volumes: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateVolumeArgs]]]
        ] = ...,
        vpc_access: Optional[pulumi.Input[JobTemplateTemplateVpcAccessArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def containers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateContainerArgs]]]
    ]: ...
    @containers.setter
    def containers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateContainerArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_key.setter
    def encryption_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionEnvironment")
    def execution_environment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_environment.setter
    def execution_environment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpuZonalRedundancyDisabled")
    def gpu_zonal_redundancy_disabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @gpu_zonal_redundancy_disabled.setter
    def gpu_zonal_redundancy_disabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxRetries")
    def max_retries(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_retries.setter
    def max_retries(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="nodeSelector")
    def node_selector(
        self,
    ) -> Optional[pulumi.Input[JobTemplateTemplateNodeSelectorArgs]]: ...
    @node_selector.setter
    def node_selector(
        self, value: Optional[pulumi.Input[JobTemplateTemplateNodeSelectorArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateVolumeArgs]]]
    ]: ...
    @volumes.setter
    def volumes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateVolumeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcAccess")
    def vpc_access(
        self,
    ) -> Optional[pulumi.Input[JobTemplateTemplateVpcAccessArgs]]: ...
    @vpc_access.setter
    def vpc_access(
        self, value: Optional[pulumi.Input[JobTemplateTemplateVpcAccessArgs]]
    ): ...

class JobTemplateTemplateContainerArgsDict(TypedDict):
    image: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    depends_ons: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    envs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateContainerEnvArgsDict]]]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ports: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateContainerPortArgsDict]]]
    ]
    resources: NotRequired[pulumi.Input[JobTemplateTemplateContainerResourcesArgsDict]]
    startup_probe: NotRequired[
        pulumi.Input[JobTemplateTemplateContainerStartupProbeArgsDict]
    ]
    volume_mounts: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[JobTemplateTemplateContainerVolumeMountArgsDict]]
        ]
    ]
    working_dir: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobTemplateTemplateContainerArgs:
    def __init__(
        __self__,
        *,
        image: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        depends_ons: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        envs: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateContainerEnvArgs]]]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ports: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateContainerPortArgs]]]
        ] = ...,
        resources: Optional[
            pulumi.Input[JobTemplateTemplateContainerResourcesArgs]
        ] = ...,
        startup_probe: Optional[
            pulumi.Input[JobTemplateTemplateContainerStartupProbeArgs]
        ] = ...,
        volume_mounts: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[JobTemplateTemplateContainerVolumeMountArgs]]
            ]
        ] = ...,
        working_dir: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Input[_builtins.str]: ...
    @image.setter
    def image(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def commands(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @commands.setter
    def commands(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dependsOns")
    def depends_ons(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @depends_ons.setter
    def depends_ons(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def envs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateContainerEnvArgs]]]
    ]: ...
    @envs.setter
    def envs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateContainerEnvArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ports(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateContainerPortArgs]]]
    ]: ...
    @ports.setter
    def ports(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateContainerPortArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[JobTemplateTemplateContainerResourcesArgs]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[JobTemplateTemplateContainerResourcesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startupProbe")
    def startup_probe(
        self,
    ) -> Optional[pulumi.Input[JobTemplateTemplateContainerStartupProbeArgs]]: ...
    @startup_probe.setter
    def startup_probe(
        self,
        value: Optional[pulumi.Input[JobTemplateTemplateContainerStartupProbeArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[JobTemplateTemplateContainerVolumeMountArgs]]
        ]
    ]: ...
    @volume_mounts.setter
    def volume_mounts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[JobTemplateTemplateContainerVolumeMountArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @working_dir.setter
    def working_dir(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobTemplateTemplateContainerEnvArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]
    value_source: NotRequired[
        pulumi.Input[JobTemplateTemplateContainerEnvValueSourceArgsDict]
    ]

@pulumi.input_type
class JobTemplateTemplateContainerEnvArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
        value_source: Optional[
            pulumi.Input[JobTemplateTemplateContainerEnvValueSourceArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="valueSource")
    def value_source(
        self,
    ) -> Optional[pulumi.Input[JobTemplateTemplateContainerEnvValueSourceArgs]]: ...
    @value_source.setter
    def value_source(
        self,
        value: Optional[pulumi.Input[JobTemplateTemplateContainerEnvValueSourceArgs]],
    ): ...

class JobTemplateTemplateContainerEnvValueSourceArgsDict(TypedDict):
    secret_key_ref: NotRequired[
        pulumi.Input[JobTemplateTemplateContainerEnvValueSourceSecretKeyRefArgsDict]
    ]

@pulumi.input_type
class JobTemplateTemplateContainerEnvValueSourceArgs:
    def __init__(
        __self__,
        *,
        secret_key_ref: Optional[
            pulumi.Input[JobTemplateTemplateContainerEnvValueSourceSecretKeyRefArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretKeyRef")
    def secret_key_ref(
        self,
    ) -> Optional[
        pulumi.Input[JobTemplateTemplateContainerEnvValueSourceSecretKeyRefArgs]
    ]: ...
    @secret_key_ref.setter
    def secret_key_ref(
        self,
        value: Optional[
            pulumi.Input[JobTemplateTemplateContainerEnvValueSourceSecretKeyRefArgs]
        ],
    ): ...

class JobTemplateTemplateContainerEnvValueSourceSecretKeyRefArgsDict(TypedDict):
    secret: pulumi.Input[_builtins.str]
    version: pulumi.Input[_builtins.str]

@pulumi.input_type
class JobTemplateTemplateContainerEnvValueSourceSecretKeyRefArgs:
    def __init__(
        __self__,
        *,
        secret: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Input[_builtins.str]: ...
    @secret.setter
    def secret(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...

class JobTemplateTemplateContainerPortArgsDict(TypedDict):
    container_port: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobTemplateTemplateContainerPortArgs:
    def __init__(
        __self__,
        *,
        container_port: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @container_port.setter
    def container_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobTemplateTemplateContainerResourcesArgsDict(TypedDict):
    limits: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class JobTemplateTemplateContainerResourcesArgs:
    def __init__(
        __self__,
        *,
        limits: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limits(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @limits.setter
    def limits(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class JobTemplateTemplateContainerStartupProbeArgsDict(TypedDict):
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    grpc: NotRequired[
        pulumi.Input[JobTemplateTemplateContainerStartupProbeGrpcArgsDict]
    ]
    http_get: NotRequired[
        pulumi.Input[JobTemplateTemplateContainerStartupProbeHttpGetArgsDict]
    ]
    initial_delay_seconds: NotRequired[pulumi.Input[_builtins.int]]
    period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    tcp_socket: NotRequired[
        pulumi.Input[JobTemplateTemplateContainerStartupProbeTcpSocketArgsDict]
    ]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class JobTemplateTemplateContainerStartupProbeArgs:
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        grpc: Optional[
            pulumi.Input[JobTemplateTemplateContainerStartupProbeGrpcArgs]
        ] = ...,
        http_get: Optional[
            pulumi.Input[JobTemplateTemplateContainerStartupProbeHttpGetArgs]
        ] = ...,
        initial_delay_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tcp_socket: Optional[
            pulumi.Input[JobTemplateTemplateContainerStartupProbeTcpSocketArgs]
        ] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[pulumi.Input[JobTemplateTemplateContainerStartupProbeGrpcArgs]]: ...
    @grpc.setter
    def grpc(
        self,
        value: Optional[pulumi.Input[JobTemplateTemplateContainerStartupProbeGrpcArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[
        pulumi.Input[JobTemplateTemplateContainerStartupProbeHttpGetArgs]
    ]: ...
    @http_get.setter
    def http_get(
        self,
        value: Optional[
            pulumi.Input[JobTemplateTemplateContainerStartupProbeHttpGetArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period_seconds.setter
    def period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(
        self,
    ) -> Optional[
        pulumi.Input[JobTemplateTemplateContainerStartupProbeTcpSocketArgs]
    ]: ...
    @tcp_socket.setter
    def tcp_socket(
        self,
        value: Optional[
            pulumi.Input[JobTemplateTemplateContainerStartupProbeTcpSocketArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class JobTemplateTemplateContainerStartupProbeGrpcArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]
    service: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobTemplateTemplateContainerStartupProbeGrpcArgs:
    def __init__(
        __self__,
        *,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobTemplateTemplateContainerStartupProbeHttpGetArgsDict(TypedDict):
    http_headers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    JobTemplateTemplateContainerStartupProbeHttpGetHttpHeaderArgsDict
                ]
            ]
        ]
    ]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class JobTemplateTemplateContainerStartupProbeHttpGetArgs:
    def __init__(
        __self__,
        *,
        http_headers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        JobTemplateTemplateContainerStartupProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    JobTemplateTemplateContainerStartupProbeHttpGetHttpHeaderArgs
                ]
            ]
        ]
    ]: ...
    @http_headers.setter
    def http_headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        JobTemplateTemplateContainerStartupProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class JobTemplateTemplateContainerStartupProbeHttpGetHttpHeaderArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobTemplateTemplateContainerStartupProbeHttpGetHttpHeaderArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobTemplateTemplateContainerStartupProbeTcpSocketArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class JobTemplateTemplateContainerStartupProbeTcpSocketArgs:
    def __init__(
        __self__, *, port: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class JobTemplateTemplateContainerVolumeMountArgsDict(TypedDict):
    mount_path: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    sub_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobTemplateTemplateContainerVolumeMountArgs:
    def __init__(
        __self__,
        *,
        mount_path: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        sub_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> pulumi.Input[_builtins.str]: ...
    @mount_path.setter
    def mount_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sub_path.setter
    def sub_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobTemplateTemplateNodeSelectorArgsDict(TypedDict):
    accelerator: pulumi.Input[_builtins.str]

@pulumi.input_type
class JobTemplateTemplateNodeSelectorArgs:
    def __init__(__self__, *, accelerator: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accelerator(self) -> pulumi.Input[_builtins.str]: ...
    @accelerator.setter
    def accelerator(self, value: pulumi.Input[_builtins.str]): ...

class JobTemplateTemplateVolumeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    cloud_sql_instance: NotRequired[
        pulumi.Input[JobTemplateTemplateVolumeCloudSqlInstanceArgsDict]
    ]
    empty_dir: NotRequired[pulumi.Input[JobTemplateTemplateVolumeEmptyDirArgsDict]]
    gcs: NotRequired[pulumi.Input[JobTemplateTemplateVolumeGcsArgsDict]]
    nfs: NotRequired[pulumi.Input[JobTemplateTemplateVolumeNfsArgsDict]]
    secret: NotRequired[pulumi.Input[JobTemplateTemplateVolumeSecretArgsDict]]

@pulumi.input_type
class JobTemplateTemplateVolumeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        cloud_sql_instance: Optional[
            pulumi.Input[JobTemplateTemplateVolumeCloudSqlInstanceArgs]
        ] = ...,
        empty_dir: Optional[pulumi.Input[JobTemplateTemplateVolumeEmptyDirArgs]] = ...,
        gcs: Optional[pulumi.Input[JobTemplateTemplateVolumeGcsArgs]] = ...,
        nfs: Optional[pulumi.Input[JobTemplateTemplateVolumeNfsArgs]] = ...,
        secret: Optional[pulumi.Input[JobTemplateTemplateVolumeSecretArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cloudSqlInstance")
    def cloud_sql_instance(
        self,
    ) -> Optional[pulumi.Input[JobTemplateTemplateVolumeCloudSqlInstanceArgs]]: ...
    @cloud_sql_instance.setter
    def cloud_sql_instance(
        self,
        value: Optional[pulumi.Input[JobTemplateTemplateVolumeCloudSqlInstanceArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="emptyDir")
    def empty_dir(
        self,
    ) -> Optional[pulumi.Input[JobTemplateTemplateVolumeEmptyDirArgs]]: ...
    @empty_dir.setter
    def empty_dir(
        self, value: Optional[pulumi.Input[JobTemplateTemplateVolumeEmptyDirArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def gcs(self) -> Optional[pulumi.Input[JobTemplateTemplateVolumeGcsArgs]]: ...
    @gcs.setter
    def gcs(self, value: Optional[pulumi.Input[JobTemplateTemplateVolumeGcsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Optional[pulumi.Input[JobTemplateTemplateVolumeNfsArgs]]: ...
    @nfs.setter
    def nfs(self, value: Optional[pulumi.Input[JobTemplateTemplateVolumeNfsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[JobTemplateTemplateVolumeSecretArgs]]: ...
    @secret.setter
    def secret(
        self, value: Optional[pulumi.Input[JobTemplateTemplateVolumeSecretArgs]]
    ): ...

class JobTemplateTemplateVolumeCloudSqlInstanceArgsDict(TypedDict):
    instances: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class JobTemplateTemplateVolumeCloudSqlInstanceArgs:
    def __init__(
        __self__,
        *,
        instances: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instances.setter
    def instances(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class JobTemplateTemplateVolumeEmptyDirArgsDict(TypedDict):
    medium: NotRequired[pulumi.Input[_builtins.str]]
    size_limit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobTemplateTemplateVolumeEmptyDirArgs:
    def __init__(
        __self__,
        *,
        medium: Optional[pulumi.Input[_builtins.str]] = ...,
        size_limit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @medium.setter
    def medium(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeLimit")
    def size_limit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @size_limit.setter
    def size_limit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class JobTemplateTemplateVolumeGcsArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    mount_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class JobTemplateTemplateVolumeGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        mount_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @mount_options.setter
    def mount_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class JobTemplateTemplateVolumeNfsArgsDict(TypedDict):
    server: pulumi.Input[_builtins.str]
    path: NotRequired[pulumi.Input[_builtins.str]]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class JobTemplateTemplateVolumeNfsArgs:
    def __init__(
        __self__,
        *,
        server: pulumi.Input[_builtins.str],
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> pulumi.Input[_builtins.str]: ...
    @server.setter
    def server(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class JobTemplateTemplateVolumeSecretArgsDict(TypedDict):
    secret: pulumi.Input[_builtins.str]
    default_mode: NotRequired[pulumi.Input[_builtins.int]]
    items: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[JobTemplateTemplateVolumeSecretItemArgsDict]]
        ]
    ]

@pulumi.input_type
class JobTemplateTemplateVolumeSecretArgs:
    def __init__(
        __self__,
        *,
        secret: pulumi.Input[_builtins.str],
        default_mode: Optional[pulumi.Input[_builtins.int]] = ...,
        items: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[JobTemplateTemplateVolumeSecretItemArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Input[_builtins.str]: ...
    @secret.setter
    def secret(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_mode.setter
    def default_mode(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[JobTemplateTemplateVolumeSecretItemArgs]]]
    ]: ...
    @items.setter
    def items(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[JobTemplateTemplateVolumeSecretItemArgs]]
            ]
        ],
    ): ...

class JobTemplateTemplateVolumeSecretItemArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    version: pulumi.Input[_builtins.str]
    mode: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class JobTemplateTemplateVolumeSecretItemArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        version: pulumi.Input[_builtins.str],
        mode: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> pulumi.Input[_builtins.str]: ...
    @version.setter
    def version(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class JobTemplateTemplateVpcAccessArgsDict(TypedDict):
    connector: NotRequired[pulumi.Input[_builtins.str]]
    egress: NotRequired[pulumi.Input[_builtins.str]]
    network_interfaces: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[JobTemplateTemplateVpcAccessNetworkInterfaceArgsDict]]
        ]
    ]

@pulumi.input_type
class JobTemplateTemplateVpcAccessArgs:
    def __init__(
        __self__,
        *,
        connector: Optional[pulumi.Input[_builtins.str]] = ...,
        egress: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interfaces: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[JobTemplateTemplateVpcAccessNetworkInterfaceArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connector(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connector.setter
    def connector(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @egress.setter
    def egress(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[JobTemplateTemplateVpcAccessNetworkInterfaceArgs]]
        ]
    ]: ...
    @network_interfaces.setter
    def network_interfaces(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[JobTemplateTemplateVpcAccessNetworkInterfaceArgs]]
            ]
        ],
    ): ...

class JobTemplateTemplateVpcAccessNetworkInterfaceArgsDict(TypedDict):
    network: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class JobTemplateTemplateVpcAccessNetworkInterfaceArgs:
    def __init__(
        __self__,
        *,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class JobTerminalConditionArgsDict(TypedDict):
    execution_reason: NotRequired[pulumi.Input[_builtins.str]]
    last_transition_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    revision_reason: NotRequired[pulumi.Input[_builtins.str]]
    severity: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class JobTerminalConditionArgs:
    def __init__(
        __self__,
        *,
        execution_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        last_transition_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        revision_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        severity: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_reason.setter
    def execution_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_transition_time.setter
    def last_transition_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_reason.setter
    def revision_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceBinaryAuthorizationArgsDict(TypedDict):
    breakglass_justification: NotRequired[pulumi.Input[_builtins.str]]
    policy: NotRequired[pulumi.Input[_builtins.str]]
    use_default: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ServiceBinaryAuthorizationArgs:
    def __init__(
        __self__,
        *,
        breakglass_justification: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        use_default: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="breakglassJustification")
    def breakglass_justification(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @breakglass_justification.setter
    def breakglass_justification(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useDefault")
    def use_default(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_default.setter
    def use_default(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ServiceBuildConfigArgsDict(TypedDict):
    base_image: NotRequired[pulumi.Input[_builtins.str]]
    enable_automatic_updates: NotRequired[pulumi.Input[_builtins.bool]]
    environment_variables: NotRequired[
        pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
    ]
    function_target: NotRequired[pulumi.Input[_builtins.str]]
    image_uri: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    source_location: NotRequired[pulumi.Input[_builtins.str]]
    worker_pool: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceBuildConfigArgs:
    def __init__(
        __self__,
        *,
        base_image: Optional[pulumi.Input[_builtins.str]] = ...,
        enable_automatic_updates: Optional[pulumi.Input[_builtins.bool]] = ...,
        environment_variables: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        function_target: Optional[pulumi.Input[_builtins.str]] = ...,
        image_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        source_location: Optional[pulumi.Input[_builtins.str]] = ...,
        worker_pool: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="baseImage")
    def base_image(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @base_image.setter
    def base_image(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="enableAutomaticUpdates")
    def enable_automatic_updates(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @enable_automatic_updates.setter
    def enable_automatic_updates(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @environment_variables.setter
    def environment_variables(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="functionTarget")
    def function_target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @function_target.setter
    def function_target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="imageUri")
    def image_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @image_uri.setter
    def image_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_location.setter
    def source_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="workerPool")
    def worker_pool(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @worker_pool.setter
    def worker_pool(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceConditionArgsDict(TypedDict):
    execution_reason: NotRequired[pulumi.Input[_builtins.str]]
    last_transition_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    revision_reason: NotRequired[pulumi.Input[_builtins.str]]
    severity: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceConditionArgs:
    def __init__(
        __self__,
        *,
        execution_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        last_transition_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        revision_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        severity: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_reason.setter
    def execution_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_transition_time.setter
    def last_transition_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_reason.setter
    def revision_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceMultiRegionSettingsArgsDict(TypedDict):
    multi_region_id: NotRequired[pulumi.Input[_builtins.str]]
    regions: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServiceMultiRegionSettingsArgs:
    def __init__(
        __self__,
        *,
        multi_region_id: Optional[pulumi.Input[_builtins.str]] = ...,
        regions: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="multiRegionId")
    def multi_region_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @multi_region_id.setter
    def multi_region_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def regions(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @regions.setter
    def regions(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServiceScalingArgsDict(TypedDict):
    manual_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    max_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    min_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    scaling_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceScalingArgs:
    def __init__(
        __self__,
        *,
        manual_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        max_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        scaling_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="manualInstanceCount")
    def manual_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @manual_instance_count.setter
    def manual_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_instance_count.setter
    def max_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_instance_count.setter
    def min_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingMode")
    def scaling_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scaling_mode.setter
    def scaling_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateArgsDict(TypedDict):
    annotations: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    containers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateContainerArgsDict]]]
    ]
    encryption_key: NotRequired[pulumi.Input[_builtins.str]]
    execution_environment: NotRequired[pulumi.Input[_builtins.str]]
    gpu_zonal_redundancy_disabled: NotRequired[pulumi.Input[_builtins.bool]]
    health_check_disabled: NotRequired[pulumi.Input[_builtins.bool]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    max_instance_request_concurrency: NotRequired[pulumi.Input[_builtins.int]]
    node_selector: NotRequired[pulumi.Input[ServiceTemplateNodeSelectorArgsDict]]
    revision: NotRequired[pulumi.Input[_builtins.str]]
    scaling: NotRequired[pulumi.Input[ServiceTemplateScalingArgsDict]]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    service_mesh: NotRequired[pulumi.Input[ServiceTemplateServiceMeshArgsDict]]
    session_affinity: NotRequired[pulumi.Input[_builtins.bool]]
    timeout: NotRequired[pulumi.Input[_builtins.str]]
    volumes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateVolumeArgsDict]]]
    ]
    vpc_access: NotRequired[pulumi.Input[ServiceTemplateVpcAccessArgsDict]]

@pulumi.input_type
class ServiceTemplateArgs:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        containers: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateContainerArgs]]]
        ] = ...,
        encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        execution_environment: Optional[pulumi.Input[_builtins.str]] = ...,
        gpu_zonal_redundancy_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        health_check_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        max_instance_request_concurrency: Optional[pulumi.Input[_builtins.int]] = ...,
        node_selector: Optional[pulumi.Input[ServiceTemplateNodeSelectorArgs]] = ...,
        revision: Optional[pulumi.Input[_builtins.str]] = ...,
        scaling: Optional[pulumi.Input[ServiceTemplateScalingArgs]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        service_mesh: Optional[pulumi.Input[ServiceTemplateServiceMeshArgs]] = ...,
        session_affinity: Optional[pulumi.Input[_builtins.bool]] = ...,
        timeout: Optional[pulumi.Input[_builtins.str]] = ...,
        volumes: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateVolumeArgs]]]
        ] = ...,
        vpc_access: Optional[pulumi.Input[ServiceTemplateVpcAccessArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def containers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateContainerArgs]]]
    ]: ...
    @containers.setter
    def containers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateContainerArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_key.setter
    def encryption_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="executionEnvironment")
    def execution_environment(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_environment.setter
    def execution_environment(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="gpuZonalRedundancyDisabled")
    def gpu_zonal_redundancy_disabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @gpu_zonal_redundancy_disabled.setter
    def gpu_zonal_redundancy_disabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="healthCheckDisabled")
    def health_check_disabled(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @health_check_disabled.setter
    def health_check_disabled(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxInstanceRequestConcurrency")
    def max_instance_request_concurrency(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_instance_request_concurrency.setter
    def max_instance_request_concurrency(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeSelector")
    def node_selector(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateNodeSelectorArgs]]: ...
    @node_selector.setter
    def node_selector(
        self, value: Optional[pulumi.Input[ServiceTemplateNodeSelectorArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def scaling(self) -> Optional[pulumi.Input[ServiceTemplateScalingArgs]]: ...
    @scaling.setter
    def scaling(self, value: Optional[pulumi.Input[ServiceTemplateScalingArgs]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceMesh")
    def service_mesh(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateServiceMeshArgs]]: ...
    @service_mesh.setter
    def service_mesh(
        self, value: Optional[pulumi.Input[ServiceTemplateServiceMeshArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sessionAffinity")
    def session_affinity(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @session_affinity.setter
    def session_affinity(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def timeout(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @timeout.setter
    def timeout(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[ServiceTemplateVolumeArgs]]]]: ...
    @volumes.setter
    def volumes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateVolumeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcAccess")
    def vpc_access(self) -> Optional[pulumi.Input[ServiceTemplateVpcAccessArgs]]: ...
    @vpc_access.setter
    def vpc_access(
        self, value: Optional[pulumi.Input[ServiceTemplateVpcAccessArgs]]
    ): ...

class ServiceTemplateContainerArgsDict(TypedDict):
    image: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    base_image_uri: NotRequired[pulumi.Input[_builtins.str]]
    build_infos: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateContainerBuildInfoArgsDict]]]
    ]
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    depends_ons: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    envs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateContainerEnvArgsDict]]]
    ]
    liveness_probe: NotRequired[
        pulumi.Input[ServiceTemplateContainerLivenessProbeArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    ports: NotRequired[pulumi.Input[ServiceTemplateContainerPortsArgsDict]]
    readiness_probe: NotRequired[
        pulumi.Input[ServiceTemplateContainerReadinessProbeArgsDict]
    ]
    resources: NotRequired[pulumi.Input[ServiceTemplateContainerResourcesArgsDict]]
    source_code: NotRequired[pulumi.Input[ServiceTemplateContainerSourceCodeArgsDict]]
    startup_probe: NotRequired[
        pulumi.Input[ServiceTemplateContainerStartupProbeArgsDict]
    ]
    volume_mounts: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ServiceTemplateContainerVolumeMountArgsDict]]
        ]
    ]
    working_dir: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateContainerArgs:
    def __init__(
        __self__,
        *,
        image: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        base_image_uri: Optional[pulumi.Input[_builtins.str]] = ...,
        build_infos: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateContainerBuildInfoArgs]]]
        ] = ...,
        commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        depends_ons: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        envs: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateContainerEnvArgs]]]
        ] = ...,
        liveness_probe: Optional[
            pulumi.Input[ServiceTemplateContainerLivenessProbeArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        ports: Optional[pulumi.Input[ServiceTemplateContainerPortsArgs]] = ...,
        readiness_probe: Optional[
            pulumi.Input[ServiceTemplateContainerReadinessProbeArgs]
        ] = ...,
        resources: Optional[pulumi.Input[ServiceTemplateContainerResourcesArgs]] = ...,
        source_code: Optional[
            pulumi.Input[ServiceTemplateContainerSourceCodeArgs]
        ] = ...,
        startup_probe: Optional[
            pulumi.Input[ServiceTemplateContainerStartupProbeArgs]
        ] = ...,
        volume_mounts: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceTemplateContainerVolumeMountArgs]]
            ]
        ] = ...,
        working_dir: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Input[_builtins.str]: ...
    @image.setter
    def image(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="baseImageUri")
    def base_image_uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @base_image_uri.setter
    def base_image_uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="buildInfos")
    def build_infos(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateContainerBuildInfoArgs]]]
    ]: ...
    @build_infos.setter
    def build_infos(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateContainerBuildInfoArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def commands(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @commands.setter
    def commands(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dependsOns")
    def depends_ons(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @depends_ons.setter
    def depends_ons(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def envs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateContainerEnvArgs]]]
    ]: ...
    @envs.setter
    def envs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateContainerEnvArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="livenessProbe")
    def liveness_probe(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateContainerLivenessProbeArgs]]: ...
    @liveness_probe.setter
    def liveness_probe(
        self, value: Optional[pulumi.Input[ServiceTemplateContainerLivenessProbeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def ports(self) -> Optional[pulumi.Input[ServiceTemplateContainerPortsArgs]]: ...
    @ports.setter
    def ports(
        self, value: Optional[pulumi.Input[ServiceTemplateContainerPortsArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="readinessProbe")
    def readiness_probe(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateContainerReadinessProbeArgs]]: ...
    @readiness_probe.setter
    def readiness_probe(
        self, value: Optional[pulumi.Input[ServiceTemplateContainerReadinessProbeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateContainerResourcesArgs]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[ServiceTemplateContainerResourcesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="sourceCode")
    def source_code(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateContainerSourceCodeArgs]]: ...
    @source_code.setter
    def source_code(
        self, value: Optional[pulumi.Input[ServiceTemplateContainerSourceCodeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startupProbe")
    def startup_probe(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateContainerStartupProbeArgs]]: ...
    @startup_probe.setter
    def startup_probe(
        self, value: Optional[pulumi.Input[ServiceTemplateContainerStartupProbeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateContainerVolumeMountArgs]]]
    ]: ...
    @volume_mounts.setter
    def volume_mounts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceTemplateContainerVolumeMountArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @working_dir.setter
    def working_dir(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateContainerBuildInfoArgsDict(TypedDict):
    function_target: NotRequired[pulumi.Input[_builtins.str]]
    source_location: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateContainerBuildInfoArgs:
    def __init__(
        __self__,
        *,
        function_target: Optional[pulumi.Input[_builtins.str]] = ...,
        source_location: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="functionTarget")
    def function_target(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @function_target.setter
    def function_target(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sourceLocation")
    def source_location(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @source_location.setter
    def source_location(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateContainerEnvArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]
    value_source: NotRequired[
        pulumi.Input[ServiceTemplateContainerEnvValueSourceArgsDict]
    ]

@pulumi.input_type
class ServiceTemplateContainerEnvArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
        value_source: Optional[
            pulumi.Input[ServiceTemplateContainerEnvValueSourceArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="valueSource")
    def value_source(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateContainerEnvValueSourceArgs]]: ...
    @value_source.setter
    def value_source(
        self, value: Optional[pulumi.Input[ServiceTemplateContainerEnvValueSourceArgs]]
    ): ...

class ServiceTemplateContainerEnvValueSourceArgsDict(TypedDict):
    secret_key_ref: NotRequired[
        pulumi.Input[ServiceTemplateContainerEnvValueSourceSecretKeyRefArgsDict]
    ]

@pulumi.input_type
class ServiceTemplateContainerEnvValueSourceArgs:
    def __init__(
        __self__,
        *,
        secret_key_ref: Optional[
            pulumi.Input[ServiceTemplateContainerEnvValueSourceSecretKeyRefArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretKeyRef")
    def secret_key_ref(
        self,
    ) -> Optional[
        pulumi.Input[ServiceTemplateContainerEnvValueSourceSecretKeyRefArgs]
    ]: ...
    @secret_key_ref.setter
    def secret_key_ref(
        self,
        value: Optional[
            pulumi.Input[ServiceTemplateContainerEnvValueSourceSecretKeyRefArgs]
        ],
    ): ...

class ServiceTemplateContainerEnvValueSourceSecretKeyRefArgsDict(TypedDict):
    secret: pulumi.Input[_builtins.str]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateContainerEnvValueSourceSecretKeyRefArgs:
    def __init__(
        __self__,
        *,
        secret: pulumi.Input[_builtins.str],
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Input[_builtins.str]: ...
    @secret.setter
    def secret(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateContainerLivenessProbeArgsDict(TypedDict):
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    grpc: NotRequired[pulumi.Input[ServiceTemplateContainerLivenessProbeGrpcArgsDict]]
    http_get: NotRequired[
        pulumi.Input[ServiceTemplateContainerLivenessProbeHttpGetArgsDict]
    ]
    initial_delay_seconds: NotRequired[pulumi.Input[_builtins.int]]
    period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    tcp_socket: NotRequired[
        pulumi.Input[ServiceTemplateContainerLivenessProbeTcpSocketArgsDict]
    ]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateContainerLivenessProbeArgs:
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        grpc: Optional[
            pulumi.Input[ServiceTemplateContainerLivenessProbeGrpcArgs]
        ] = ...,
        http_get: Optional[
            pulumi.Input[ServiceTemplateContainerLivenessProbeHttpGetArgs]
        ] = ...,
        initial_delay_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tcp_socket: Optional[
            pulumi.Input[ServiceTemplateContainerLivenessProbeTcpSocketArgs]
        ] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateContainerLivenessProbeGrpcArgs]]: ...
    @grpc.setter
    def grpc(
        self,
        value: Optional[pulumi.Input[ServiceTemplateContainerLivenessProbeGrpcArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateContainerLivenessProbeHttpGetArgs]]: ...
    @http_get.setter
    def http_get(
        self,
        value: Optional[pulumi.Input[ServiceTemplateContainerLivenessProbeHttpGetArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period_seconds.setter
    def period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateContainerLivenessProbeTcpSocketArgs]]: ...
    @tcp_socket.setter
    def tcp_socket(
        self,
        value: Optional[
            pulumi.Input[ServiceTemplateContainerLivenessProbeTcpSocketArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTemplateContainerLivenessProbeGrpcArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]
    service: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateContainerLivenessProbeGrpcArgs:
    def __init__(
        __self__,
        *,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateContainerLivenessProbeHttpGetArgsDict(TypedDict):
    http_headers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServiceTemplateContainerLivenessProbeHttpGetHttpHeaderArgsDict
                ]
            ]
        ]
    ]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateContainerLivenessProbeHttpGetArgs:
    def __init__(
        __self__,
        *,
        http_headers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceTemplateContainerLivenessProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServiceTemplateContainerLivenessProbeHttpGetHttpHeaderArgs]
            ]
        ]
    ]: ...
    @http_headers.setter
    def http_headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceTemplateContainerLivenessProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTemplateContainerLivenessProbeHttpGetHttpHeaderArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateContainerLivenessProbeHttpGetHttpHeaderArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateContainerLivenessProbeTcpSocketArgsDict(TypedDict):
    port: pulumi.Input[_builtins.int]

@pulumi.input_type
class ServiceTemplateContainerLivenessProbeTcpSocketArgs:
    def __init__(__self__, *, port: pulumi.Input[_builtins.int]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...

class ServiceTemplateContainerPortsArgsDict(TypedDict):
    container_port: NotRequired[pulumi.Input[_builtins.int]]
    name: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateContainerPortsArgs:
    def __init__(
        __self__,
        *,
        container_port: Optional[pulumi.Input[_builtins.int]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="containerPort")
    def container_port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @container_port.setter
    def container_port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateContainerReadinessProbeArgsDict(TypedDict):
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    grpc: NotRequired[pulumi.Input[ServiceTemplateContainerReadinessProbeGrpcArgsDict]]
    http_get: NotRequired[
        pulumi.Input[ServiceTemplateContainerReadinessProbeHttpGetArgsDict]
    ]
    period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    success_threshold: NotRequired[pulumi.Input[_builtins.int]]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateContainerReadinessProbeArgs:
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        grpc: Optional[
            pulumi.Input[ServiceTemplateContainerReadinessProbeGrpcArgs]
        ] = ...,
        http_get: Optional[
            pulumi.Input[ServiceTemplateContainerReadinessProbeHttpGetArgs]
        ] = ...,
        period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        success_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateContainerReadinessProbeGrpcArgs]]: ...
    @grpc.setter
    def grpc(
        self,
        value: Optional[pulumi.Input[ServiceTemplateContainerReadinessProbeGrpcArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateContainerReadinessProbeHttpGetArgs]]: ...
    @http_get.setter
    def http_get(
        self,
        value: Optional[
            pulumi.Input[ServiceTemplateContainerReadinessProbeHttpGetArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period_seconds.setter
    def period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="successThreshold")
    def success_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @success_threshold.setter
    def success_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTemplateContainerReadinessProbeGrpcArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]
    service: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateContainerReadinessProbeGrpcArgs:
    def __init__(
        __self__,
        *,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateContainerReadinessProbeHttpGetArgsDict(TypedDict):
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateContainerReadinessProbeHttpGetArgs:
    def __init__(
        __self__,
        *,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTemplateContainerResourcesArgsDict(TypedDict):
    cpu_idle: NotRequired[pulumi.Input[_builtins.bool]]
    limits: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    startup_cpu_boost: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ServiceTemplateContainerResourcesArgs:
    def __init__(
        __self__,
        *,
        cpu_idle: Optional[pulumi.Input[_builtins.bool]] = ...,
        limits: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        startup_cpu_boost: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cpuIdle")
    def cpu_idle(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @cpu_idle.setter
    def cpu_idle(self, value: Optional[pulumi.Input[_builtins.bool]]): ...
    @_builtins.property
    @pulumi.getter
    def limits(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @limits.setter
    def limits(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startupCpuBoost")
    def startup_cpu_boost(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @startup_cpu_boost.setter
    def startup_cpu_boost(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ServiceTemplateContainerSourceCodeArgsDict(TypedDict):
    cloud_storage_source: NotRequired[
        pulumi.Input[ServiceTemplateContainerSourceCodeCloudStorageSourceArgsDict]
    ]

@pulumi.input_type
class ServiceTemplateContainerSourceCodeArgs:
    def __init__(
        __self__,
        *,
        cloud_storage_source: Optional[
            pulumi.Input[ServiceTemplateContainerSourceCodeCloudStorageSourceArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="cloudStorageSource")
    def cloud_storage_source(
        self,
    ) -> Optional[
        pulumi.Input[ServiceTemplateContainerSourceCodeCloudStorageSourceArgs]
    ]: ...
    @cloud_storage_source.setter
    def cloud_storage_source(
        self,
        value: Optional[
            pulumi.Input[ServiceTemplateContainerSourceCodeCloudStorageSourceArgs]
        ],
    ): ...

class ServiceTemplateContainerSourceCodeCloudStorageSourceArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    object: pulumi.Input[_builtins.str]
    generation: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateContainerSourceCodeCloudStorageSourceArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        object: pulumi.Input[_builtins.str],
        generation: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def object(self) -> pulumi.Input[_builtins.str]: ...
    @object.setter
    def object(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def generation(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @generation.setter
    def generation(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateContainerStartupProbeArgsDict(TypedDict):
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    grpc: NotRequired[pulumi.Input[ServiceTemplateContainerStartupProbeGrpcArgsDict]]
    http_get: NotRequired[
        pulumi.Input[ServiceTemplateContainerStartupProbeHttpGetArgsDict]
    ]
    initial_delay_seconds: NotRequired[pulumi.Input[_builtins.int]]
    period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    tcp_socket: NotRequired[
        pulumi.Input[ServiceTemplateContainerStartupProbeTcpSocketArgsDict]
    ]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateContainerStartupProbeArgs:
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        grpc: Optional[
            pulumi.Input[ServiceTemplateContainerStartupProbeGrpcArgs]
        ] = ...,
        http_get: Optional[
            pulumi.Input[ServiceTemplateContainerStartupProbeHttpGetArgs]
        ] = ...,
        initial_delay_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tcp_socket: Optional[
            pulumi.Input[ServiceTemplateContainerStartupProbeTcpSocketArgs]
        ] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateContainerStartupProbeGrpcArgs]]: ...
    @grpc.setter
    def grpc(
        self,
        value: Optional[pulumi.Input[ServiceTemplateContainerStartupProbeGrpcArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateContainerStartupProbeHttpGetArgs]]: ...
    @http_get.setter
    def http_get(
        self,
        value: Optional[pulumi.Input[ServiceTemplateContainerStartupProbeHttpGetArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period_seconds.setter
    def period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateContainerStartupProbeTcpSocketArgs]]: ...
    @tcp_socket.setter
    def tcp_socket(
        self,
        value: Optional[
            pulumi.Input[ServiceTemplateContainerStartupProbeTcpSocketArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTemplateContainerStartupProbeGrpcArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]
    service: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateContainerStartupProbeGrpcArgs:
    def __init__(
        __self__,
        *,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateContainerStartupProbeHttpGetArgsDict(TypedDict):
    http_headers: NotRequired[
        pulumi.Input[
            Sequence[
                pulumi.Input[
                    ServiceTemplateContainerStartupProbeHttpGetHttpHeaderArgsDict
                ]
            ]
        ]
    ]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateContainerStartupProbeHttpGetArgs:
    def __init__(
        __self__,
        *,
        http_headers: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceTemplateContainerStartupProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[
                pulumi.Input[ServiceTemplateContainerStartupProbeHttpGetHttpHeaderArgs]
            ]
        ]
    ]: ...
    @http_headers.setter
    def http_headers(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[
                    pulumi.Input[
                        ServiceTemplateContainerStartupProbeHttpGetHttpHeaderArgs
                    ]
                ]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTemplateContainerStartupProbeHttpGetHttpHeaderArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateContainerStartupProbeHttpGetHttpHeaderArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateContainerStartupProbeTcpSocketArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateContainerStartupProbeTcpSocketArgs:
    def __init__(
        __self__, *, port: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTemplateContainerVolumeMountArgsDict(TypedDict):
    mount_path: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    sub_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateContainerVolumeMountArgs:
    def __init__(
        __self__,
        *,
        mount_path: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        sub_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> pulumi.Input[_builtins.str]: ...
    @mount_path.setter
    def mount_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sub_path.setter
    def sub_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateNodeSelectorArgsDict(TypedDict):
    accelerator: pulumi.Input[_builtins.str]

@pulumi.input_type
class ServiceTemplateNodeSelectorArgs:
    def __init__(__self__, *, accelerator: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accelerator(self) -> pulumi.Input[_builtins.str]: ...
    @accelerator.setter
    def accelerator(self, value: pulumi.Input[_builtins.str]): ...

class ServiceTemplateScalingArgsDict(TypedDict):
    max_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    min_instance_count: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class ServiceTemplateScalingArgs:
    def __init__(
        __self__,
        *,
        max_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_instance_count.setter
    def max_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_instance_count.setter
    def min_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ServiceTemplateServiceMeshArgsDict(TypedDict):
    mesh: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateServiceMeshArgs:
    def __init__(
        __self__, *, mesh: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def mesh(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @mesh.setter
    def mesh(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateVolumeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    cloud_sql_instance: NotRequired[
        pulumi.Input[ServiceTemplateVolumeCloudSqlInstanceArgsDict]
    ]
    empty_dir: NotRequired[pulumi.Input[ServiceTemplateVolumeEmptyDirArgsDict]]
    gcs: NotRequired[pulumi.Input[ServiceTemplateVolumeGcsArgsDict]]
    nfs: NotRequired[pulumi.Input[ServiceTemplateVolumeNfsArgsDict]]
    secret: NotRequired[pulumi.Input[ServiceTemplateVolumeSecretArgsDict]]

@pulumi.input_type
class ServiceTemplateVolumeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        cloud_sql_instance: Optional[
            pulumi.Input[ServiceTemplateVolumeCloudSqlInstanceArgs]
        ] = ...,
        empty_dir: Optional[pulumi.Input[ServiceTemplateVolumeEmptyDirArgs]] = ...,
        gcs: Optional[pulumi.Input[ServiceTemplateVolumeGcsArgs]] = ...,
        nfs: Optional[pulumi.Input[ServiceTemplateVolumeNfsArgs]] = ...,
        secret: Optional[pulumi.Input[ServiceTemplateVolumeSecretArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cloudSqlInstance")
    def cloud_sql_instance(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateVolumeCloudSqlInstanceArgs]]: ...
    @cloud_sql_instance.setter
    def cloud_sql_instance(
        self, value: Optional[pulumi.Input[ServiceTemplateVolumeCloudSqlInstanceArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="emptyDir")
    def empty_dir(
        self,
    ) -> Optional[pulumi.Input[ServiceTemplateVolumeEmptyDirArgs]]: ...
    @empty_dir.setter
    def empty_dir(
        self, value: Optional[pulumi.Input[ServiceTemplateVolumeEmptyDirArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def gcs(self) -> Optional[pulumi.Input[ServiceTemplateVolumeGcsArgs]]: ...
    @gcs.setter
    def gcs(self, value: Optional[pulumi.Input[ServiceTemplateVolumeGcsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Optional[pulumi.Input[ServiceTemplateVolumeNfsArgs]]: ...
    @nfs.setter
    def nfs(self, value: Optional[pulumi.Input[ServiceTemplateVolumeNfsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[ServiceTemplateVolumeSecretArgs]]: ...
    @secret.setter
    def secret(
        self, value: Optional[pulumi.Input[ServiceTemplateVolumeSecretArgs]]
    ): ...

class ServiceTemplateVolumeCloudSqlInstanceArgsDict(TypedDict):
    instances: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServiceTemplateVolumeCloudSqlInstanceArgs:
    def __init__(
        __self__,
        *,
        instances: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instances.setter
    def instances(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServiceTemplateVolumeEmptyDirArgsDict(TypedDict):
    medium: NotRequired[pulumi.Input[_builtins.str]]
    size_limit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateVolumeEmptyDirArgs:
    def __init__(
        __self__,
        *,
        medium: Optional[pulumi.Input[_builtins.str]] = ...,
        size_limit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @medium.setter
    def medium(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeLimit")
    def size_limit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @size_limit.setter
    def size_limit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateVolumeGcsArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    mount_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ServiceTemplateVolumeGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        mount_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @mount_options.setter
    def mount_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ServiceTemplateVolumeNfsArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    server: pulumi.Input[_builtins.str]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class ServiceTemplateVolumeNfsArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        server: pulumi.Input[_builtins.str],
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> pulumi.Input[_builtins.str]: ...
    @server.setter
    def server(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class ServiceTemplateVolumeSecretArgsDict(TypedDict):
    secret: pulumi.Input[_builtins.str]
    default_mode: NotRequired[pulumi.Input[_builtins.int]]
    items: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateVolumeSecretItemArgsDict]]]
    ]

@pulumi.input_type
class ServiceTemplateVolumeSecretArgs:
    def __init__(
        __self__,
        *,
        secret: pulumi.Input[_builtins.str],
        default_mode: Optional[pulumi.Input[_builtins.int]] = ...,
        items: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateVolumeSecretItemArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Input[_builtins.str]: ...
    @secret.setter
    def secret(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_mode.setter
    def default_mode(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[ServiceTemplateVolumeSecretItemArgs]]]
    ]: ...
    @items.setter
    def items(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[ServiceTemplateVolumeSecretItemArgs]]]
        ],
    ): ...

class ServiceTemplateVolumeSecretItemArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    mode: NotRequired[pulumi.Input[_builtins.int]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTemplateVolumeSecretItemArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        mode: Optional[pulumi.Input[_builtins.int]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTemplateVpcAccessArgsDict(TypedDict):
    connector: NotRequired[pulumi.Input[_builtins.str]]
    egress: NotRequired[pulumi.Input[_builtins.str]]
    network_interfaces: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[ServiceTemplateVpcAccessNetworkInterfaceArgsDict]]
        ]
    ]

@pulumi.input_type
class ServiceTemplateVpcAccessArgs:
    def __init__(
        __self__,
        *,
        connector: Optional[pulumi.Input[_builtins.str]] = ...,
        egress: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interfaces: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceTemplateVpcAccessNetworkInterfaceArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connector(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connector.setter
    def connector(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @egress.setter
    def egress(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[ServiceTemplateVpcAccessNetworkInterfaceArgs]]
        ]
    ]: ...
    @network_interfaces.setter
    def network_interfaces(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[ServiceTemplateVpcAccessNetworkInterfaceArgs]]
            ]
        ],
    ): ...

class ServiceTemplateVpcAccessNetworkInterfaceArgsDict(TypedDict):
    network: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class ServiceTemplateVpcAccessNetworkInterfaceArgs:
    def __init__(
        __self__,
        *,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class ServiceTerminalConditionArgsDict(TypedDict):
    execution_reason: NotRequired[pulumi.Input[_builtins.str]]
    last_transition_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    revision_reason: NotRequired[pulumi.Input[_builtins.str]]
    severity: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTerminalConditionArgs:
    def __init__(
        __self__,
        *,
        execution_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        last_transition_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        revision_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        severity: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_reason.setter
    def execution_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_transition_time.setter
    def last_transition_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_reason.setter
    def revision_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTrafficArgsDict(TypedDict):
    percent: NotRequired[pulumi.Input[_builtins.int]]
    revision: NotRequired[pulumi.Input[_builtins.str]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTrafficArgs:
    def __init__(
        __self__,
        *,
        percent: Optional[pulumi.Input[_builtins.int]] = ...,
        revision: Optional[pulumi.Input[_builtins.str]] = ...,
        tag: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percent.setter
    def percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class ServiceTrafficStatusArgsDict(TypedDict):
    percent: NotRequired[pulumi.Input[_builtins.int]]
    revision: NotRequired[pulumi.Input[_builtins.str]]
    tag: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]
    uri: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ServiceTrafficStatusArgs:
    def __init__(
        __self__,
        *,
        percent: Optional[pulumi.Input[_builtins.int]] = ...,
        revision: Optional[pulumi.Input[_builtins.str]] = ...,
        tag: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
        uri: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percent.setter
    def percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tag(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @tag.setter
    def tag(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def uri(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @uri.setter
    def uri(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolBinaryAuthorizationArgsDict(TypedDict):
    breakglass_justification: NotRequired[pulumi.Input[_builtins.str]]
    policy: NotRequired[pulumi.Input[_builtins.str]]
    use_default: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class WorkerPoolBinaryAuthorizationArgs:
    def __init__(
        __self__,
        *,
        breakglass_justification: Optional[pulumi.Input[_builtins.str]] = ...,
        policy: Optional[pulumi.Input[_builtins.str]] = ...,
        use_default: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="breakglassJustification")
    def breakglass_justification(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @breakglass_justification.setter
    def breakglass_justification(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def policy(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @policy.setter
    def policy(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="useDefault")
    def use_default(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @use_default.setter
    def use_default(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class WorkerPoolConditionArgsDict(TypedDict):
    execution_reason: NotRequired[pulumi.Input[_builtins.str]]
    last_transition_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    revision_reason: NotRequired[pulumi.Input[_builtins.str]]
    severity: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolConditionArgs:
    def __init__(
        __self__,
        *,
        execution_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        last_transition_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        revision_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        severity: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_reason.setter
    def execution_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_transition_time.setter
    def last_transition_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_reason.setter
    def revision_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolIamBindingConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolIamBindingConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolIamMemberConditionArgsDict(TypedDict):
    expression: pulumi.Input[_builtins.str]
    title: pulumi.Input[_builtins.str]
    description: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolIamMemberConditionArgs:
    def __init__(
        __self__,
        *,
        expression: pulumi.Input[_builtins.str],
        title: pulumi.Input[_builtins.str],
        description: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def expression(self) -> pulumi.Input[_builtins.str]: ...
    @expression.setter
    def expression(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def title(self) -> pulumi.Input[_builtins.str]: ...
    @title.setter
    def title(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @description.setter
    def description(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolInstanceSplitArgsDict(TypedDict):
    percent: NotRequired[pulumi.Input[_builtins.int]]
    revision: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolInstanceSplitArgs:
    def __init__(
        __self__,
        *,
        percent: Optional[pulumi.Input[_builtins.int]] = ...,
        revision: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percent.setter
    def percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolInstanceSplitStatusArgsDict(TypedDict):
    percent: NotRequired[pulumi.Input[_builtins.int]]
    revision: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolInstanceSplitStatusArgs:
    def __init__(
        __self__,
        *,
        percent: Optional[pulumi.Input[_builtins.int]] = ...,
        revision: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def percent(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @percent.setter
    def percent(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolScalingArgsDict(TypedDict):
    manual_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    max_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    min_instance_count: NotRequired[pulumi.Input[_builtins.int]]
    scaling_mode: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolScalingArgs:
    def __init__(
        __self__,
        *,
        manual_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        max_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        min_instance_count: Optional[pulumi.Input[_builtins.int]] = ...,
        scaling_mode: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="manualInstanceCount")
    def manual_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @manual_instance_count.setter
    def manual_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="maxInstanceCount")
    def max_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_instance_count.setter
    def max_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="minInstanceCount")
    def min_instance_count(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @min_instance_count.setter
    def min_instance_count(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="scalingMode")
    def scaling_mode(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @scaling_mode.setter
    def scaling_mode(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolTemplateArgsDict(TypedDict):
    annotations: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    containers: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateContainerArgsDict]]]
    ]
    encryption_key: NotRequired[pulumi.Input[_builtins.str]]
    encryption_key_revocation_action: NotRequired[pulumi.Input[_builtins.str]]
    encryption_key_shutdown_duration: NotRequired[pulumi.Input[_builtins.str]]
    gpu_zonal_redundancy_disabled: NotRequired[pulumi.Input[_builtins.bool]]
    labels: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    node_selector: NotRequired[pulumi.Input[WorkerPoolTemplateNodeSelectorArgsDict]]
    revision: NotRequired[pulumi.Input[_builtins.str]]
    service_account: NotRequired[pulumi.Input[_builtins.str]]
    volumes: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateVolumeArgsDict]]]
    ]
    vpc_access: NotRequired[pulumi.Input[WorkerPoolTemplateVpcAccessArgsDict]]

@pulumi.input_type
class WorkerPoolTemplateArgs:
    def __init__(
        __self__,
        *,
        annotations: Optional[
            pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]
        ] = ...,
        containers: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateContainerArgs]]]
        ] = ...,
        encryption_key: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_key_revocation_action: Optional[pulumi.Input[_builtins.str]] = ...,
        encryption_key_shutdown_duration: Optional[pulumi.Input[_builtins.str]] = ...,
        gpu_zonal_redundancy_disabled: Optional[pulumi.Input[_builtins.bool]] = ...,
        labels: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
        node_selector: Optional[pulumi.Input[WorkerPoolTemplateNodeSelectorArgs]] = ...,
        revision: Optional[pulumi.Input[_builtins.str]] = ...,
        service_account: Optional[pulumi.Input[_builtins.str]] = ...,
        volumes: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateVolumeArgs]]]
        ] = ...,
        vpc_access: Optional[pulumi.Input[WorkerPoolTemplateVpcAccessArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def annotations(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @annotations.setter
    def annotations(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def containers(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateContainerArgs]]]
    ]: ...
    @containers.setter
    def containers(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateContainerArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_key.setter
    def encryption_key(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyRevocationAction")
    def encryption_key_revocation_action(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_key_revocation_action.setter
    def encryption_key_revocation_action(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="encryptionKeyShutdownDuration")
    def encryption_key_shutdown_duration(
        self,
    ) -> Optional[pulumi.Input[_builtins.str]]: ...
    @encryption_key_shutdown_duration.setter
    def encryption_key_shutdown_duration(
        self, value: Optional[pulumi.Input[_builtins.str]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="gpuZonalRedundancyDisabled")
    def gpu_zonal_redundancy_disabled(
        self,
    ) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @gpu_zonal_redundancy_disabled.setter
    def gpu_zonal_redundancy_disabled(
        self, value: Optional[pulumi.Input[_builtins.bool]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def labels(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @labels.setter
    def labels(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="nodeSelector")
    def node_selector(
        self,
    ) -> Optional[pulumi.Input[WorkerPoolTemplateNodeSelectorArgs]]: ...
    @node_selector.setter
    def node_selector(
        self, value: Optional[pulumi.Input[WorkerPoolTemplateNodeSelectorArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision.setter
    def revision(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="serviceAccount")
    def service_account(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service_account.setter
    def service_account(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def volumes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateVolumeArgs]]]
    ]: ...
    @volumes.setter
    def volumes(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateVolumeArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="vpcAccess")
    def vpc_access(self) -> Optional[pulumi.Input[WorkerPoolTemplateVpcAccessArgs]]: ...
    @vpc_access.setter
    def vpc_access(
        self, value: Optional[pulumi.Input[WorkerPoolTemplateVpcAccessArgs]]
    ): ...

class WorkerPoolTemplateContainerArgsDict(TypedDict):
    image: pulumi.Input[_builtins.str]
    args: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    commands: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    depends_ons: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    envs: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateContainerEnvArgsDict]]]
    ]
    liveness_probe: NotRequired[
        pulumi.Input[WorkerPoolTemplateContainerLivenessProbeArgsDict]
    ]
    name: NotRequired[pulumi.Input[_builtins.str]]
    resources: NotRequired[pulumi.Input[WorkerPoolTemplateContainerResourcesArgsDict]]
    startup_probe: NotRequired[
        pulumi.Input[WorkerPoolTemplateContainerStartupProbeArgsDict]
    ]
    volume_mounts: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[WorkerPoolTemplateContainerVolumeMountArgsDict]]
        ]
    ]
    working_dir: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolTemplateContainerArgs:
    def __init__(
        __self__,
        *,
        image: pulumi.Input[_builtins.str],
        args: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        commands: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
        depends_ons: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        envs: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateContainerEnvArgs]]]
        ] = ...,
        liveness_probe: Optional[
            pulumi.Input[WorkerPoolTemplateContainerLivenessProbeArgs]
        ] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        resources: Optional[
            pulumi.Input[WorkerPoolTemplateContainerResourcesArgs]
        ] = ...,
        startup_probe: Optional[
            pulumi.Input[WorkerPoolTemplateContainerStartupProbeArgs]
        ] = ...,
        volume_mounts: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkerPoolTemplateContainerVolumeMountArgs]]
            ]
        ] = ...,
        working_dir: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def image(self) -> pulumi.Input[_builtins.str]: ...
    @image.setter
    def image(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def args(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @args.setter
    def args(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def commands(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @commands.setter
    def commands(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="dependsOns")
    def depends_ons(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @depends_ons.setter
    def depends_ons(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def envs(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateContainerEnvArgs]]]
    ]: ...
    @envs.setter
    def envs(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateContainerEnvArgs]]]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="livenessProbe")
    def liveness_probe(
        self,
    ) -> Optional[pulumi.Input[WorkerPoolTemplateContainerLivenessProbeArgs]]: ...
    @liveness_probe.setter
    def liveness_probe(
        self,
        value: Optional[pulumi.Input[WorkerPoolTemplateContainerLivenessProbeArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def resources(
        self,
    ) -> Optional[pulumi.Input[WorkerPoolTemplateContainerResourcesArgs]]: ...
    @resources.setter
    def resources(
        self, value: Optional[pulumi.Input[WorkerPoolTemplateContainerResourcesArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="startupProbe")
    def startup_probe(
        self,
    ) -> Optional[pulumi.Input[WorkerPoolTemplateContainerStartupProbeArgs]]: ...
    @startup_probe.setter
    def startup_probe(
        self, value: Optional[pulumi.Input[WorkerPoolTemplateContainerStartupProbeArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="volumeMounts")
    def volume_mounts(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateContainerVolumeMountArgs]]]
    ]: ...
    @volume_mounts.setter
    def volume_mounts(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkerPoolTemplateContainerVolumeMountArgs]]
            ]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="workingDir")
    def working_dir(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @working_dir.setter
    def working_dir(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolTemplateContainerEnvArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    value: NotRequired[pulumi.Input[_builtins.str]]
    value_source: NotRequired[
        pulumi.Input[WorkerPoolTemplateContainerEnvValueSourceArgsDict]
    ]

@pulumi.input_type
class WorkerPoolTemplateContainerEnvArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
        value_source: Optional[
            pulumi.Input[WorkerPoolTemplateContainerEnvValueSourceArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="valueSource")
    def value_source(
        self,
    ) -> Optional[pulumi.Input[WorkerPoolTemplateContainerEnvValueSourceArgs]]: ...
    @value_source.setter
    def value_source(
        self,
        value: Optional[pulumi.Input[WorkerPoolTemplateContainerEnvValueSourceArgs]],
    ): ...

class WorkerPoolTemplateContainerEnvValueSourceArgsDict(TypedDict):
    secret_key_ref: NotRequired[
        pulumi.Input[WorkerPoolTemplateContainerEnvValueSourceSecretKeyRefArgsDict]
    ]

@pulumi.input_type
class WorkerPoolTemplateContainerEnvValueSourceArgs:
    def __init__(
        __self__,
        *,
        secret_key_ref: Optional[
            pulumi.Input[WorkerPoolTemplateContainerEnvValueSourceSecretKeyRefArgs]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="secretKeyRef")
    def secret_key_ref(
        self,
    ) -> Optional[
        pulumi.Input[WorkerPoolTemplateContainerEnvValueSourceSecretKeyRefArgs]
    ]: ...
    @secret_key_ref.setter
    def secret_key_ref(
        self,
        value: Optional[
            pulumi.Input[WorkerPoolTemplateContainerEnvValueSourceSecretKeyRefArgs]
        ],
    ): ...

class WorkerPoolTemplateContainerEnvValueSourceSecretKeyRefArgsDict(TypedDict):
    secret: pulumi.Input[_builtins.str]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolTemplateContainerEnvValueSourceSecretKeyRefArgs:
    def __init__(
        __self__,
        *,
        secret: pulumi.Input[_builtins.str],
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Input[_builtins.str]: ...
    @secret.setter
    def secret(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolTemplateContainerLivenessProbeArgsDict(TypedDict):
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    grpc: NotRequired[
        pulumi.Input[WorkerPoolTemplateContainerLivenessProbeGrpcArgsDict]
    ]
    http_get: NotRequired[
        pulumi.Input[WorkerPoolTemplateContainerLivenessProbeHttpGetArgsDict]
    ]
    initial_delay_seconds: NotRequired[pulumi.Input[_builtins.int]]
    period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    tcp_socket: NotRequired[
        pulumi.Input[WorkerPoolTemplateContainerLivenessProbeTcpSocketArgsDict]
    ]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WorkerPoolTemplateContainerLivenessProbeArgs:
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        grpc: Optional[
            pulumi.Input[WorkerPoolTemplateContainerLivenessProbeGrpcArgs]
        ] = ...,
        http_get: Optional[
            pulumi.Input[WorkerPoolTemplateContainerLivenessProbeHttpGetArgs]
        ] = ...,
        initial_delay_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tcp_socket: Optional[
            pulumi.Input[WorkerPoolTemplateContainerLivenessProbeTcpSocketArgs]
        ] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[pulumi.Input[WorkerPoolTemplateContainerLivenessProbeGrpcArgs]]: ...
    @grpc.setter
    def grpc(
        self,
        value: Optional[pulumi.Input[WorkerPoolTemplateContainerLivenessProbeGrpcArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[
        pulumi.Input[WorkerPoolTemplateContainerLivenessProbeHttpGetArgs]
    ]: ...
    @http_get.setter
    def http_get(
        self,
        value: Optional[
            pulumi.Input[WorkerPoolTemplateContainerLivenessProbeHttpGetArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period_seconds.setter
    def period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(
        self,
    ) -> Optional[
        pulumi.Input[WorkerPoolTemplateContainerLivenessProbeTcpSocketArgs]
    ]: ...
    @tcp_socket.setter
    def tcp_socket(
        self,
        value: Optional[
            pulumi.Input[WorkerPoolTemplateContainerLivenessProbeTcpSocketArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class WorkerPoolTemplateContainerLivenessProbeGrpcArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]
    service: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolTemplateContainerLivenessProbeGrpcArgs:
    def __init__(
        __self__,
        *,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolTemplateContainerLivenessProbeHttpGetArgsDict(TypedDict):
    http_headers: NotRequired[
        pulumi.Input[WorkerPoolTemplateContainerLivenessProbeHttpGetHttpHeadersArgsDict]
    ]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WorkerPoolTemplateContainerLivenessProbeHttpGetArgs:
    def __init__(
        __self__,
        *,
        http_headers: Optional[
            pulumi.Input[WorkerPoolTemplateContainerLivenessProbeHttpGetHttpHeadersArgs]
        ] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        pulumi.Input[WorkerPoolTemplateContainerLivenessProbeHttpGetHttpHeadersArgs]
    ]: ...
    @http_headers.setter
    def http_headers(
        self,
        value: Optional[
            pulumi.Input[WorkerPoolTemplateContainerLivenessProbeHttpGetHttpHeadersArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class WorkerPoolTemplateContainerLivenessProbeHttpGetHttpHeadersArgsDict(TypedDict):
    port: pulumi.Input[_builtins.int]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolTemplateContainerLivenessProbeHttpGetHttpHeadersArgs:
    def __init__(
        __self__,
        *,
        port: pulumi.Input[_builtins.int],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolTemplateContainerLivenessProbeTcpSocketArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WorkerPoolTemplateContainerLivenessProbeTcpSocketArgs:
    def __init__(
        __self__, *, port: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class WorkerPoolTemplateContainerResourcesArgsDict(TypedDict):
    limits: NotRequired[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WorkerPoolTemplateContainerResourcesArgs:
    def __init__(
        __self__,
        *,
        limits: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def limits(
        self,
    ) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]: ...
    @limits.setter
    def limits(
        self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[_builtins.str]]]]
    ): ...

class WorkerPoolTemplateContainerStartupProbeArgsDict(TypedDict):
    failure_threshold: NotRequired[pulumi.Input[_builtins.int]]
    grpc: NotRequired[pulumi.Input[WorkerPoolTemplateContainerStartupProbeGrpcArgsDict]]
    http_get: NotRequired[
        pulumi.Input[WorkerPoolTemplateContainerStartupProbeHttpGetArgsDict]
    ]
    initial_delay_seconds: NotRequired[pulumi.Input[_builtins.int]]
    period_seconds: NotRequired[pulumi.Input[_builtins.int]]
    tcp_socket: NotRequired[
        pulumi.Input[WorkerPoolTemplateContainerStartupProbeTcpSocketArgsDict]
    ]
    timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WorkerPoolTemplateContainerStartupProbeArgs:
    def __init__(
        __self__,
        *,
        failure_threshold: Optional[pulumi.Input[_builtins.int]] = ...,
        grpc: Optional[
            pulumi.Input[WorkerPoolTemplateContainerStartupProbeGrpcArgs]
        ] = ...,
        http_get: Optional[
            pulumi.Input[WorkerPoolTemplateContainerStartupProbeHttpGetArgs]
        ] = ...,
        initial_delay_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        period_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
        tcp_socket: Optional[
            pulumi.Input[WorkerPoolTemplateContainerStartupProbeTcpSocketArgs]
        ] = ...,
        timeout_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="failureThreshold")
    def failure_threshold(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @failure_threshold.setter
    def failure_threshold(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def grpc(
        self,
    ) -> Optional[pulumi.Input[WorkerPoolTemplateContainerStartupProbeGrpcArgs]]: ...
    @grpc.setter
    def grpc(
        self,
        value: Optional[pulumi.Input[WorkerPoolTemplateContainerStartupProbeGrpcArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="httpGet")
    def http_get(
        self,
    ) -> Optional[pulumi.Input[WorkerPoolTemplateContainerStartupProbeHttpGetArgs]]: ...
    @http_get.setter
    def http_get(
        self,
        value: Optional[
            pulumi.Input[WorkerPoolTemplateContainerStartupProbeHttpGetArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="initialDelaySeconds")
    def initial_delay_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @initial_delay_seconds.setter
    def initial_delay_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="periodSeconds")
    def period_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @period_seconds.setter
    def period_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter(name="tcpSocket")
    def tcp_socket(
        self,
    ) -> Optional[
        pulumi.Input[WorkerPoolTemplateContainerStartupProbeTcpSocketArgs]
    ]: ...
    @tcp_socket.setter
    def tcp_socket(
        self,
        value: Optional[
            pulumi.Input[WorkerPoolTemplateContainerStartupProbeTcpSocketArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="timeoutSeconds")
    def timeout_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @timeout_seconds.setter
    def timeout_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class WorkerPoolTemplateContainerStartupProbeGrpcArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]
    service: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolTemplateContainerStartupProbeGrpcArgs:
    def __init__(
        __self__,
        *,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
        service: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def service(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @service.setter
    def service(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolTemplateContainerStartupProbeHttpGetArgsDict(TypedDict):
    http_headers: NotRequired[
        pulumi.Input[WorkerPoolTemplateContainerStartupProbeHttpGetHttpHeadersArgsDict]
    ]
    path: NotRequired[pulumi.Input[_builtins.str]]
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WorkerPoolTemplateContainerStartupProbeHttpGetArgs:
    def __init__(
        __self__,
        *,
        http_headers: Optional[
            pulumi.Input[WorkerPoolTemplateContainerStartupProbeHttpGetHttpHeadersArgs]
        ] = ...,
        path: Optional[pulumi.Input[_builtins.str]] = ...,
        port: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="httpHeaders")
    def http_headers(
        self,
    ) -> Optional[
        pulumi.Input[WorkerPoolTemplateContainerStartupProbeHttpGetHttpHeadersArgs]
    ]: ...
    @http_headers.setter
    def http_headers(
        self,
        value: Optional[
            pulumi.Input[WorkerPoolTemplateContainerStartupProbeHttpGetHttpHeadersArgs]
        ],
    ): ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @path.setter
    def path(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class WorkerPoolTemplateContainerStartupProbeHttpGetHttpHeadersArgsDict(TypedDict):
    port: pulumi.Input[_builtins.int]
    value: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolTemplateContainerStartupProbeHttpGetHttpHeadersArgs:
    def __init__(
        __self__,
        *,
        port: pulumi.Input[_builtins.int],
        value: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> pulumi.Input[_builtins.int]: ...
    @port.setter
    def port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @value.setter
    def value(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolTemplateContainerStartupProbeTcpSocketArgsDict(TypedDict):
    port: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class WorkerPoolTemplateContainerStartupProbeTcpSocketArgs:
    def __init__(
        __self__, *, port: Optional[pulumi.Input[_builtins.int]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @port.setter
    def port(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class WorkerPoolTemplateContainerVolumeMountArgsDict(TypedDict):
    mount_path: pulumi.Input[_builtins.str]
    name: pulumi.Input[_builtins.str]
    sub_path: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolTemplateContainerVolumeMountArgs:
    def __init__(
        __self__,
        *,
        mount_path: pulumi.Input[_builtins.str],
        name: pulumi.Input[_builtins.str],
        sub_path: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="mountPath")
    def mount_path(self) -> pulumi.Input[_builtins.str]: ...
    @mount_path.setter
    def mount_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="subPath")
    def sub_path(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @sub_path.setter
    def sub_path(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolTemplateNodeSelectorArgsDict(TypedDict):
    accelerator: pulumi.Input[_builtins.str]

@pulumi.input_type
class WorkerPoolTemplateNodeSelectorArgs:
    def __init__(__self__, *, accelerator: pulumi.Input[_builtins.str]) -> None: ...
    @_builtins.property
    @pulumi.getter
    def accelerator(self) -> pulumi.Input[_builtins.str]: ...
    @accelerator.setter
    def accelerator(self, value: pulumi.Input[_builtins.str]): ...

class WorkerPoolTemplateVolumeArgsDict(TypedDict):
    name: pulumi.Input[_builtins.str]
    cloud_sql_instance: NotRequired[
        pulumi.Input[WorkerPoolTemplateVolumeCloudSqlInstanceArgsDict]
    ]
    empty_dir: NotRequired[pulumi.Input[WorkerPoolTemplateVolumeEmptyDirArgsDict]]
    gcs: NotRequired[pulumi.Input[WorkerPoolTemplateVolumeGcsArgsDict]]
    nfs: NotRequired[pulumi.Input[WorkerPoolTemplateVolumeNfsArgsDict]]
    secret: NotRequired[pulumi.Input[WorkerPoolTemplateVolumeSecretArgsDict]]

@pulumi.input_type
class WorkerPoolTemplateVolumeArgs:
    def __init__(
        __self__,
        *,
        name: pulumi.Input[_builtins.str],
        cloud_sql_instance: Optional[
            pulumi.Input[WorkerPoolTemplateVolumeCloudSqlInstanceArgs]
        ] = ...,
        empty_dir: Optional[pulumi.Input[WorkerPoolTemplateVolumeEmptyDirArgs]] = ...,
        gcs: Optional[pulumi.Input[WorkerPoolTemplateVolumeGcsArgs]] = ...,
        nfs: Optional[pulumi.Input[WorkerPoolTemplateVolumeNfsArgs]] = ...,
        secret: Optional[pulumi.Input[WorkerPoolTemplateVolumeSecretArgs]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> pulumi.Input[_builtins.str]: ...
    @name.setter
    def name(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="cloudSqlInstance")
    def cloud_sql_instance(
        self,
    ) -> Optional[pulumi.Input[WorkerPoolTemplateVolumeCloudSqlInstanceArgs]]: ...
    @cloud_sql_instance.setter
    def cloud_sql_instance(
        self,
        value: Optional[pulumi.Input[WorkerPoolTemplateVolumeCloudSqlInstanceArgs]],
    ): ...
    @_builtins.property
    @pulumi.getter(name="emptyDir")
    def empty_dir(
        self,
    ) -> Optional[pulumi.Input[WorkerPoolTemplateVolumeEmptyDirArgs]]: ...
    @empty_dir.setter
    def empty_dir(
        self, value: Optional[pulumi.Input[WorkerPoolTemplateVolumeEmptyDirArgs]]
    ): ...
    @_builtins.property
    @pulumi.getter
    def gcs(self) -> Optional[pulumi.Input[WorkerPoolTemplateVolumeGcsArgs]]: ...
    @gcs.setter
    def gcs(self, value: Optional[pulumi.Input[WorkerPoolTemplateVolumeGcsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def nfs(self) -> Optional[pulumi.Input[WorkerPoolTemplateVolumeNfsArgs]]: ...
    @nfs.setter
    def nfs(self, value: Optional[pulumi.Input[WorkerPoolTemplateVolumeNfsArgs]]): ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> Optional[pulumi.Input[WorkerPoolTemplateVolumeSecretArgs]]: ...
    @secret.setter
    def secret(
        self, value: Optional[pulumi.Input[WorkerPoolTemplateVolumeSecretArgs]]
    ): ...

class WorkerPoolTemplateVolumeCloudSqlInstanceArgsDict(TypedDict):
    instances: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WorkerPoolTemplateVolumeCloudSqlInstanceArgs:
    def __init__(
        __self__,
        *,
        instances: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def instances(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @instances.setter
    def instances(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class WorkerPoolTemplateVolumeEmptyDirArgsDict(TypedDict):
    medium: NotRequired[pulumi.Input[_builtins.str]]
    size_limit: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolTemplateVolumeEmptyDirArgs:
    def __init__(
        __self__,
        *,
        medium: Optional[pulumi.Input[_builtins.str]] = ...,
        size_limit: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def medium(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @medium.setter
    def medium(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="sizeLimit")
    def size_limit(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @size_limit.setter
    def size_limit(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolTemplateVolumeGcsArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    mount_options: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class WorkerPoolTemplateVolumeGcsArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        mount_options: Optional[
            pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]
        ] = ...,
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="mountOptions")
    def mount_options(
        self,
    ) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @mount_options.setter
    def mount_options(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class WorkerPoolTemplateVolumeNfsArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    server: pulumi.Input[_builtins.str]
    read_only: NotRequired[pulumi.Input[_builtins.bool]]

@pulumi.input_type
class WorkerPoolTemplateVolumeNfsArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        server: pulumi.Input[_builtins.str],
        read_only: Optional[pulumi.Input[_builtins.bool]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def server(self) -> pulumi.Input[_builtins.str]: ...
    @server.setter
    def server(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="readOnly")
    def read_only(self) -> Optional[pulumi.Input[_builtins.bool]]: ...
    @read_only.setter
    def read_only(self, value: Optional[pulumi.Input[_builtins.bool]]): ...

class WorkerPoolTemplateVolumeSecretArgsDict(TypedDict):
    secret: pulumi.Input[_builtins.str]
    default_mode: NotRequired[pulumi.Input[_builtins.int]]
    items: NotRequired[
        pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateVolumeSecretItemArgsDict]]]
    ]

@pulumi.input_type
class WorkerPoolTemplateVolumeSecretArgs:
    def __init__(
        __self__,
        *,
        secret: pulumi.Input[_builtins.str],
        default_mode: Optional[pulumi.Input[_builtins.int]] = ...,
        items: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateVolumeSecretItemArgs]]]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def secret(self) -> pulumi.Input[_builtins.str]: ...
    @secret.setter
    def secret(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="defaultMode")
    def default_mode(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @default_mode.setter
    def default_mode(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def items(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateVolumeSecretItemArgs]]]
    ]: ...
    @items.setter
    def items(
        self,
        value: Optional[
            pulumi.Input[Sequence[pulumi.Input[WorkerPoolTemplateVolumeSecretItemArgs]]]
        ],
    ): ...

class WorkerPoolTemplateVolumeSecretItemArgsDict(TypedDict):
    path: pulumi.Input[_builtins.str]
    mode: NotRequired[pulumi.Input[_builtins.int]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolTemplateVolumeSecretItemArgs:
    def __init__(
        __self__,
        *,
        path: pulumi.Input[_builtins.str],
        mode: Optional[pulumi.Input[_builtins.int]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def path(self) -> pulumi.Input[_builtins.str]: ...
    @path.setter
    def path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def mode(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @mode.setter
    def mode(self, value: Optional[pulumi.Input[_builtins.int]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class WorkerPoolTemplateVpcAccessArgsDict(TypedDict):
    connector: NotRequired[pulumi.Input[_builtins.str]]
    egress: NotRequired[pulumi.Input[_builtins.str]]
    network_interfaces: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[WorkerPoolTemplateVpcAccessNetworkInterfaceArgsDict]]
        ]
    ]

@pulumi.input_type
class WorkerPoolTemplateVpcAccessArgs:
    def __init__(
        __self__,
        *,
        connector: Optional[pulumi.Input[_builtins.str]] = ...,
        egress: Optional[pulumi.Input[_builtins.str]] = ...,
        network_interfaces: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkerPoolTemplateVpcAccessNetworkInterfaceArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def connector(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @connector.setter
    def connector(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def egress(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @egress.setter
    def egress(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(
        self,
    ) -> Optional[
        pulumi.Input[
            Sequence[pulumi.Input[WorkerPoolTemplateVpcAccessNetworkInterfaceArgs]]
        ]
    ]: ...
    @network_interfaces.setter
    def network_interfaces(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[WorkerPoolTemplateVpcAccessNetworkInterfaceArgs]]
            ]
        ],
    ): ...

class WorkerPoolTemplateVpcAccessNetworkInterfaceArgsDict(TypedDict):
    network: NotRequired[pulumi.Input[_builtins.str]]
    subnetwork: NotRequired[pulumi.Input[_builtins.str]]
    tags: NotRequired[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]

@pulumi.input_type
class WorkerPoolTemplateVpcAccessNetworkInterfaceArgs:
    def __init__(
        __self__,
        *,
        network: Optional[pulumi.Input[_builtins.str]] = ...,
        subnetwork: Optional[pulumi.Input[_builtins.str]] = ...,
        tags: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def network(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @network.setter
    def network(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def subnetwork(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @subnetwork.setter
    def subnetwork(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]: ...
    @tags.setter
    def tags(
        self, value: Optional[pulumi.Input[Sequence[pulumi.Input[_builtins.str]]]]
    ): ...

class WorkerPoolTerminalConditionArgsDict(TypedDict):
    execution_reason: NotRequired[pulumi.Input[_builtins.str]]
    last_transition_time: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]
    reason: NotRequired[pulumi.Input[_builtins.str]]
    revision_reason: NotRequired[pulumi.Input[_builtins.str]]
    severity: NotRequired[pulumi.Input[_builtins.str]]
    state: NotRequired[pulumi.Input[_builtins.str]]
    type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class WorkerPoolTerminalConditionArgs:
    def __init__(
        __self__,
        *,
        execution_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        last_transition_time: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
        reason: Optional[pulumi.Input[_builtins.str]] = ...,
        revision_reason: Optional[pulumi.Input[_builtins.str]] = ...,
        severity: Optional[pulumi.Input[_builtins.str]] = ...,
        state: Optional[pulumi.Input[_builtins.str]] = ...,
        type: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="executionReason")
    def execution_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @execution_reason.setter
    def execution_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="lastTransitionTime")
    def last_transition_time(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @last_transition_time.setter
    def last_transition_time(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @reason.setter
    def reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter(name="revisionReason")
    def revision_reason(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @revision_reason.setter
    def revision_reason(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @severity.setter
    def severity(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @state.setter
    def state(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @type.setter
    def type(self, value: Optional[pulumi.Input[_builtins.str]]): ...
