import builtins as _builtins
import sys
import pulumi
from typing import NotRequired, Optional, Sequence, TypedDict

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AliasRoutingStrategyArgs",
    "AliasRoutingStrategyArgsDict",
    "BuildStorageLocationArgs",
    "BuildStorageLocationArgsDict",
    "FleetCertificateConfigurationArgs",
    "FleetCertificateConfigurationArgsDict",
    "FleetEc2InboundPermissionArgs",
    "FleetEc2InboundPermissionArgsDict",
    "FleetResourceCreationLimitPolicyArgs",
    "FleetResourceCreationLimitPolicyArgsDict",
    "FleetRuntimeConfigurationArgs",
    "FleetRuntimeConfigurationArgsDict",
    "FleetRuntimeConfigurationServerProcessArgs",
    "FleetRuntimeConfigurationServerProcessArgsDict",
    "GameServerGroupAutoScalingPolicyArgs",
    "GameServerGroupAutoScalingPolicyArgsDict",
    ...,
    ...,
    "GameServerGroupInstanceDefinitionArgs",
    "GameServerGroupInstanceDefinitionArgsDict",
    "GameServerGroupLaunchTemplateArgs",
    "GameServerGroupLaunchTemplateArgsDict",
    "GameSessionQueuePlayerLatencyPolicyArgs",
    "GameSessionQueuePlayerLatencyPolicyArgsDict",
    "ScriptStorageLocationArgs",
    "ScriptStorageLocationArgsDict",
]

class AliasRoutingStrategyArgsDict(TypedDict):
    type: pulumi.Input[_builtins.str]
    fleet_id: NotRequired[pulumi.Input[_builtins.str]]
    message: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class AliasRoutingStrategyArgs:
    def __init__(
        __self__,
        *,
        type: pulumi.Input[_builtins.str],
        fleet_id: Optional[pulumi.Input[_builtins.str]] = ...,
        message: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> pulumi.Input[_builtins.str]: ...
    @type.setter
    def type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="fleetId")
    def fleet_id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @fleet_id.setter
    def fleet_id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @message.setter
    def message(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class BuildStorageLocationArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    object_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class BuildStorageLocationArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        object_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="objectVersion")
    def object_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_version.setter
    def object_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FleetCertificateConfigurationArgsDict(TypedDict):
    certificate_type: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FleetCertificateConfigurationArgs:
    def __init__(
        __self__, *, certificate_type: Optional[pulumi.Input[_builtins.str]] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateType")
    def certificate_type(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @certificate_type.setter
    def certificate_type(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class FleetEc2InboundPermissionArgsDict(TypedDict):
    from_port: pulumi.Input[_builtins.int]
    ip_range: pulumi.Input[_builtins.str]
    protocol: pulumi.Input[_builtins.str]
    to_port: pulumi.Input[_builtins.int]

@pulumi.input_type
class FleetEc2InboundPermissionArgs:
    def __init__(
        __self__,
        *,
        from_port: pulumi.Input[_builtins.int],
        ip_range: pulumi.Input[_builtins.str],
        protocol: pulumi.Input[_builtins.str],
        to_port: pulumi.Input[_builtins.int],
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> pulumi.Input[_builtins.int]: ...
    @from_port.setter
    def from_port(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="ipRange")
    def ip_range(self) -> pulumi.Input[_builtins.str]: ...
    @ip_range.setter
    def ip_range(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> pulumi.Input[_builtins.str]: ...
    @protocol.setter
    def protocol(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> pulumi.Input[_builtins.int]: ...
    @to_port.setter
    def to_port(self, value: pulumi.Input[_builtins.int]): ...

class FleetResourceCreationLimitPolicyArgsDict(TypedDict):
    new_game_sessions_per_creator: NotRequired[pulumi.Input[_builtins.int]]
    policy_period_in_minutes: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class FleetResourceCreationLimitPolicyArgs:
    def __init__(
        __self__,
        *,
        new_game_sessions_per_creator: Optional[pulumi.Input[_builtins.int]] = ...,
        policy_period_in_minutes: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="newGameSessionsPerCreator")
    def new_game_sessions_per_creator(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @new_game_sessions_per_creator.setter
    def new_game_sessions_per_creator(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyPeriodInMinutes")
    def policy_period_in_minutes(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @policy_period_in_minutes.setter
    def policy_period_in_minutes(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class FleetRuntimeConfigurationArgsDict(TypedDict):
    game_session_activation_timeout_seconds: NotRequired[pulumi.Input[_builtins.int]]
    max_concurrent_game_session_activations: NotRequired[pulumi.Input[_builtins.int]]
    server_processes: NotRequired[
        pulumi.Input[
            Sequence[pulumi.Input[FleetRuntimeConfigurationServerProcessArgsDict]]
        ]
    ]

@pulumi.input_type
class FleetRuntimeConfigurationArgs:
    def __init__(
        __self__,
        *,
        game_session_activation_timeout_seconds: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        max_concurrent_game_session_activations: Optional[
            pulumi.Input[_builtins.int]
        ] = ...,
        server_processes: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FleetRuntimeConfigurationServerProcessArgs]]
            ]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gameSessionActivationTimeoutSeconds")
    def game_session_activation_timeout_seconds(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @game_session_activation_timeout_seconds.setter
    def game_session_activation_timeout_seconds(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentGameSessionActivations")
    def max_concurrent_game_session_activations(
        self,
    ) -> Optional[pulumi.Input[_builtins.int]]: ...
    @max_concurrent_game_session_activations.setter
    def max_concurrent_game_session_activations(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...
    @_builtins.property
    @pulumi.getter(name="serverProcesses")
    def server_processes(
        self,
    ) -> Optional[
        pulumi.Input[Sequence[pulumi.Input[FleetRuntimeConfigurationServerProcessArgs]]]
    ]: ...
    @server_processes.setter
    def server_processes(
        self,
        value: Optional[
            pulumi.Input[
                Sequence[pulumi.Input[FleetRuntimeConfigurationServerProcessArgs]]
            ]
        ],
    ): ...

class FleetRuntimeConfigurationServerProcessArgsDict(TypedDict):
    concurrent_executions: pulumi.Input[_builtins.int]
    launch_path: pulumi.Input[_builtins.str]
    parameters: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class FleetRuntimeConfigurationServerProcessArgs:
    def __init__(
        __self__,
        *,
        concurrent_executions: pulumi.Input[_builtins.int],
        launch_path: pulumi.Input[_builtins.str],
        parameters: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="concurrentExecutions")
    def concurrent_executions(self) -> pulumi.Input[_builtins.int]: ...
    @concurrent_executions.setter
    def concurrent_executions(self, value: pulumi.Input[_builtins.int]): ...
    @_builtins.property
    @pulumi.getter(name="launchPath")
    def launch_path(self) -> pulumi.Input[_builtins.str]: ...
    @launch_path.setter
    def launch_path(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GameServerGroupAutoScalingPolicyArgsDict(TypedDict):
    target_tracking_configuration: pulumi.Input[
        GameServerGroupAutoScalingPolicyTargetTrackingConfigurationArgsDict
    ]
    estimated_instance_warmup: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GameServerGroupAutoScalingPolicyArgs:
    def __init__(
        __self__,
        *,
        target_tracking_configuration: pulumi.Input[
            GameServerGroupAutoScalingPolicyTargetTrackingConfigurationArgs
        ],
        estimated_instance_warmup: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetTrackingConfiguration")
    def target_tracking_configuration(
        self,
    ) -> pulumi.Input[
        GameServerGroupAutoScalingPolicyTargetTrackingConfigurationArgs
    ]: ...
    @target_tracking_configuration.setter
    def target_tracking_configuration(
        self,
        value: pulumi.Input[
            GameServerGroupAutoScalingPolicyTargetTrackingConfigurationArgs
        ],
    ): ...
    @_builtins.property
    @pulumi.getter(name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @estimated_instance_warmup.setter
    def estimated_instance_warmup(
        self, value: Optional[pulumi.Input[_builtins.int]]
    ): ...

class GameServerGroupAutoScalingPolicyTargetTrackingConfigurationArgsDict(TypedDict):
    target_value: pulumi.Input[_builtins.float]

@pulumi.input_type
class GameServerGroupAutoScalingPolicyTargetTrackingConfigurationArgs:
    def __init__(__self__, *, target_value: pulumi.Input[_builtins.float]) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> pulumi.Input[_builtins.float]: ...
    @target_value.setter
    def target_value(self, value: pulumi.Input[_builtins.float]): ...

class GameServerGroupInstanceDefinitionArgsDict(TypedDict):
    instance_type: pulumi.Input[_builtins.str]
    weighted_capacity: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GameServerGroupInstanceDefinitionArgs:
    def __init__(
        __self__,
        *,
        instance_type: pulumi.Input[_builtins.str],
        weighted_capacity: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> pulumi.Input[_builtins.str]: ...
    @instance_type.setter
    def instance_type(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @weighted_capacity.setter
    def weighted_capacity(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GameServerGroupLaunchTemplateArgsDict(TypedDict):
    id: NotRequired[pulumi.Input[_builtins.str]]
    name: NotRequired[pulumi.Input[_builtins.str]]
    version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class GameServerGroupLaunchTemplateArgs:
    def __init__(
        __self__,
        *,
        id: Optional[pulumi.Input[_builtins.str]] = ...,
        name: Optional[pulumi.Input[_builtins.str]] = ...,
        version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @id.setter
    def id(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @name.setter
    def name(self, value: Optional[pulumi.Input[_builtins.str]]): ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @version.setter
    def version(self, value: Optional[pulumi.Input[_builtins.str]]): ...

class GameSessionQueuePlayerLatencyPolicyArgsDict(TypedDict):
    maximum_individual_player_latency_milliseconds: pulumi.Input[_builtins.int]
    policy_duration_seconds: NotRequired[pulumi.Input[_builtins.int]]

@pulumi.input_type
class GameSessionQueuePlayerLatencyPolicyArgs:
    def __init__(
        __self__,
        *,
        maximum_individual_player_latency_milliseconds: pulumi.Input[_builtins.int],
        policy_duration_seconds: Optional[pulumi.Input[_builtins.int]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumIndividualPlayerLatencyMilliseconds")
    def maximum_individual_player_latency_milliseconds(
        self,
    ) -> pulumi.Input[_builtins.int]: ...
    @maximum_individual_player_latency_milliseconds.setter
    def maximum_individual_player_latency_milliseconds(
        self, value: pulumi.Input[_builtins.int]
    ): ...
    @_builtins.property
    @pulumi.getter(name="policyDurationSeconds")
    def policy_duration_seconds(self) -> Optional[pulumi.Input[_builtins.int]]: ...
    @policy_duration_seconds.setter
    def policy_duration_seconds(self, value: Optional[pulumi.Input[_builtins.int]]): ...

class ScriptStorageLocationArgsDict(TypedDict):
    bucket: pulumi.Input[_builtins.str]
    key: pulumi.Input[_builtins.str]
    role_arn: pulumi.Input[_builtins.str]
    object_version: NotRequired[pulumi.Input[_builtins.str]]

@pulumi.input_type
class ScriptStorageLocationArgs:
    def __init__(
        __self__,
        *,
        bucket: pulumi.Input[_builtins.str],
        key: pulumi.Input[_builtins.str],
        role_arn: pulumi.Input[_builtins.str],
        object_version: Optional[pulumi.Input[_builtins.str]] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> pulumi.Input[_builtins.str]: ...
    @bucket.setter
    def bucket(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> pulumi.Input[_builtins.str]: ...
    @key.setter
    def key(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> pulumi.Input[_builtins.str]: ...
    @role_arn.setter
    def role_arn(self, value: pulumi.Input[_builtins.str]): ...
    @_builtins.property
    @pulumi.getter(name="objectVersion")
    def object_version(self) -> Optional[pulumi.Input[_builtins.str]]: ...
    @object_version.setter
    def object_version(self, value: Optional[pulumi.Input[_builtins.str]]): ...
