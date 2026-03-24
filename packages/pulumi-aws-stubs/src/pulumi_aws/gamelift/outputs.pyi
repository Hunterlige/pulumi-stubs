import builtins as _builtins
import sys
import pulumi
from typing import Any, Optional, Sequence
from . import outputs

if sys.version_info >= (3, 11): ...
else: ...
__all__ = [
    "AliasRoutingStrategy",
    "BuildStorageLocation",
    "FleetCertificateConfiguration",
    "FleetEc2InboundPermission",
    "FleetResourceCreationLimitPolicy",
    "FleetRuntimeConfiguration",
    "FleetRuntimeConfigurationServerProcess",
    "GameServerGroupAutoScalingPolicy",
    ...,
    "GameServerGroupInstanceDefinition",
    "GameServerGroupLaunchTemplate",
    "GameSessionQueuePlayerLatencyPolicy",
    "ScriptStorageLocation",
]

@pulumi.output_type
class AliasRoutingStrategy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        type: _builtins.str,
        fleet_id: Optional[_builtins.str] = ...,
        message: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="fleetId")
    def fleet_id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def message(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class BuildStorageLocation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        key: _builtins.str,
        role_arn: _builtins.str,
        object_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectVersion")
    def object_version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FleetCertificateConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__, *, certificate_type: Optional[_builtins.str] = ...
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="certificateType")
    def certificate_type(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class FleetEc2InboundPermission(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        from_port: _builtins.int,
        ip_range: _builtins.str,
        protocol: _builtins.str,
        to_port: _builtins.int,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="fromPort")
    def from_port(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="ipRange")
    def ip_range(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def protocol(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="toPort")
    def to_port(self) -> _builtins.int: ...

@pulumi.output_type
class FleetResourceCreationLimitPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        new_game_sessions_per_creator: Optional[_builtins.int] = ...,
        policy_period_in_minutes: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="newGameSessionsPerCreator")
    def new_game_sessions_per_creator(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="policyPeriodInMinutes")
    def policy_period_in_minutes(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class FleetRuntimeConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        game_session_activation_timeout_seconds: Optional[_builtins.int] = ...,
        max_concurrent_game_session_activations: Optional[_builtins.int] = ...,
        server_processes: Optional[
            Sequence[outputs.FleetRuntimeConfigurationServerProcess]
        ] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="gameSessionActivationTimeoutSeconds")
    def game_session_activation_timeout_seconds(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="maxConcurrentGameSessionActivations")
    def max_concurrent_game_session_activations(self) -> Optional[_builtins.int]: ...
    @_builtins.property
    @pulumi.getter(name="serverProcesses")
    def server_processes(
        self,
    ) -> Optional[Sequence[outputs.FleetRuntimeConfigurationServerProcess]]: ...

@pulumi.output_type
class FleetRuntimeConfigurationServerProcess(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        concurrent_executions: _builtins.int,
        launch_path: _builtins.str,
        parameters: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="concurrentExecutions")
    def concurrent_executions(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="launchPath")
    def launch_path(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def parameters(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GameServerGroupAutoScalingPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        target_tracking_configuration: outputs.GameServerGroupAutoScalingPolicyTargetTrackingConfiguration,
        estimated_instance_warmup: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetTrackingConfiguration")
    def target_tracking_configuration(
        self,
    ) -> outputs.GameServerGroupAutoScalingPolicyTargetTrackingConfiguration: ...
    @_builtins.property
    @pulumi.getter(name="estimatedInstanceWarmup")
    def estimated_instance_warmup(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class GameServerGroupAutoScalingPolicyTargetTrackingConfiguration(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(__self__, *, target_value: _builtins.float) -> None: ...
    @_builtins.property
    @pulumi.getter(name="targetValue")
    def target_value(self) -> _builtins.float: ...

@pulumi.output_type
class GameServerGroupInstanceDefinition(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        instance_type: _builtins.str,
        weighted_capacity: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="instanceType")
    def instance_type(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="weightedCapacity")
    def weighted_capacity(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GameServerGroupLaunchTemplate(dict):
    def __init__(
        __self__,
        *,
        id: Optional[_builtins.str] = ...,
        name: Optional[_builtins.str] = ...,
        version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def id(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def name(self) -> Optional[_builtins.str]: ...
    @_builtins.property
    @pulumi.getter
    def version(self) -> Optional[_builtins.str]: ...

@pulumi.output_type
class GameSessionQueuePlayerLatencyPolicy(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        maximum_individual_player_latency_milliseconds: _builtins.int,
        policy_duration_seconds: Optional[_builtins.int] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter(name="maximumIndividualPlayerLatencyMilliseconds")
    def maximum_individual_player_latency_milliseconds(self) -> _builtins.int: ...
    @_builtins.property
    @pulumi.getter(name="policyDurationSeconds")
    def policy_duration_seconds(self) -> Optional[_builtins.int]: ...

@pulumi.output_type
class ScriptStorageLocation(dict):
    def __getitem__(self, key: str) -> Any: ...
    def get(self, key: str, default=...) -> Any: ...
    def __init__(
        __self__,
        *,
        bucket: _builtins.str,
        key: _builtins.str,
        role_arn: _builtins.str,
        object_version: Optional[_builtins.str] = ...,
    ) -> None: ...
    @_builtins.property
    @pulumi.getter
    def bucket(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter
    def key(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="roleArn")
    def role_arn(self) -> _builtins.str: ...
    @_builtins.property
    @pulumi.getter(name="objectVersion")
    def object_version(self) -> Optional[_builtins.str]: ...
